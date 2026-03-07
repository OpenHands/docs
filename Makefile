.PHONY: llms llms-check

# Regenerate the Mintlify llms context files (V1-only override).
#
# See: scripts/generate-llms-files.py
llms:
	python3 scripts/generate-llms-files.py

# Regenerate and fail if llms files changed (useful for local verification).
llms-check:
	python3 scripts/generate-llms-files.py
	git diff --exit-code llms.txt llms-full.txt
