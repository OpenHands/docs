## Invariants (Normative)

### Workspace Factory: Host Chooses Remote

The `Workspace(...)` constructor is a factory:

- If `host` is provided, it returns a `RemoteWorkspace`.
- Otherwise it returns a `LocalWorkspace`.

OCL-like (conceptual):

- `context Workspace::__new__ post RemoteIffHost: (host <> null) implies result.oclIsKindOf(RemoteWorkspace)`


### BaseWorkspace Contract

All workspace implementations must satisfy:

- `execute_command(command, cwd, timeout)` returns a `CommandResult` where `exit_code=-1` indicates timeout.
- `file_upload` / `file_download` return a `FileOperationResult` with `success=false` and a populated `error` field on failure.
- Git helpers (`git_changes`, `git_diff`) must raise if the path is not a git repository.

### working_dir Normalization

Natural language invariant:

- `working_dir` is normalized to a `str` even if passed as a `Path`.

### Pause/Resume Semantics (Optional Capability)

`pause()` / `resume()` are intentionally **optional capabilities**:

- `LocalWorkspace.pause()` / `.resume()` are no-ops.
- Remote/container workspaces may implement pause/resume to conserve resources.
- If a workspace type does not support pausing, it must raise `NotImplementedError`.

#### Discussion: `pause()` / `resume()` semantics (design tradeoff)

There is an argument that this is compatible with the “swap workspaces without rewriting code” principle, because most client code should only rely on the *core* workspace and conversation operations, while optional capabilities are feature-detected or used conditionally.

There is a mild design smell here: the method names `pause()` / `resume()` suggest a strong guarantee (that work is actually suspended), but the SDK currently treats them as a **best-effort resource management hook**.

- Locally, there is often nothing meaningful the workspace can suspend at the boundary (it is operating on the host OS), so `LocalWorkspace.pause()` is a no-op.
- Some remote/container workspaces may be able to pause a container or VM, but others may not.

This tension matters because it creates two different reasonable expectations:

1. *Ergonomic expectation*: orchestration code can call `pause()` unconditionally and it will be safe.
2. *Guarantee expectation*: calling `pause()` actually pauses resource usage.

**Maybe it would make sense to** model this explicitly as an optional capability:

- Add `supports_pause` (or a richer `pause_capability`) to `BaseWorkspace`, and
- Make `pause()` / `resume()` no-ops everywhere by default (including remote) while letting pausable implementations override,
- Keep a strict helper (e.g., `pause_or_raise()`) for callers who require a guarantee.

This would make the default behavior unsurprising (safe to call), while still letting clients opt into fail-fast behavior when pausing is required.


### File Operations

| Operation | Local Implementation | Remote Implementation |
|-----------|---------------------|----------------------|
| **Upload** | `shutil.copy()` | `POST /file/upload` with multipart |
| **Download** | `shutil.copy()` | `GET /file/download` stream |
| **Result** | `FileOperationResult` | `FileOperationResult` |
