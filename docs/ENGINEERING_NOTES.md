# Skills and verification

## What this repository demonstrates

Defensive secret detection, bounded UTF-8 log parsing, and redaction of supported credential patterns.

## Reproduce the result

Run `make verify` and `python3 secret_scanner.py sample_backup.log --redact`. Check that passwords and tokens are replaced with category markers. Tests cover escaped and unterminated quotes. Reproduce the primary fixture with `python3 secret_scanner.py sample_backup.log`.

Run `make verify` locally. Ruff and Bandit medium/high checks passed for the checked Python code.

## Scope

The redaction CLI writes a copy to stdout. Pattern coverage is limited to documented signatures, so still review the output before sharing.

[secret_scanner.py](../secret_scanner.py) · [examples/Demo 1.stdout.txt](../examples/Demo%201.stdout.txt) · [Architecture](../docs/ARCHITECTURE.md) · [Case study](../docs/CASE_STUDY.md) · [Runbook](../docs/RUNBOOK.md) · [CI template](../docs/github-actions/ci.yml)
