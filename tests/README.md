# Documentation Tests

This directory contains tests to verify the consistency and accuracy of the documentation.

## Running Tests

To run the tests, we recommend using `uv` for one-off dependency management:

```bash
uv run --with pytest --with requests pytest -q tests/
```

## Tests

### test_pricing_documentation.py

This test verifies that the pricing information in the OpenHands LLM documentation is:
- Consistent with the LiteLLM pricing data
- Complete (all models are documented)
- Properly formatted
- Up to date with the models listed in the OpenHands codebase

The test fetches data from:
- LiteLLM's pricing JSON: https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
- OpenHands model list: https://github.com/OpenHands/OpenHands/blob/main/openhands/utils/llm.py
