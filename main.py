#!/usr/bin/env python3
"""main.py — news-image-20261122 entrypoint (v5).

The entry image is pre-rendered on the build machine by build_v5.py
(code-drawn flat 2D vector, 1024x1024 PNG, well under 1 MiB) and
shipped in this repo as entry.png. This program does no image work:
it only validates the shipped file and copies it byte-for-byte into
the grader's output directory, so it runs in the grader's stdlib-only
container with no network and no third-party packages.

Runtime contract (RULES.txt): Python 3.13, standard library only,
writes $MAKEFUN_OUTPUT_DIR/entry.png, output <= 1 MiB and
<= 1024x1024, and both grader runs must write identical bytes. A
plain byte copy makes the two runs identical by construction. The
program never deletes, moves, or rewrites the output directory
itself, and it never touches anything outside the output directory
except reading entry.png.
"""
import os
import sys

MAX_BYTES = 1048576
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def fail(message):
    print("main.py: " + message, file=sys.stderr)
    return 1


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        return fail("MAKEFUN_OUTPUT_DIR is not set")
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    try:
        with open(src, "rb") as f:
            data = f.read()
    except OSError as exc:
        return fail("cannot read entry.png: %s" % exc)
    if not data:
        return fail("entry.png is empty")
    if data[:8] != PNG_MAGIC:
        return fail("entry.png is not a PNG file")
    if len(data) < 24 or data[12:16] != b"IHDR":
        return fail("entry.png has no valid PNG IHDR chunk")
    # PNG IHDR: width and height are big-endian uint32 at bytes 16-24.
    # Verifies the <= 1024x1024 output limit inside the grader, using
    # only the standard library (no Pillow in the grader image).
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    if width > 1024 or height > 1024:
        return fail("entry.png is %dx%d, over the 1024x1024 limit"
                    % (width, height))
    if len(data) > MAX_BYTES:
        return fail("entry.png exceeds 1 MiB (%d bytes)" % len(data))
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(dst, "wb") as f:
        f.write(data)
    with open(dst, "rb") as f:
        written = f.read()
    if written != data:
        return fail("output bytes do not match entry.png")
    print("wrote %s (%d bytes)" % (dst, len(data)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
