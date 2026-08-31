# OpenHands Documentation

This repository provides a unified documentation site powered by Mintlify.

## Structure

- `docs.json` - Mintlify configuration file that references docs in these repos.
- `openhands/` - Main OpenHands docs.
- `openapi/` - API References.
- `sdk/` - Agent SDK docs.
- `success-stories/` - Success stories docs.

## Local Development

To run the documentation site locally:

```bash
npm install -g mint
# or
yarn global add mint

# Preview local changes
mint dev
```

## Deployment

The documentation site is automatically deployed via Mintlify when changes are pushed to the main branch.

## Repository boundaries

This site documents a multi-repository OpenHands system. [`OpenHands/OpenHands`](https://github.com/OpenHands/OpenHands) owns Agent Canvas, [`OpenHands/software-agent-sdk`](https://github.com/OpenHands/software-agent-sdk) owns the Python SDK and Agent Server, [`OpenHands/typescript-client`](https://github.com/OpenHands/typescript-client) owns the browser client for the Agent Server API, [`OpenHands/automation`](https://github.com/OpenHands/automation) owns scheduling and dispatch, and [`OpenHands/extensions`](https://github.com/OpenHands/extensions) owns reusable skills, plugins, automations, and integrations.

The usual API flow is SDK/Agent Server → OpenAPI contract → TypeScript client → Agent Canvas. Documentation should preserve these ownership boundaries; a PR opened in the wrong repository should be closed and moved to the repository that owns the change.
