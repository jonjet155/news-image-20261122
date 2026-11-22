#!/usr/bin/env python3
"""Entrypoint for the news-image-20261122 entry (v6).

The page image is rendered ahead of time on the build machine
(build_v6.py: code-drawn flat 2D vector, 1024x1024 PNG, ~227 KiB) and
stored in this repository as entry.png. This script does no drawing
and needs no third-party package: it only checks the shipped PNG and
copies it unchanged to the directory named by MAKEFUN_OUTPUT_DIR.

Grader contract (RULES.txt): Python 3.13, standard library only, no
network, output entry.png at most 1 MiB and at most 1024x1024 pixels,
and two runs must produce identical bytes. A straight byte copy meets
all of that by construction. The script only reads entry.png next to
itself and only writes one file inside the output directory; it never
removes, renames, or recreates that directory.
"""
import os
import sys

SIZE_LIMIT = 1048576          # 1 MiB
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
CHUNK_IHDR = b"IHDR"


def die(reason):
    """Report a problem on stderr and return a failing exit code."""
    sys.stderr.write("main.py: " + reason + "\n")
    return 1


def read_shipped_png():
    """Load entry.png from beside this file, or return None + reason."""
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "entry.png")
    try:
        with open(path, "rb") as handle:
            return handle.read(), None
    except OSError as exc:
        return None, "cannot read entry.png: %s" % exc


def check_png(data):
    """Validate size, signature, and pixel dimensions (stdlib only)."""
    if not data:
        return "entry.png is empty"
    if len(data) > SIZE_LIMIT:
        return "entry.png is %d bytes, over the 1 MiB limit" % len(data)
    if data[:8] != PNG_SIGNATURE:
        return "entry.png is not a PNG file"
    if len(data) < 24 or data[12:16] != CHUNK_IHDR:
        return "entry.png has no valid PNG header"
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    if width == 0 or height == 0:
        return "entry.png has zero width or height"
    if width > 1024 or height > 1024:
        return "entry.png is %dx%d, over the 1024x1024 limit" % (
            width, height)
    return None


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        return die("MAKEFUN_OUTPUT_DIR is not set")
    data, problem = read_shipped_png()
    if problem is not None:
        return die(problem)
    problem = check_png(data)
    if problem is not None:
        return die(problem)
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    with open(target, "wb") as handle:
        handle.write(data)
    with open(target, "rb") as handle:
        if handle.read() != data:
            return die("output bytes do not match entry.png")
    print("wrote %s (%d bytes)" % (target, len(data)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
