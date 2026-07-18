# Backup Secret Exposure Scanner

Scans backup logs for leaked tokens, keys, and connection strings before ticket sharing.

Focus: Backup-platform DevSecOps security.

Built as a small, runnable Python project with clear input, output, sample data, and tests.

## Run

```bash
python3 secret_scanner.py sample_backup.log
```

## Verify

```bash
python3 -m unittest discover . -v
```
