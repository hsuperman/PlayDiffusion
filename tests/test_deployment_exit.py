"""Exercise the deployment-check entry point without a Modal request."""
import contextlib
import io
from pathlib import Path
import runpy
import sys
import types
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "quick_test.py"

class DeploymentExitTests(unittest.TestCase):
    def run_check(self, lookup):
        modal = types.ModuleType("modal")
        modal.Cls = types.SimpleNamespace(lookup=lookup)
        with patch.dict(sys.modules, {"modal": modal}), contextlib.redirect_stdout(io.StringIO()):
            try:
                runpy.run_path(str(SCRIPT), run_name="__main__")
            except SystemExit as result:
                return result.code
        return 0

    def test_lookup_failure_exits_nonzero(self):
        def fail(*args):
            raise RuntimeError("deployment unavailable")
        self.assertEqual(self.run_check(fail), 1)

    def test_lookup_success_exits_zero(self):
        self.assertEqual(self.run_check(lambda *args: object()), 0)

if __name__ == "__main__":
    unittest.main()
