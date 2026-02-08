"""Entry point for the sarif-sample script."""

import sys


def main() -> int:
    """Run the script and report success."""
    sys.stdout.write("Hello from sarif-sample!\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
