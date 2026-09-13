# Orchestration guide evidence

September 13, 2026. Guide source: `5b5bf8a8`.

The actual Mintlify page rendered with HTTP 200 and no browser errors. Both Python blocks were extracted unchanged from the guide and executed against an isolated Docker Agent Server containing the unreleased SDK client. The first uploaded a harmless archive and created `Scheduled automation`. A preceding user message configured the workflow to reply `DOCS_ORCHESTRATION_PASS` without tools, GitHub access, secrets, or file changes; it used `run=False`. The second block attached, ran the model, and printed that response. Canvas displayed the resulting conversation and response.

![Rendered guide](https://raw.githubusercontent.com/OpenHands/docs/4b0e728244ae9cbcdd52e8b3b61dfe2cc22511b3/.pr/orchestration-guide.png)
![Documented example's actual Canvas response](https://raw.githubusercontent.com/OpenHands/docs/4b0e728244ae9cbcdd52e8b3b61dfe2cc22511b3/.pr/orchestration-agent.png)

[Credential-free result](https://github.com/OpenHands/docs/blob/4b0e728244ae9cbcdd52e8b3b61dfe2cc22511b3/.pr/orchestration-live.json). The disposable runtime was released after capture. No application repository was modified. The example calls `register_default_tools()` before attachment; this run verifies a simple model response, not every registered tool. The source-built SDK satisfies unreleased prerequisites; this does not claim the current PyPI package contains these APIs.

Reproduce by extracting the guide's Python blocks, supplying an isolated server URL/key and saved profile, calling `dispatch()` with a fixture archive, and executing the attachment block with the returned conversation ID/workspace. Capture the Canvas response before releasing its runtime.
