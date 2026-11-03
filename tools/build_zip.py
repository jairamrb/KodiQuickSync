#!/usr/bin/env python3
"""Package the add-on as dist/script.program.quicksync-<version>.zip, ready to install in Kodi."""

import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ADDON_ID = "script.program.quicksync"
ADDON_DIR = ROOT / ADDON_ID
DIST = ROOT / "dist"


def addon_version():
    addon_xml = (ADDON_DIR / "addon.xml").read_text(encoding="utf-8")
    return re.search(r'<addon [^>]*version="([^"]+)"', addon_xml).group(1)


def main():
    DIST.mkdir(exist_ok=True)
    target = DIST / ("%s-%s.zip" % (ADDON_ID, addon_version()))

    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(ADDON_DIR.rglob("*")):
            if path.is_file() and "__pycache__" not in path.parts:
                zf.write(path, path.relative_to(ROOT).as_posix())

    print(target)


if __name__ == "__main__":
    main()
