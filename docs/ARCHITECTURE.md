# Backup Secret Exposure Scanner architecture

Scans backup logs for leaked tokens, keys, and connection strings before ticket sharing.

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

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
