#!/usr/bin/env python3
"""news-image-20261122 entry point (v3).

Stdlib only. Copies the pre-built entry.png — rendered on the build
machine with Pillow + scene_lib, neither of which exists (or is
needed) in the grader — into $MAKEFUN_OUTPUT_DIR/entry.png, byte
for byte.

The grader runs this program twice in a fresh container with no
network, the repository read-only, 1 CPU, 512 MB and 60 seconds;
both runs must write identical bytes. This module does no image work
at all: it reads one file, checks the 1 MiB limit, writes one file,
and reads the output back to confirm the copy.
"""
import os
import sys

MAX_BYTES = 1048576


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    with open(src, "rb") as f:
        data = f.read()
    if not data:
        print("entry.png is empty", file=sys.stderr)
        return 1
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        print("entry.png is not a PNG file", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print("entry.png exceeds 1 MiB", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(dst, "wb") as f:
        f.write(data)
    with open(dst, "rb") as f:
        written = f.read()
    if written != data:
        print("output does not match entry.png", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes)" % (dst, len(data)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
