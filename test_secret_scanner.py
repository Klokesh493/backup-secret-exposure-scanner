import unittest

from secret_scanner import redact, scan


class SecretScannerTest(unittest.TestCase):
    def test_detects_password_and_token(self):
        result = scan("password=secret token=abcde12345ABCDE")
        self.assertEqual(result["password"], 1)
        self.assertEqual(result["token"], 1)

    def test_redaction_removes_values_and_preserves_adjacent_fields(self):
        source = 'password="sample secret" token=abcde12345ABCDE x=ok\n'
        expected = "password=<REDACTED:password> token=<REDACTED:token> x=ok\n"
        self.assertEqual(redact(source), expected)

    def test_redacts_temporary_aws_key_pattern(self):
        synthetic_key = "ASIA" + "Z" * 16
        self.assertEqual(redact("key " + synthetic_key), "key <REDACTED:aws_key>")

    def test_escaped_quotes_do_not_leave_a_password_suffix(self):
        source = r'password="sample\"secret" x=ok'
        self.assertEqual(redact(source), 'password=<REDACTED:password> x=ok')

    def test_unclosed_quote_is_redacted_to_end_of_line(self):
        self.assertEqual(redact('password="unfinished value\nx=ok'), 'password=<REDACTED:password>\nx=ok')


if __name__ == "__main__":
    unittest.main()
