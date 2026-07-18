import unittest

from secret_scanner import scan


class SecretScannerTest(unittest.TestCase):
    def test_detects_password_and_token(self):
        result = scan("password=secret token=abcde12345ABCDE")
        self.assertEqual(result["password"], 1)
        self.assertEqual(result["token"], 1)


if __name__ == "__main__":
    unittest.main()
