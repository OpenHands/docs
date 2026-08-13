import importlib.util
from pathlib import Path
import sys


SCRIPT_PATH = Path(__file__).parents[1] / "scripts" / "generate-llms-files.py"
SPEC = importlib.util.spec_from_file_location("generate_llms_files", SCRIPT_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def test_iter_doc_pages_excludes_former_monorepo_architecture() -> None:
    paths = {page.rel_path for page in MODULE.iter_doc_pages()}

    assert Path("openhands/usage/architecture/backend.mdx") not in paths
    assert Path("openhands/usage/architecture/runtime.mdx") not in paths
    assert Path("openhands/usage/agent-canvas/architecture.mdx") in paths
