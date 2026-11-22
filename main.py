"""Make.fun submission entry bot for news-image-20261122.

Copies the generated summary entry image to the target grader output directory.
Compatible with `python3 -P -s /bot/main.py` execution environment.
"""

import os
import sys
import shutil
from pathlib import Path


def run() -> int:
    # Resolve bot directory and source asset
    bot_dir = Path(__file__).resolve().parent
    src_image = bot_dir / "entry.png"

    # Identify target output location
    output_dir_env = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_dir = Path(output_dir_env)

    # Ensure destination directory exists
    output_dir.mkdir(parents=True, exist_ok=True)
    dest_image = output_dir / "entry.png"

    # Verify input image exists
    if not src_image.is_file():
        print(f"Error: Source image not found at {src_image}", file=sys.stderr)
        return 1

    # Copy entry image to designated grader output
    print("[TheGlobalChronicle] Deploying 36-story high-contrast 15-card illustrated broadsheet for Sunday 22 November 2026")
    shutil.copyfile(src_image, dest_image)
    size_bytes = dest_image.stat().st_size
    print(f"Successfully deployed entry image ({size_bytes} bytes) to {dest_image}")
    return 0


if __name__ == "__main__":
    sys.exit(run())

