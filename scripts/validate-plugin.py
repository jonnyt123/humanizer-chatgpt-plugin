#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ERRORS = []
CATEGORIES = {
    "Productivity", "Creativity", "Developer Tools", "Business & Operations",
    "Data & Analytics", "Communication", "Education & Research", "Security",
    "Finance", "Healthcare", "Travel", "Entertainment", "Other",
}
SEMVER = re.compile(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
HEX = re.compile(r"#[0-9A-Fa-f]{6}$")
PACKAGE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}$")


def fail(message):
    ERRORS.append(message)


def read_json(path, label):
    if not path.is_file():
        fail(f"missing {label}: {path.relative_to(ROOT)}")
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"{label} invalid JSON: {exc}")
        return {}


def is_https(value):
    try:
        p = urlparse(value)
        return p.scheme == "https" and bool(p.netloc) and not p.username and not p.password
    except Exception:
        return False


m = read_json(ROOT / "plugin.json", "root plugin manifest")
version = str(m.get("version", ""))
if m.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
    fail("unexpected or missing Agent Plugins 1.0.0 schema")
if m.get("name") != "humanizer" or not PACKAGE.fullmatch(str(m.get("name", ""))):
    fail("plugin name must be humanizer and satisfy directory package-name rules")
if not SEMVER.fullmatch(version):
    fail("version must be semantic versioning")
if not str(m.get("description", "")).strip() or len(str(m.get("description", ""))) > 1024:
    fail("description is required and must be <=1024 characters")

author = m.get("author")
if not isinstance(author, dict) or not str(author.get("name", "")).strip():
    fail("author.name is required")
elif len(author["name"]) > 120:
    fail("author.name must be <=120 characters")
if isinstance(author, dict) and author.get("url") and not is_https(author["url"]):
    fail("author.url must be HTTPS")
for field in ("homepage", "repository"):
    if m.get(field) and not is_https(m[field]):
        fail(f"{field} must be HTTPS")

ui = (((m.get("extensions") or {}).get("com.openai") or {}).get("interface") or {})
for field in ("displayName", "shortDescription", "longDescription", "developerName"):
    if not str(ui.get(field, "")).strip():
        fail(f"missing interface.{field}")
if len(str(ui.get("displayName", ""))) > 30:
    fail("interface.displayName exceeds final 30-character directory limit")
short = str(ui.get("shortDescription", ""))
if len(short) > 30 or "\n" in short or "\r" in short:
    fail("interface.shortDescription must be one line and <=30 characters")
if len(str(ui.get("longDescription", ""))) > 4000:
    fail("interface.longDescription must be <=4000 characters")
if len(str(ui.get("developerName", ""))) > 80:
    fail("interface.developerName must be <=80 characters")
if isinstance(author, dict) and ui.get("developerName") != author.get("name"):
    fail("interface.developerName should match author.name before portal normalization")
if ui.get("category") not in CATEGORIES:
    fail("interface.category is unsupported")

caps = ui.get("capabilities")
if not isinstance(caps, list) or not caps or len(caps) > 20:
    fail("interface.capabilities must contain 1-20 entries")
else:
    for i, item in enumerate(caps, 1):
        if not isinstance(item, str) or not item.strip() or len(item) > 120 or "\n" in item:
            fail(f"capability {i} must be a non-empty one-line string <=120 characters")

for field in ("websiteURL", "privacyPolicyURL", "termsOfServiceURL", "supportURL"):
    value = ui.get(field)
    if not isinstance(value, str) or not value or not is_https(value) or len(value) > 1024:
        fail(f"interface.{field} must be an HTTPS URL <=1024 characters")
for field in ("brandColor", "brandColorDark"):
    if ui.get(field) and not HEX.fullmatch(ui[field]):
        fail(f"interface.{field} must be a six-digit hex color")

prompts = ui.get("defaultPrompt")
if isinstance(prompts, str):
    prompts = [prompts]
if not isinstance(prompts, list) or not prompts or len(prompts) > 3:
    fail("interface.defaultPrompt must contain 1-3 prompts")
else:
    normalized = []
    for i, prompt in enumerate(prompts, 1):
        if not isinstance(prompt, str) or not prompt.strip() or len(prompt) > 128 or "\n" in prompt or "\r" in prompt:
            fail(f"starter prompt {i} must be one line and <=128 characters")
        normalized.append(" ".join(str(prompt).lower().split()))
    if len(normalized) != len(set(normalized)):
        fail("starter prompts must be unique")

if "screenshots" in ui:
    fail("interface.screenshots must be omitted for a skills-only directory bundle")
for forbidden in ("mcp.json", ".mcp.json", ".app.json"):
    if (ROOT / forbidden).exists():
        fail(f"skills-only repository must not contain root {forbidden}")

for field in ("logo", "composerIcon"):
    value = ui.get(field)
    if not isinstance(value, str) or not value.startswith("./") or ".." in Path(value).parts:
        fail(f"interface.{field} must be a safe plugin-relative path beginning ./")
        continue
    asset = ROOT / value[2:]
    if not asset.is_file():
        fail(f"interface.{field} asset missing")
        continue
    if asset.stat().st_size > 5 * 1024 * 1024:
        fail(f"interface.{field} asset exceeds 5 MiB")
    if asset.suffix.lower() == ".svg":
        try:
            svg = ET.parse(asset).getroot()
            vb = svg.attrib.get("viewBox", "").replace(",", " ").split()
            if len(vb) == 4:
                width, height = float(vb[2]), float(vb[3])
            else:
                width, height = float(svg.attrib["width"]), float(svg.attrib["height"])
            if not svg.tag.endswith("svg") or width != height or width < 48:
                fail(f"interface.{field} SVG must be square and at least 48x48")
        except Exception as exc:
            fail(f"interface.{field} SVG invalid: {exc}")

skill = ROOT / "skills" / "humanizer" / "SKILL.md"
if not skill.is_file():
    fail("missing skills/humanizer/SKILL.md")
else:
    text = skill.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail("SKILL.md missing YAML frontmatter")
    if not re.search(r"(?m)^name:\s*humanizer\s*$", text):
        fail("SKILL.md frontmatter name must be humanizer")
    sm = re.search(r'(?m)^\s*version:\s*["\']?([^"\'\s]+)', text)
    if not sm or sm.group(1) != version:
        fail("SKILL.md metadata.version must match plugin.json version")
    for ref in sorted(set(re.findall(r"`references/([^`]+\.md)`", text))):
        if not (skill.parent / "references" / ref).is_file():
            fail(f"missing referenced file: references/{ref}")

compat = read_json(ROOT / ".claude-plugin" / "plugin.json", "Claude compatibility manifest")
if compat and (compat.get("name") != "humanizer" or compat.get("version") != version or not compat.get("skills")):
    fail("Claude compatibility manifest name/version/skills mismatch")

market = read_json(ROOT / ".agents" / "plugins" / "marketplace.json", "workspace marketplace manifest")
entries = market.get("plugins") if isinstance(market, dict) else None
if not isinstance(entries, list) or len(entries) != 1:
    fail("workspace marketplace must contain exactly one Humanizer entry")
else:
    entry = entries[0]
    source = entry.get("source", {}) if isinstance(entry, dict) else {}
    if entry.get("name") != "humanizer" or source.get("source") != "local" or source.get("path") not in (".", "./"):
        fail("workspace marketplace entry must point to repository root")

for rel in (
    "LICENSE", "NOTICE.md", "README.md", "PRIVACY.md", "TERMS.md", "SUPPORT.md", "SECURITY.md",
    "submission/LISTING.md", "submission/TEST_CASES.md", "submission/SUBMISSION_CHECKLIST.md",
):
    if not (ROOT / rel).is_file():
        fail(f"missing {rel}")

tests = ROOT / "submission" / "TEST_CASES.md"
if tests.is_file():
    body = tests.read_text(encoding="utf-8")
    pos = re.search(r"## Positive tests(.*?)(?:## Negative tests|\Z)", body, re.S)
    neg = re.search(r"## Negative tests(.*)\Z", body, re.S)
    pc = len(re.findall(r"(?m)^###\s+\d+\.", pos.group(1) if pos else ""))
    nc = len(re.findall(r"(?m)^###\s+\d+\.", neg.group(1) if neg else ""))
    if (pc, nc) != (5, 3):
        fail(f"submission suite must contain exactly 5 positive and 3 negative tests (found {pc}+{nc})")

if ERRORS:
    print("Humanizer plugin validation: FAIL")
    for error in ERRORS:
        print(f"- {error}")
    sys.exit(1)

print("Humanizer plugin validation: PASS")
print(f"Plugin: humanizer {version}")
print("Mode: skills-only")
print("Skill: skills/humanizer/SKILL.md")
print("Directory metadata: final-limit checked")
print("Brand assets: checked")
print("Review tests: 5 positive + 3 negative")
print("MCP server: none")
