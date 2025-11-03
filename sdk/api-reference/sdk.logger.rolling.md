---
title: openhands.sdk.logger.rolling
description: API reference for openhands.sdk.logger.rolling
---

# openhands.sdk.logger.rolling module

<a id="module-openhands.sdk.logger.rolling"></a>

### openhands.sdk.logger.rolling.rolling_log_view(logger: [Logger](https://docs.python.org/3/library/logging.html#logging.Logger), max_lines: [int](https://docs.python.org/3/library/functions.html#int) = 60, level: [int](https://docs.python.org/3/library/functions.html#int) = 20, propagate: [bool](https://docs.python.org/3/library/functions.html#bool) = False, header: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, footer: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, , json_flush_level: [int](https://docs.python.org/3/library/functions.html#int) | [None](https://docs.python.org/3/library/constants.html#None) = None)

Temporarily attach a rolling view handler that renders the last N log lines.

- Local TTY & not CI & not JSON: pretty, live-updating view (Rich.Live)
- CI / non-TTY: plain line-by-line (no terminal control)
- JSON mode: buffer only; on exit emit ONE large log record with the full snapshot.
