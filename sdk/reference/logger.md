## `openhands.sdk.logger`

**Modules:**

- [**logger**](#openhands.sdk.logger.logger) – Minimal logger setup that encourages per-module loggers,
- [**rolling**](#openhands.sdk.logger.rolling) –

**Functions:**

- [**get_logger**](#openhands.sdk.logger.get_logger) – Return a logger for the given module name.
- [**rolling_log_view**](#openhands.sdk.logger.rolling_log_view) – Temporarily attach a rolling view handler that renders the last N log lines.
- [**setup_logging**](#openhands.sdk.logger.setup_logging) – Configure the root logger. All child loggers inherit this setup.

**Attributes:**

- [**DEBUG**](#openhands.sdk.logger.DEBUG) –
- [**ENV_JSON**](#openhands.sdk.logger.ENV_JSON) –
- [**ENV_LOG_DIR**](#openhands.sdk.logger.ENV_LOG_DIR) –
- [**ENV_LOG_LEVEL**](#openhands.sdk.logger.ENV_LOG_LEVEL) –
- [**IN_CI**](#openhands.sdk.logger.IN_CI) –

### `openhands.sdk.logger.DEBUG`

```python
DEBUG = os.environ.get('DEBUG', 'false').lower() in {'1', 'true', 'yes'}
```

### `openhands.sdk.logger.ENV_JSON`

```python
ENV_JSON = os.getenv('LOG_JSON', 'false').lower() in {'1', 'true', 'yes'}
```

### `openhands.sdk.logger.ENV_LOG_DIR`

```python
ENV_LOG_DIR = os.getenv('LOG_DIR', 'logs')
```

### `openhands.sdk.logger.ENV_LOG_LEVEL`

```python
ENV_LOG_LEVEL = LEVEL_MAP.get(ENV_LOG_LEVEL_STR, logging.INFO)
```

### `openhands.sdk.logger.IN_CI`

```python
IN_CI = os.getenv('CI', 'false').lower() in {'1', 'true', 'yes'} or bool(os.environ.get('GITHUB_ACTIONS'))
```

### `openhands.sdk.logger.get_logger`

```python
get_logger(name)
```

Return a logger for the given module name.

### `openhands.sdk.logger.logger`

Minimal logger setup that encourages per-module loggers,
with Rich for humans and JSON for machines.

<details class="usage" open markdown="1">
<summary>Usage</summary>

from openhands.sdk.logger import get_logger
logger = get_logger(__name__)
logger.info("Hello from this module!")

</details>

**Functions:**

- [**disable_logger**](#openhands.sdk.logger.logger.disable_logger) – Disable or quiet down a specific logger by name.
- [**get_logger**](#openhands.sdk.logger.logger.get_logger) – Return a logger for the given module name.
- [**setup_logging**](#openhands.sdk.logger.logger.setup_logging) – Configure the root logger. All child loggers inherit this setup.

**Attributes:**

- [**DEBUG**](#openhands.sdk.logger.logger.DEBUG) –
- [**ENV_AUTO_CONFIG**](#openhands.sdk.logger.logger.ENV_AUTO_CONFIG) –
- [**ENV_BACKUP_COUNT**](#openhands.sdk.logger.logger.ENV_BACKUP_COUNT) –
- [**ENV_DEBUG_LLM**](#openhands.sdk.logger.logger.ENV_DEBUG_LLM) –
- [**ENV_JSON**](#openhands.sdk.logger.logger.ENV_JSON) –
- [**ENV_LOG_DIR**](#openhands.sdk.logger.logger.ENV_LOG_DIR) –
- [**ENV_LOG_LEVEL**](#openhands.sdk.logger.logger.ENV_LOG_LEVEL) –
- [**ENV_LOG_LEVEL_STR**](#openhands.sdk.logger.logger.ENV_LOG_LEVEL_STR) –
- [**ENV_LOG_TO_FILE**](#openhands.sdk.logger.logger.ENV_LOG_TO_FILE) –
- [**ENV_RICH_TRACEBACKS**](#openhands.sdk.logger.logger.ENV_RICH_TRACEBACKS) –
- [**ENV_ROTATE_WHEN**](#openhands.sdk.logger.logger.ENV_ROTATE_WHEN) –
- [**IN_CI**](#openhands.sdk.logger.logger.IN_CI) –
- [**LEVEL_MAP**](#openhands.sdk.logger.logger.LEVEL_MAP) –
- [**confirmation**](#openhands.sdk.logger.logger.confirmation) –

#### `openhands.sdk.logger.logger.DEBUG`

```python
DEBUG = os.environ.get('DEBUG', 'false').lower() in {'1', 'true', 'yes'}
```

#### `openhands.sdk.logger.logger.ENV_AUTO_CONFIG`

```python
ENV_AUTO_CONFIG = os.getenv('LOG_AUTO_CONFIG', 'true').lower() in {'1', 'true', 'yes'}
```

#### `openhands.sdk.logger.logger.ENV_BACKUP_COUNT`

```python
ENV_BACKUP_COUNT = int(os.getenv('LOG_BACKUP_COUNT', '7'))
```

#### `openhands.sdk.logger.logger.ENV_DEBUG_LLM`

```python
ENV_DEBUG_LLM = os.getenv('DEBUG_LLM', 'false').lower() in {'1', 'true', 'yes'}
```

#### `openhands.sdk.logger.logger.ENV_JSON`

```python
ENV_JSON = os.getenv('LOG_JSON', 'false').lower() in {'1', 'true', 'yes'}
```

#### `openhands.sdk.logger.logger.ENV_LOG_DIR`

```python
ENV_LOG_DIR = os.getenv('LOG_DIR', 'logs')
```

#### `openhands.sdk.logger.logger.ENV_LOG_LEVEL`

```python
ENV_LOG_LEVEL = LEVEL_MAP.get(ENV_LOG_LEVEL_STR, logging.INFO)
```

#### `openhands.sdk.logger.logger.ENV_LOG_LEVEL_STR`

```python
ENV_LOG_LEVEL_STR = os.getenv('LOG_LEVEL', 'INFO').upper()
```

#### `openhands.sdk.logger.logger.ENV_LOG_TO_FILE`

```python
ENV_LOG_TO_FILE = os.getenv('LOG_TO_FILE', 'false').lower() in {'1', 'true', 'yes'}
```

#### `openhands.sdk.logger.logger.ENV_RICH_TRACEBACKS`

```python
ENV_RICH_TRACEBACKS = os.getenv('LOG_RICH_TRACEBACKS', 'true').lower() in {'1', 'true', 'yes'}
```

#### `openhands.sdk.logger.logger.ENV_ROTATE_WHEN`

```python
ENV_ROTATE_WHEN = os.getenv('LOG_ROTATE_WHEN', 'midnight')
```

#### `openhands.sdk.logger.logger.IN_CI`

```python
IN_CI = os.getenv('CI', 'false').lower() in {'1', 'true', 'yes'} or bool(os.environ.get('GITHUB_ACTIONS'))
```

#### `openhands.sdk.logger.logger.LEVEL_MAP`

```python
LEVEL_MAP = logging.getLevelNamesMapping() if hasattr(logging, 'getLevelNamesMapping') else logging._nameToLevel
```

#### `openhands.sdk.logger.logger.confirmation`

```python
confirmation = input("\n⚠️ WARNING: You are enabling DEBUG_LLM which may expose sensitive information like API keys.\nThis should NEVER be enabled in production.\nType 'y' to confirm you understand the risks: ")
```

#### `openhands.sdk.logger.logger.disable_logger`

```python
disable_logger(name, level=logging.CRITICAL)
```

Disable or quiet down a specific logger by name.

#### `openhands.sdk.logger.logger.get_logger`

```python
get_logger(name)
```

Return a logger for the given module name.

#### `openhands.sdk.logger.logger.setup_logging`

```python
setup_logging(level=None, log_to_file=None, log_dir=None, fmt=None, when=None, backup_count=None)
```

Configure the root logger. All child loggers inherit this setup.

### `openhands.sdk.logger.rolling`

**Functions:**

- [**rolling_log_view**](#openhands.sdk.logger.rolling.rolling_log_view) – Temporarily attach a rolling view handler that renders the last N log lines.

**Attributes:**

- [**RenderFnType**](#openhands.sdk.logger.rolling.RenderFnType) –

#### `openhands.sdk.logger.rolling.RenderFnType`

```python
RenderFnType = Callable[[], str]
```

#### `openhands.sdk.logger.rolling.rolling_log_view`

```python
rolling_log_view(logger, max_lines=60, level=logging.INFO, propagate=False, header=None, footer=None, *, json_flush_level=None)
```

Temporarily attach a rolling view handler that renders the last N log lines.

- Local TTY & not CI & not JSON: pretty, live-updating view (Rich.Live)
- CI / non-TTY: plain line-by-line (no terminal control)
- JSON mode: buffer only; on exit emit ONE large log record with the full snapshot.

### `openhands.sdk.logger.rolling_log_view`

```python
rolling_log_view(logger, max_lines=60, level=logging.INFO, propagate=False, header=None, footer=None, *, json_flush_level=None)
```

Temporarily attach a rolling view handler that renders the last N log lines.

- Local TTY & not CI & not JSON: pretty, live-updating view (Rich.Live)
- CI / non-TTY: plain line-by-line (no terminal control)
- JSON mode: buffer only; on exit emit ONE large log record with the full snapshot.

### `openhands.sdk.logger.setup_logging`

```python
setup_logging(level=None, log_to_file=None, log_dir=None, fmt=None, when=None, backup_count=None)
```

Configure the root logger. All child loggers inherit this setup.
