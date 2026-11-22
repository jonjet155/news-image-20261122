#!/usr/bin/env python3
"""news-image-20261122 entrypoint.

Copies the pre-built front page (entry.png, 1024x1024, Sunday
22 November 2026: 35 stories, 6 regions) to $MAKEFUN_OUTPUT_DIR.

Standard library only: no third-party imports, no network, no
writes outside the output directory. The copy is byte-identical on
every run, and the program never removes or rewrites the output
directory itself.
"""

import os
import sys

SOURCE_NAME = "entry.png"
MAX_BYTES = 1048576


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, SOURCE_NAME)
    with open(src, "rb") as f:
        data = f.read()
    if not data:
        print("entry.png is empty", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print("entry.png exceeds 1 MiB", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, SOURCE_NAME)
    with open(dst, "wb") as f:
        f.write(data)
    # Read the output back: the grader runs the program twice and the
    # two runs must produce identical bytes, so confirm the copy here
    # instead of trusting the write.
    with open(dst, "rb") as f:
        written = f.read()
    if written != data:
        print("output does not match entry.png", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes)" % (dst, len(data)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
