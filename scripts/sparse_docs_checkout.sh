#!/usr/bin/env bash
set -euo pipefail

MODULE="${1:-}"
if [[ -z "${MODULE}" ]]; then
  echo "Usage: $0 <submodule-path>"
  exit 2
fi

# Ensure the submodule exists locally
if [[ ! -d "${MODULE}" ]]; then
  git submodule update --init -- "${MODULE}"
fi

# Fetch latest for the submodule from its configured branch
git submodule update --remote --checkout -- "${MODULE}"

# Enable sparse-checkout: only keep docs/
if git -C "${MODULE}" sparse-checkout -h >/dev/null 2>&1; then
  # Modern sparse-checkout (preferred)
  git -C "${MODULE}" sparse-checkout init --cone
  git -C "${MODULE}" sparse-checkout set docs
else
  # Fallback for older git
  git -C "${MODULE}" config core.sparseCheckout true
  mkdir -p "${MODULE}/.git/info"
  printf "docs/\n" > "${MODULE}/.git/info/sparse-checkout"
  git -C "${MODULE}" read-tree -mu HEAD
fi
