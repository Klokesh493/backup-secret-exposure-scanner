# Backup Secret Exposure Scanner architecture

Scans backup logs for leaked tokens, keys, and connection strings before ticket sharing.

```mermaid
flowchart LR
    N0["sample_backup.log"]
    N1["secret_scanner.py"]
    N2["scan"]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
