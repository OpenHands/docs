#!/usr/bin/env python3
import json
import re
import sys
import urllib.request

LITELLM_URL = "https://raw.githubusercontent.com/BerriAI/litellm/refs/heads/main/model_prices_and_context_window.json"
MDX_PATH = "openhands/usage/llms/openhands-llms.mdx"

# Models to skip from strict validation (absent in LiteLLM DB or intentionally N/A values)
SKIP_MODELS = {
    "qwen3-coder-480b",
    "devstral-medium-2507",
    "devstral-small-2507",
}

# Optional manual key mapping if MDX model name differs from LiteLLM JSON key
MODEL_KEY_MAP: dict[str, str] = {
    # Add mappings here only if necessary
}


def fetch_litellm_db(url: str) -> dict:
    with urllib.request.urlopen(url, timeout=30) as resp:
        data = resp.read()
    return json.loads(data)


def parse_money(s: str) -> float | None:
    s = s.strip()
    if s.upper() in {"N/A", "NA", "-", "—", "--", ""}:
        return None
    if s.startswith("$"):
        s = s[1:]
    try:
        return float(s)
    except ValueError:
        return None


def parse_int(s: str) -> int | None:
    s = s.strip()
    if s.upper() in {"N/A", "NA", "-", "—", "--", ""}:
        return None
    s = s.replace(",", "")
    try:
        return int(s)
    except ValueError:
        return None


def extract_table_from_mdx(path: str) -> list[dict[str, str | None]]:
    rows: list[dict[str, str | None]] = []
    with open(path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    # Find table header
    start = None
    for i, line in enumerate(lines):
        if "| Model |" in line:
            start = i
            break
    if start is None:
        raise SystemExit("ERROR: Could not find LLM pricing table header in MDX file.")

    i = start + 1
    # Skip the separator line (---)
    while i < len(lines) and lines[i].strip().startswith("|"):
        # Stop when we hit a blank line after table
        if not lines[i].strip():
            break
        # Skip header separator row like |-----|
        if re.match(r"^\|\s*-+\s*\|", lines[i]):
            i += 1
            continue
        # Stop when the row clearly ends (non-table line)
        if not lines[i].strip().startswith("|"):
            break

        parts = [p.strip() for p in lines[i].strip().strip("|").split("|")]
        if len(parts) == 6 and parts[0] != "Model":
            rows.append({
                "model": parts[0],
                "input_cost": parts[1],
                "cached_input_cost": parts[2],
                "output_cost": parts[3],
                "max_input_tokens": parts[4],
                "max_output_tokens": parts[5],
            })
        i += 1

    if not rows:
        raise SystemExit("ERROR: Found table header but no data rows parsed.")
    return rows


def to_per_million(val_per_token: float | None) -> float | None:
    if val_per_token is None:
        return None
    return val_per_token * 1_000_000.0


def near(a: float | None, b: float | None, tol: float = 1e-3) -> bool:
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return abs(a - b) <= tol


def main() -> int:
    db = fetch_litellm_db(LITELLM_URL)
    rows = extract_table_from_mdx(MDX_PATH)

    failures: List[str] = []
    validations = 0

    for row in rows:
        model = row["model"]
        if model in SKIP_MODELS:
            continue

        key = MODEL_KEY_MAP.get(model, model)
        entry = db.get(key)
        if entry is None:
            # Try a few fallbacks (provider-prefixed keys)
            # e.g., openai/gpt-5-codex, google/gemini-2.5-pro
            candidates = [
                f"openai/{model}",
                f"azure/{model}",
                f"anthropic/{model}",
                f"google/{model}",
                f"gemini/{model}",
                f"mistral/{model}",
            ]
            for c in candidates:
                if c in db:
                    entry = db[c]
                    key = c
                    break

        if entry is None:
            # Not in LiteLLM DB; skip but report
            print(f"[skip] {model}: not found in LiteLLM DB")
            continue

        # Parse MDX values
        mdx_input_cost = parse_money(row["input_cost"])  # $ per 1M
        mdx_cached_cost = parse_money(row["cached_input_cost"])  # $ per 1M or None
        mdx_output_cost = parse_money(row["output_cost"])  # $ per 1M
        mdx_max_in = parse_int(row["max_input_tokens"])  # tokens
        mdx_max_out = parse_int(row["max_output_tokens"])  # tokens

        # Compute expected from LiteLLM DB
        llm_in_per_token = entry.get("input_cost_per_token")
        llm_cached_per_token = entry.get("cache_read_input_token_cost")
        llm_out_per_token = entry.get("output_cost_per_token")

        exp_input_cost = to_per_million(llm_in_per_token)
        exp_cached_cost = to_per_million(llm_cached_per_token)
        exp_output_cost = to_per_million(llm_out_per_token)

        # Compare costs (only if LLM DB provides them)
        def add_fail(msg: str):
            failures.append(f"{model}: {msg}")

        # Input cost
        if exp_input_cost is not None and mdx_input_cost is not None:
            validations += 1
            if not near(mdx_input_cost, exp_input_cost):
                add_fail(f"input_cost mismatch: mdx={mdx_input_cost} vs litellm={exp_input_cost}")

        # Cached input cost
        if exp_cached_cost is not None or mdx_cached_cost is not None:
            # If JSON missing but MDX has numeric, that's a mismatch; if MDX N/A and JSON missing, accept
            validations += 1
            if exp_cached_cost is None and mdx_cached_cost is None:
                pass
            elif exp_cached_cost is None and mdx_cached_cost is not None:
                add_fail(f"cached_input_cost present in MDX but missing in LiteLLM: mdx={mdx_cached_cost}")
            elif exp_cached_cost is not None and mdx_cached_cost is None:
                add_fail(f"cached_input_cost missing in MDX but present in LiteLLM: litellm={exp_cached_cost}")
            elif not near(mdx_cached_cost, exp_cached_cost):
                add_fail(f"cached_input_cost mismatch: mdx={mdx_cached_cost} vs litellm={exp_cached_cost}")

        # Output cost
        if exp_output_cost is not None and mdx_output_cost is not None:
            validations += 1
            if not near(mdx_output_cost, exp_output_cost):
                add_fail(f"output_cost mismatch: mdx={mdx_output_cost} vs litellm={exp_output_cost}")

        # Token limits (compare only if LiteLLM provides the field)
        llm_max_in = entry.get("max_input_tokens")
        llm_max_out = entry.get("max_output_tokens")

        if llm_max_in is not None and mdx_max_in is not None:
            validations += 1
            if mdx_max_in != int(llm_max_in):
                add_fail(f"max_input_tokens mismatch: mdx={mdx_max_in} vs litellm={llm_max_in}")

        if llm_max_out is not None and mdx_max_out is not None:
            validations += 1
            if mdx_max_out != int(llm_max_out):
                add_fail(f"max_output_tokens mismatch: mdx={mdx_max_out} vs litellm={llm_max_out}")

    if failures:
        print("\nValidation FAILED:\n" + "\n".join(failures))
        return 1

    print(f"Validation passed. Checks performed: {validations}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
