# All Hands AI Documentation

This repository aggregates documentation from multiple All Hands AI repositories to provide a unified documentation site powered by Mintlify.

## Structure

- `docs.json` - Mintlify configuration file that references docs in these repos
- `.github/workflows/` - GitHub Actions for automatic `docs` updates
- `docs/` Folders synced from other repos, e.g., `openhands/`, `agent-sdk/`

## Adding New Documentation Sources

To add documentation from a new repository:

1. Add workflow [like this](https://github.com/All-Hands-AI/agent-sdk/blob/main/.github/workflows/deploy-docs.yml) to the new repo.
2. Update `docs.json` to include navigation for the new content (e.g., `new-repo/docs/`)
3. Commit the changes and manually trigger the [update-docs workflow](.github/workflows/update-docs.yml)


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
