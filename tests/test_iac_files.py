import unittest
import os

class IaCTest(unittest.TestCase):
    IAC_DIR = os.path.join(os.path.dirname(__file__), '..', 'iac')
    REQUIRED_FILES = [
        "main.tf",
        "variables.tf",
        "outputs.tf",
        "vpc.tf",
        "ec2.tf",
        "s3.tf",
        "lambda.tf",
        "iam.tf",
        "guardduty.tf"
    ]

    def test_iac_files_exist(self):
        missing = []
        for f in self.REQUIRED_FILES:
            if not os.path.isfile(os.path.join(self.IAC_DIR, f)):
                missing.append(f)
        self.assertFalse(missing, f"Missing IaC files: {missing}")

if __name__ == "__main__":
    unittest.main()
