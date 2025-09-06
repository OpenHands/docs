# All Hands AI Documentation

This repository aggregates documentation from multiple All Hands AI repositories to provide a unified documentation site powered by Mintlify.

## Structure

- `openhands/` - Git submodule linking to the OpenHands repository
- `agent-sdk/` - Git submodule linking to the agent-sdk repository
- `docs.json` - Mintlify configuration file that references docs in these repos
- `.github/workflows/` - GitHub Actions for automatic submodule updates

## Adding New Documentation Sources

To add documentation from a new repository:

1. Add the repository as a submodule: `git submodule add https://github.com/All-Hands-AI/new-repo.git new-repo`
2. Update `docs.json` to include navigation for the new content (e.g., `new-repo/docs/`)
3. Update the submodule sync workflow to include the new submodule
4. Commit the changes to register the new submodule

## Working with Submodules

### Initial Setup
```bash
# Clone this repository with submodules
git clone --recursive https://github.com/All-Hands-AI/docs.git

# Or if already cloned, initialize submodules
git submodule update --init --recursive
```

### Updating Submodules
```bash
# Update all submodules to latest commits
git submodule update --remote

# Update specific submodule
git submodule update --remote openhands-repo

# Commit the submodule updates
git add .
git commit -m "Update submodules to latest versions"
```

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
