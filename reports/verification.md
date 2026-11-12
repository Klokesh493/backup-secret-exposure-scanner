# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 secret_scanner.py sample_backup.log
token: 1
password: 1
test_detects_password_and_token (test_secret_scanner.SecretScannerTest) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
````
