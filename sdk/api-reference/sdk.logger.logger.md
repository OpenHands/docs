---
title: openhands.sdk.logger.logger
description: API reference for openhands.sdk.logger.logger
---

# openhands.sdk.logger.logger module

<a id="module-openhands.sdk.logger.logger"></a>

Minimal logger setup that encourages per-module loggers,
with Rich for humans and JSON for machines.

Usage:
: from openhands.sdk.logger import get_logger
  logger = get_logger(_\_name_\_)
  logger.info(“Hello from this module!”)

### openhands.sdk.logger.logger.disable_logger(name: [str](https://docs.python.org/3/library/stdtypes.html#str), level: [int](https://docs.python.org/3/library/functions.html#int) = 50) → [None](https://docs.python.org/3/library/constants.html#None)

Disable or quiet down a specific logger by name.

### openhands.sdk.logger.logger.setup_logging(level: [int](https://docs.python.org/3/library/functions.html#int) | [None](https://docs.python.org/3/library/constants.html#None) = None, log_to_file: [bool](https://docs.python.org/3/library/functions.html#bool) | [None](https://docs.python.org/3/library/constants.html#None) = None, log_dir: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, fmt: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, when: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, backup_count: [int](https://docs.python.org/3/library/functions.html#int) | [None](https://docs.python.org/3/library/constants.html#None) = None) → [None](https://docs.python.org/3/library/constants.html#None)

Configure the root logger. All child loggers inherit this setup.

### openhands.sdk.logger.logger.get_logger(name: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [Logger](https://docs.python.org/3/library/logging.html#logging.Logger)

Get a logger instance for the specified module.

This function returns a configured logger that inherits from the root logger
setup. The logger supports both Rich formatting for human-readable output
and JSON formatting for machine processing, depending on environment configuration.

Parameters:
  name – The name of the module, typically \_\_name_\_.
Returns:
  A configured Logger instance.

### Example

```pycon
>>> from openhands.sdk.logger import get_logger
>>> logger = get_logger(__name__)
>>> logger.info("This is an info message")
>>> logger.error("This is an error message")
```
