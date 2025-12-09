#!/usr/bin/env python3
"""
Minimal helper to invoke the OpenHands Cloud API to start a conversation
for weekly documentation automation tasks.

Environment:
- OPENHANDS_API_KEY: required. Cloud API key created at https://app.all-hands.dev/settings/api-keys

Usage:
  python scripts/openhands_api.py \
    --prompt scripts/prompts/architecture_refresh.j2 \
    --repo OpenHands/docs \
    [--base-url https://app.all-hands.dev]

Notes:
- This helper only creates the conversation and prints its URL. The remote
  agent (per your prompt) is expected to open any PRs.
"""
from __future__ import annotations

import argparse
import os
import sys
import textwrap
from dataclasses import dataclass
from typing import Any, Dict

import json
import time
import urllib.request


DEFAULT_BASE_URL = "https://app.all-hands.dev"
API_TIMEOUT = 30


@dataclass
class Conversation:
    id: str
    status: str | None


def _http_json(url: str, method: str, headers: Dict[str, str], data: Dict[str, Any] | None) -> Dict[str, Any]:
    req = urllib.request.Request(url=url, method=method)
    for k, v in headers.items():
        req.add_header(k, v)
    if data is not None:
        payload = json.dumps(data).encode("utf-8")
        req.data = payload
    with urllib.request.urlopen(req, timeout=API_TIMEOUT) as resp:
        body = resp.read().decode("utf-8")
        if not body:
            return {}
        return json.loads(body)


def create_conversation(base_url: str, api_key: str, initial_user_msg: str, repo: str | None = None) -> Conversation:
    url = base_url.rstrip("/") + "/api/conversations"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    payload: Dict[str, Any] = {"initial_user_msg": initial_user_msg}
    if repo:
        payload["repository"] = repo
    data = _http_json(url, "POST", headers, payload)
    conv_id = data.get("conversation_id") or data.get("id") or ""
    status = data.get("status")
    if not conv_id:
        raise RuntimeError(f"Unexpected response creating conversation: {data}")
    return Conversation(id=str(conv_id), status=status)


def read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def build_prompt(prompt_file: str) -> str:
    return read_text(prompt_file)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", required=True, help="Path to prompt file (j2 or txt)")
    parser.add_argument("--repo", required=False, help="Target GitHub repo for the agent to work on, e.g. OpenHands/docs")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL, help="OpenHands API base URL")
    args = parser.parse_args()

    api_key = os.getenv("OPENHANDS_API_KEY") or os.getenv("OPENHANDS_CLOUD_API_KEY") or os.getenv("ALL_HANDS_BOT")
    if not api_key:
        print("ERROR: OPENHANDS_API_KEY (or OPENHANDS_CLOUD_API_KEY / ALL_HANDS_BOT) is not set.", file=sys.stderr)
        return 2

    try:
        initial_user_msg = build_prompt(args.prompt)
    except Exception as e:
        print(f"ERROR: failed to read prompt: {e}", file=sys.stderr)
        return 2

    try:
        conv = create_conversation(args.base_url, api_key, initial_user_msg, repo=args.repo)
    except Exception as e:
        print(f"ERROR: failed to create conversation: {e}", file=sys.stderr)
        return 1

    conv_url = args.base_url.rstrip("/") + f"/conversations/{conv.id}"
    print(f"Created conversation: {conv.id}")
    print(f"URL: {conv_url}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
