---
title: openhands.sdk.logger
description: API reference for openhands.sdk.logger
---

# openhands.sdk.logger package

<a id="module-openhands.sdk.logger"></a>

### openhands.sdk.logger.get_logger(name: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [Logger](https://docs.python.org/3/library/logging.html#logging.Logger)

Return a logger for the given module name.

### openhands.sdk.logger.setup_logging(level: [int](https://docs.python.org/3/library/functions.html#int) | [None](https://docs.python.org/3/library/constants.html#None) = None, log_to_file: [bool](https://docs.python.org/3/library/functions.html#bool) | [None](https://docs.python.org/3/library/constants.html#None) = None, log_dir: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, fmt: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, when: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, backup_count: [int](https://docs.python.org/3/library/functions.html#int) | [None](https://docs.python.org/3/library/constants.html#None) = None) → [None](https://docs.python.org/3/library/constants.html#None)

Configure the root logger. All child loggers inherit this setup.

### openhands.sdk.logger.rolling_log_view(logger: [Logger](https://docs.python.org/3/library/logging.html#logging.Logger), max_lines: [int](https://docs.python.org/3/library/functions.html#int) = 60, level: [int](https://docs.python.org/3/library/functions.html#int) = 20, propagate: [bool](https://docs.python.org/3/library/functions.html#bool) = False, header: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, footer: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, , json_flush_level: [int](https://docs.python.org/3/library/functions.html#int) | [None](https://docs.python.org/3/library/constants.html#None) = None)

Temporarily attach a rolling view handler that renders the last N log lines.

- Local TTY & not CI & not JSON: pretty, live-updating view (Rich.Live)
- CI / non-TTY: plain line-by-line (no terminal control)
- JSON mode: buffer only; on exit emit ONE large log record with the full snapshot.

## Submodules

* [openhands.sdk.logger.logger module](https://github.com/OpenHands/software-agent-sdk/sdk.logger.logger.md)
  * [`disable_logger()`](https://github.com/OpenHands/software-agent-sdk/sdk.logger.logger.md#openhands.sdk.logger.logger.disable_logger)
  * [`setup_logging()`](https://github.com/OpenHands/software-agent-sdk/sdk.logger.logger.md#openhands.sdk.logger.logger.setup_logging)
  * [`get_logger()`](https://github.com/OpenHands/software-agent-sdk/sdk.logger.logger.md#openhands.sdk.logger.logger.get_logger)
* [openhands.sdk.logger.rolling module](https://github.com/OpenHands/software-agent-sdk/sdk.logger.rolling.md)
  * [`rolling_log_view()`](https://github.com/OpenHands/software-agent-sdk/sdk.logger.rolling.md#openhands.sdk.logger.rolling.rolling_log_view)
