# All Hands AI Documentation

This repository aggregates documentation from multiple All Hands AI repositories to provide a unified documentation site powered by Mintlify.

## Structure

- `docs.json` - Mintlify configuration file that references docs in these repos.
- `openhands/` - Main OpenHands docs.
- `openapi/` - API References.
- `sdk/` - Agent SDK docs.
- `success-stories/` - Success stories docs.

## Adding New Documentation Sources

To add documentation from a new repository:

1. Add workflow [like this](https://github.com/All-Hands-AI/agent-sdk/blob/main/.github/workflows/deploy-docs.yml) to the new repo.
2. Update `docs.json` to include navigation for the new content (e.g., `new-repo/docs/`)

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
