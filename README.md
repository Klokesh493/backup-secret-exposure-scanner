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

## Local verification

Run `make verify` with Make and Python 3 installed. The target runs the documented sample through the project CLI. It also runs the existing Python unit tests.

## Project walkthrough

```mermaid
flowchart LR
    A["Backup log file"]
    B["Count matches by token, password, and key pattern"]
    C{"Matching pattern present?"}
    D["Emit finding category and count"]
    E["Omit categories with zero matches"]
    A --> B --> C
    C -->|Yes| D
    C -->|No| E
```

[Architecture and data flow](docs/ARCHITECTURE.md) · [Business problem, demo, and verification](docs/CASE_STUDY.md)
