"""Count or redact common credential patterns from a local backup log."""

import argparse
from pathlib import Path
import re
import sys

MAX_LOG_BYTES = 8 * 1024 * 1024

QUOTED = r'''(?:"(?:\\[^\n]|[^"\\\n])*"?|'(?:\\[^\n]|[^'\\\n])*'?)'''
PATTERNS = {
    "token": re.compile(rf"(?i)(\btoken[ \t]*=[ \t]*)(?:{QUOTED}|[\w-]{{12,}})"),
    "password": re.compile(rf"(?i)(\bpassword[ \t]*=[ \t]*)(?:{QUOTED}|[^\s,;]+)"),
    "aws_key": re.compile(r"(\b)(?:AKIA|ASIA)[0-9A-Z]{16}\b"),
}


def scan(text):
    return dict(
        (name, count) for name, pattern in PATTERNS.items()
        if (count := sum(1 for _ in pattern.finditer(text)))
    )


def redact(text):
    for label, pattern in PATTERNS.items():
        text = pattern.sub(lambda match: match[1] + f"<REDACTED:{label}>", text)
    return text


def main(path, *, redact_output=False):
    with Path(path).open("rb") as handle:
        source = handle.read(MAX_LOG_BYTES + 1)
    if len(source) > MAX_LOG_BYTES:
        raise ValueError("input exceeds 8 MiB")
    text = source.decode("utf-8")
    if redact_output:
        sys.stdout.write(redact(text))
    else:
        for key, count in scan(text).items():
            print(f"{key}: {count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    parser.add_argument("--redact", action="store_true", help="emit a redacted copy on stdout")
    args = parser.parse_args()
    try:
        main(args.path, redact_output=args.redact)
    except (OSError, ValueError) as error:
        parser.error(str(error))
