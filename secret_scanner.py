import re
import sys


PATTERNS = {
    "token": re.compile(r"token=[A-Za-z0-9_\-]{12,}"),
    "password": re.compile(r"password=[^\s]+", re.IGNORECASE),
    "aws_key": re.compile(r"AKIA[0-9A-Z]{16}"),
}


def scan(text):
    return {name: len(pattern.findall(text)) for name, pattern in PATTERNS.items() if pattern.findall(text)}


def main(path):
    result = scan(open(path, encoding="utf-8").read())
    for key, count in result.items():
        print(f"{key}: {count}")


if __name__ == "__main__":
    main(sys.argv[1])
