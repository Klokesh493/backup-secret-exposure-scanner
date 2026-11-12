# Backup Secret Exposure Scanner walkthrough

## Business problem

Scans backup logs for leaked tokens, keys, and connection strings before ticket sharing.

## Reproduce the workflow

Run `python3 secret_scanner.py sample_backup.log` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
token: 1
password: 1
```

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
