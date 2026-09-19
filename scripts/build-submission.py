#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
MANIFEST = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
VERSION = MANIFEST["version"]
OUTPUT = DIST / f"humanizer-plugin-v{VERSION}.zip"

INCLUDE_FILES = [
    "plugin.json", "LICENSE", "NOTICE.md", "PRIVACY.md", "TERMS.md", "SUPPORT.md", "SECURITY.md",
]
INCLUDE_DIRS = ["assets", "skills"]


def collect():
    files = []
    for rel in INCLUDE_FILES:
        p = ROOT / rel
        if not p.is_file():
            raise FileNotFoundError(rel)
        files.append((p, PurePosixPath(rel)))
    for rel in INCLUDE_DIRS:
        base = ROOT / rel
        for p in sorted(base.rglob("*")):
            if p.is_file():
                files.append((p, PurePosixPath(p.relative_to(ROOT).as_posix())))
    return files


def validate_archive(path):
    with zipfile.ZipFile(path) as zf:
        names = zf.namelist()
        if len(names) > 5000:
            raise RuntimeError("archive has more than 5000 entries")
        total = sum(i.file_size for i in zf.infolist())
        if total > 512 * 1024 * 1024:
            raise RuntimeError("archive exceeds 512 MiB uncompressed")
        if path.stat().st_size > 100 * 1024 * 1024:
            raise RuntimeError("archive exceeds 100 MB compressed")
        for name in names:
            pp = PurePosixPath(name)
            if pp.is_absolute() or ".." in pp.parts:
                raise RuntimeError(f"unsafe ZIP member: {name}")
        required = {"plugin.json", "skills/humanizer/SKILL.md", "assets/humanizer.svg"}
        missing = required - set(names)
        if missing:
            raise RuntimeError(f"archive missing required members: {sorted(missing)}")
        forbidden = {"mcp.json", ".mcp.json", ".app.json"}
        if forbidden.intersection(names):
            raise RuntimeError("skills-only archive contains MCP/app configuration")
    return len(names), total


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="build and validate, then remove the ZIP")
    args = ap.parse_args()
    subprocess.run([sys.executable, str(ROOT / "scripts/validate-plugin.py")], check=True)
    DIST.mkdir(exist_ok=True)
    if OUTPUT.exists():
        OUTPUT.unlink()
    with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for src, arc in collect():
            info = zipfile.ZipInfo(arc.as_posix(), date_time=(2026, 9, 18, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o100644 & 0xFFFF) << 16
            zf.writestr(info, src.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    entries, total = validate_archive(OUTPUT)
    print(f"Submission package: {OUTPUT}")
    print(f"Entries: {entries}")
    print(f"Compressed bytes: {OUTPUT.stat().st_size}")
    print(f"Uncompressed bytes: {total}")
    if args.check:
        OUTPUT.unlink()
        print("Check mode: archive removed after validation")


if __name__ == "__main__":
    main()
