#!/usr/bin/env python3
"""main.py — news-image-20261122 entry point (v7).

The entry image is a pre-built PNG held in this repository
(entry.png, 1024x1024, built by build_v7.py from the 22 Nov brief).
This program only copies it to the grader's output directory.

Runtime rules (competition RULES.txt): Python 3.13, standard library
only — nothing is installed before this runs, so this file imports
only os and sys. It never deletes, moves or rewrites the output
directory itself; it only writes $MAKEFUN_OUTPUT_DIR/entry.png.
It runs twice and both runs write the same bytes (a straight copy).
"""
import os
import sys


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    with open(src, "rb") as f:
        data = f.read()
    if len(data) > 1048576:
        print("entry.png exceeds 1 MiB", file=sys.stderr)
        return 1
    # Validate the PNG header: 8-byte signature + IHDR chunk with
    # width/height at most 1024 (competition limit). Pure stdlib,
    # no image library needed.
    if data[:8] != b"\x89PNG\r\n\x1a\n" or len(data) < 24:
        print("entry.png is not a PNG", file=sys.stderr)
        return 1
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    if width > 1024 or height > 1024 or width < 1 or height < 1:
        print("entry.png dimensions out of range:", width, "x", height,
              file=sys.stderr)
        return 1
    with open(dst, "wb") as f:
        f.write(data)
    print("wrote", dst, len(data), "bytes", str(width) + "x" + str(height))
    return 0


if __name__ == "__main__":
    sys.exit(main())
