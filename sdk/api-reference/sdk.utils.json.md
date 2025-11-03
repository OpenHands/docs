---
title: openhands.sdk.utils.json
description: API reference for openhands.sdk.utils.json
---

# openhands.sdk.utils.json module

<a id="module-openhands.sdk.utils.json"></a>

### class openhands.sdk.utils.json.OpenHandsJSONEncoder(, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False, indent=None, separators=None, default=None)

Bases: [`JSONEncoder`](https://docs.python.org/3/library/json.html#json.JSONEncoder)

Custom JSON encoder that handles datetime and other OH objects

#### default(o: [object](https://docs.python.org/3/library/functions.html#object)) → [Any](https://docs.python.org/3/library/typing.html#typing.Any)

Implement this method in a subclass such that it returns
a serializable object for `o`, or calls the base implementation
(to raise a `TypeError`).

For example, to support arbitrary iterators, you could
implement default like this:

```default
def default(self, o):
    try:
        iterable = iter(o)
    except TypeError:
        pass
    else:
        return list(iterable)
    # Let the base class default method raise the TypeError
    return super().default(o)
```

### openhands.sdk.utils.json.dumps(obj, **kwargs)

Serialize an object to str format

### openhands.sdk.utils.json.loads(json_str, **kwargs)

Create a JSON object from str
