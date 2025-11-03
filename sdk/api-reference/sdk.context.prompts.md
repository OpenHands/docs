---
title: openhands.sdk.context.prompts
description: API reference for openhands.sdk.context.prompts
---

# openhands.sdk.context.prompts package

<a id="module-openhands.sdk.context.prompts"></a>

### openhands.sdk.context.prompts.render_template(prompt_dir: [str](https://docs.python.org/3/library/stdtypes.html#str), template_name: [str](https://docs.python.org/3/library/stdtypes.html#str), **ctx) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Render a Jinja2 template.

Parameters:
  * prompt_dir – The base directory for relative template paths.
  * template_name – The template filename. Can be either:
    - A relative filename (e.g., “system_prompt.j2”) loaded from prompt_dir
    - An absolute path (e.g., “/path/to/custom_prompt.j2”)
  * **ctx – Template context variables.
Returns:
  Rendered template string.
Raises:
  [FileNotFoundError](https://docs.python.org/3/library/exceptions.html#FileNotFoundError) – If the template file cannot be found.

## Submodules

* [openhands.sdk.context.prompts.prompt module](https://github.com/OpenHands/software-agent-sdk/sdk.context.prompts.prompt.md)
  * [`refine()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.prompts.prompt.md#openhands.sdk.context.prompts.prompt.refine)
  * [`render_template()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.prompts.prompt.md#openhands.sdk.context.prompts.prompt.render_template)
