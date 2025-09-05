# Documentation Repository Setup Plan

## Overview

This document outlines the complete setup for the All Hands AI documentation repository that aggregates docs from multiple repositories using Git submodules and Mintlify.

## Architecture

```
All-Hands-AI/docs (main documentation repo)
├── docs.json                    # Mintlify configuration (root level)
├── openhands-repo/             # Git submodule → All-Hands-AI/OpenHands
│   └── docs/                   # OpenHands documentation content
├── .github/workflows/          # Automation workflows
└── README.md                   # Usage instructions
```

## Implementation Status

### ✅ Completed

1. **Repository Setup**
   - Created empty main branch in `All-Hands-AI/docs`
   - Added OpenHands as git submodule (`openhands-repo/`)
   - Configured git user credentials

2. **Mintlify Configuration**
   - Moved `docs.json` from `OpenHands/docs/` to root of docs repo
   - Updated all paths to reference `openhands-repo/docs/`
   - Maintained all navigation, theming, and API reference configuration

3. **Documentation Structure**
   - Created comprehensive README with submodule usage instructions
   - Added setup and maintenance documentation

4. **Automation Workflows (Docs Repo)**
   - `update-submodules.yml`: Updates specific submodules via repository dispatch or all submodules on schedule
   - Handles both targeted updates (from source repos) and scheduled bulk updates
   - Manual trigger capability

### 🔄 Next Steps

1. **Add Trigger Workflow to OpenHands Repo**
   - Copy `dispatch-to-docs.yml` to `OpenHands/.github/workflows/dispatch-to-docs.yml`
   - This will trigger docs repo updates when OpenHands docs change

2. **Configure Mintlify Deployment**
   - Connect the docs repository to Mintlify
   - Set up automatic deployment on main branch changes

3. **Test the Complete Flow**
   - Make a test change to OpenHands docs
   - Verify the trigger workflow runs
   - Confirm submodule updates automatically
   - Check that Mintlify rebuilds the site

## Workflow Details

### Automatic Synchronization Flow

1. **Developer makes changes to OpenHands/docs/**
2. **Changes are pushed/merged to main branch**
3. **OpenHands dispatch workflow runs** (`dispatch-to-docs.yml`)
4. **Docs repo receives repository dispatch event with module info**
5. **Docs repo update workflow runs** (`update-submodules.yml`)
6. **Specific submodule (openhands-repo) is updated to latest commit**
7. **Changes are committed and pushed to docs repo**
8. **Mintlify automatically rebuilds and deploys the site**

### Manual Operations

```bash
# Clone with submodules
git clone --recursive https://github.com/All-Hands-AI/docs.git

# Update submodules manually
git submodule update --remote
git add .
git commit -m "Update submodules"
git push

# Add new repository as submodule
git submodule add https://github.com/All-Hands-AI/new-repo.git new-repo
# Update docs.json to include new-repo/docs/ paths
git add .
git commit -m "Add new-repo submodule"
git push
```

## Benefits of This Approach

1. **Version Control**: Exact commit tracking for each source repo
2. **No Duplication**: Direct links to source repositories
3. **Automatic Updates**: GitHub Actions handle synchronization
4. **Scalable**: Easy to add new repositories
5. **Maintainable**: Clear separation of concerns
6. **Transparent**: Easy to see what version of docs is deployed

## Future Enhancements

1. **Multi-repo Support**: Add agent-sdk, evaluation, etc.
2. **Selective Updates**: Only update specific submodules when their docs change
3. **Preview Deployments**: Deploy preview sites for PR changes
4. **Content Validation**: Lint and validate documentation on updates
5. **Analytics**: Track documentation usage and popular sections

## Troubleshooting

### Submodule Issues
```bash
# Reset submodules if they get out of sync
git submodule deinit --all
git submodule update --init --recursive

# Force update if conflicts occur
git submodule update --remote --force
```

### Workflow Issues
- Check GitHub Actions logs in both repositories
- Verify repository dispatch permissions
- Ensure GITHUB_TOKEN has necessary permissions

## Security Considerations

- Uses repository-scoped GITHUB_TOKEN (no additional secrets needed)
- Repository dispatch events are limited to organization members
- Submodule updates only pull from trusted repositories
- All changes are tracked in git history