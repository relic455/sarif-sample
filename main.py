"""Entry point for the sarif-sample script."""

import os
import sys

typed_number: int = "not an int"


def lint_and_type_errors(value: int) -> int:
    unused_local = 1
    return value + "1"


def main() -> int:
    """Run the script and report success."""
    sys.stdout.write("Hello from sarif-sample!\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
