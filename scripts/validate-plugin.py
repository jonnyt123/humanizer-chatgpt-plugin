#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
errors = []

manifest_path = root / "plugin.json"
if not manifest_path.exists():
    errors.append("missing root plugin.json")
else:
    try:
        m = json.loads(manifest_path.read_text())
        if m.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
            errors.append("unexpected or missing Agent Plugins schema")
        if m.get("name") != "humanizer":
            errors.append("plugin name must be humanizer")
        if not re.fullmatch(r"\d+\.\d+\.\d+", str(m.get("version", ""))):
            errors.append("version must be semver x.y.z")
        if not str(m.get("description", "")).strip():
            errors.append("description is required")
        interface = (((m.get("extensions") or {}).get("com.openai") or {}).get("interface") or {})
        for field in ("displayName", "shortDescription", "longDescription"):
            if not str(interface.get(field, "")).strip():
                errors.append(f"missing interface.{field}")
    except Exception as e:
        errors.append(f"plugin.json invalid JSON: {e}")

skill = root / "skills" / "humanizer" / "SKILL.md"
if not skill.exists():
    errors.append("missing skills/humanizer/SKILL.md")
else:
    text = skill.read_text()
    if not text.startswith("---\n"):
        errors.append("SKILL.md missing YAML frontmatter")
    if not re.search(r"(?m)^name:\s*humanizer\s*$", text):
        errors.append("SKILL.md frontmatter name must be humanizer")
    refs = sorted(set(re.findall(r"`references/([^`]+\.md)`", text)))
    for ref in refs:
        if not (skill.parent / "references" / ref).exists():
            errors.append(f"missing referenced file: references/{ref}")

compat = root / ".claude-plugin" / "plugin.json"
if compat.exists():
    try:
        c = json.loads(compat.read_text())
        if c.get("name") != "humanizer":
            errors.append("compatibility plugin name mismatch")
        if not c.get("skills"):
            errors.append("compatibility manifest has no skills")
    except Exception as e:
        errors.append(f"compatibility manifest invalid JSON: {e}")

for required in ("LICENSE", "NOTICE.md", "README.md", "submission/LISTING.md", "submission/TEST_CASES.md"):
    if not (root / required).exists():
        errors.append(f"missing {required}")

if errors:
    print("Humanizer plugin validation: FAIL")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print("Humanizer plugin validation: PASS")
print("Plugin: humanizer 3.8.0")
print("Mode: skills-only")
print("Skill: skills/humanizer/SKILL.md")
print("MCP server: none")
