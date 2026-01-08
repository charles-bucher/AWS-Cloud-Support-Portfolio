import unittest
import os
import importlib.util

class ScriptsTest(unittest.TestCase):
    SCRIPT_DIR = os.path.join(os.path.dirname(__file__), '..', 'scripts')

    def test_scripts_importable(self):
        py_files = [f for f in os.listdir(self.SCRIPT_DIR) if f.endswith('.py')]
        errors = []
        for f in py_files:
            file_path = os.path.join(self.SCRIPT_DIR, f)
            spec = importlib.util.spec_from_file_location("module.name", file_path)
            try:
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
            except Exception as e:
                errors.append(f"{f}: {e}")
        self.assertFalse(errors, f"Scripts failed to import: {errors}")

if __name__ == "__main__":
    unittest.main()
