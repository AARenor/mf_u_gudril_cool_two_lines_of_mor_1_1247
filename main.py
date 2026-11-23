"""Write the make.fun entry text to a file, byte for byte, no trailing newline."""

import os
import sys
from pathlib import Path

TEXT = (
    "The cat has not moved since six.\n"
    "The square of light has, and takes her with it."
)


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"text length {len(TEXT)} outside 1..280"

    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
