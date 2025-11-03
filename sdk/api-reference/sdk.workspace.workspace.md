---
title: openhands.sdk.workspace.workspace
description: API reference for openhands.sdk.workspace.workspace
---

# openhands.sdk.workspace.workspace module

<a id="module-openhands.sdk.workspace.workspace"></a>

### *class* openhands.sdk.workspace.workspace.Workspace(, working_dir: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'workspace/project')

### *class* openhands.sdk.workspace.workspace.Workspace(, host: [str](https://docs.python.org/3/library/stdtypes.html#str), working_dir: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'workspace/project', api_key: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None)

Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Factory entrypoint that returns a LocalWorkspace or RemoteWorkspace.

Usage:
: - Workspace(working_dir=…) -> LocalWorkspace
  - Workspace(working_dir=…, host=”[http://](http://)…”) -> RemoteWorkspace
