#!/usr/bin/env python3
"""news-image-20261119 entry: copy the front-page image to /output/entry.png.

Deterministic: a pure byte copy of entry.png (held in this repository), so
two runs write identical bytes. No network, stdlib only. The output directory
is MAKEFUN_OUTPUT_DIR (default /output)."""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")


if __name__ == "__main__":
    sys.exit(main())
