import unittest
import os

class ScreenshotsTest(unittest.TestCase):
    SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), '..', 'screenshots')
    EXPECTED_FILES = [
        "ec2-security-groups.png",
        "s3-bucket-config.png",
        "cloudwatch-lambda-metrics.png",
        "iam-role-policies.png",
        "guardduty-findings.png"
    ]

    def test_screenshots_exist(self):
        missing_files = []
        for f in self.EXPECTED_FILES:
            if not os.path.isfile(os.path.join(self.SCREENSHOT_DIR, f)):
                missing_files.append(f)
        self.assertFalse(missing_files, f"Missing screenshots: {missing_files}")

if __name__ == "__main__":
    unittest.main()
