SHELL := /usr/bin/env bash
.SHELLFLAGS := -eu -o pipefail -c

# Colors for output
ECHO := printf '%b\n'
GREEN := \033[32m
YELLOW := \033[33m
RED := \033[31m
CYAN := \033[36m
UNDERLINE := \033[4m
RESET := \033[0m

.PHONY: help run lint clean llms llms-check sync-code test api-docs install-mintlify

# Default target
.DEFAULT_GOAL := help

# Show help
help:
	@$(ECHO) "$(CYAN)OpenHands Docs Makefile$(RESET)"
	@$(ECHO) ""
	@$(ECHO) "$(UNDERLINE)Usage:$(RESET) make <command>"
	@$(ECHO) ""
	@$(ECHO) "$(UNDERLINE)Development:$(RESET)"
	@$(ECHO) "  $(GREEN)run$(RESET)              Start Mintlify local dev server"
	@$(ECHO) "  $(GREEN)install-mintlify$(RESET) Install Mintlify CLI globally"
	@$(ECHO) ""
	@$(ECHO) "$(UNDERLINE)Validation:$(RESET)"
	@$(ECHO) "  $(GREEN)lint$(RESET)             Check for broken links"
	@$(ECHO) "  $(GREEN)test$(RESET)             Run pytest checks (LLM pricing, sync)"
	@$(ECHO) ""
	@$(ECHO) "$(UNDERLINE)Code Sync (from software-agent-sdk):$(RESET)"
	@$(ECHO) "  $(GREEN)sync-code$(RESET)        Sync code blocks from agent-sdk examples"
	@$(ECHO) "  $(GREEN)api-docs$(RESET)         Generate SDK API reference docs"
	@$(ECHO) ""
	@$(ECHO) "$(UNDERLINE)LLM Context Files:$(RESET)"
	@$(ECHO) "  $(GREEN)llms$(RESET)             Regenerate llms.txt and llms-full.txt"
	@$(ECHO) "  $(GREEN)llms-check$(RESET)       Regenerate and verify no changes"
	@$(ECHO) ""
	@$(ECHO) "$(UNDERLINE)Maintenance:$(RESET)"
	@$(ECHO) "  $(GREEN)clean$(RESET)            Clean up generated/cache files"
	@$(ECHO) "  $(GREEN)help$(RESET)             Show this help message"

# Install Mintlify CLI
install-mintlify:
	@$(ECHO) "$(YELLOW)Installing Mintlify CLI...$(RESET)"
	@npm install -g mintlify@latest
	@$(ECHO) "$(GREEN)Mintlify CLI installed successfully.$(RESET)"

# Start Mintlify local development server
run:
	@$(ECHO) "$(CYAN)Starting Mintlify dev server...$(RESET)"
	@mintlify dev

# Check for broken links
lint:
	@$(ECHO) "$(YELLOW)Checking for broken links...$(RESET)"
	@mintlify broken-links
	@$(ECHO) "$(GREEN)Link check completed.$(RESET)"

# Run pytest checks
test:
	@$(ECHO) "$(YELLOW)Running pytest checks...$(RESET)"
	@uv run --with pytest --with requests pytest -q tests/
	@$(ECHO) "$(GREEN)Tests completed.$(RESET)"

# Sync code blocks from agent-sdk examples
sync-code:
	@$(ECHO) "$(YELLOW)Syncing code blocks from software-agent-sdk...$(RESET)"
	@if [ ! -d "agent-sdk" ]; then \
		$(ECHO) "$(CYAN)Cloning software-agent-sdk...$(RESET)"; \
		git clone --depth 1 https://github.com/OpenHands/software-agent-sdk.git agent-sdk; \
	fi
	@python3 .github/scripts/sync_code_blocks.py
	@$(ECHO) "$(GREEN)Code blocks synced successfully.$(RESET)"

# Generate SDK API reference docs
api-docs:
	@$(ECHO) "$(YELLOW)Generating SDK API reference docs...$(RESET)"
	@uv run --with sphinx --with sphinx-markdown-builder --with myst-parser \
		python scripts/generate-api-docs.py
	@$(ECHO) "$(GREEN)API docs generated successfully.$(RESET)"

# Regenerate llms.txt and llms-full.txt (V1-only override)
llms:
	@$(ECHO) "$(YELLOW)Regenerating LLM context files...$(RESET)"
	@python3 scripts/generate-llms-files.py
	@$(ECHO) "$(GREEN)LLM context files regenerated.$(RESET)"

# Regenerate and verify no changes (for CI/local verification)
llms-check:
	@$(ECHO) "$(YELLOW)Checking LLM context files...$(RESET)"
	@python3 scripts/generate-llms-files.py
	@git diff --exit-code llms.txt llms-full.txt
	@$(ECHO) "$(GREEN)LLM context files are up to date.$(RESET)"

# Clean up generated and cache files
clean:
	@$(ECHO) "$(YELLOW)Cleaning up...$(RESET)"
	@rm -rf agent-sdk 2>/dev/null || true
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@rm -rf .pytest_cache 2>/dev/null || true
	@$(ECHO) "$(GREEN)Clean completed.$(RESET)"
