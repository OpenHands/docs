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
