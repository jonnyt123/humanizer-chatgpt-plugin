# Humanizer Plugin v3.8.0

A skills-only ChatGPT/Codex plugin for humanizing prose and lyrics without flattening the writer's voice.

## What it does

- Rewrites AI-sounding prose while preserving supported facts, meaning, and voice.
- Builds a reusable voice fingerprint from writing samples.
- Scores lyric lines for AI-writing artifacts.
- Scores rap technique separately for multisyllabic rhyme, pocket, cadence, and rhyme density.
- Freezes strong lines and repairs weak bars with a three-candidate tournament.
- Optimizes full verses in context instead of treating each bar independently.
- Optimizes verse-to-hook setup and transitions.
- Uses supplied BPM and time signature for beat-grid-aware pocket analysis.
- Suggests context-aware bar-by-bar flow patterns.

## Plugin structure

```text
plugin.json
skills/
  humanizer/
    SKILL.md
    references/
      artifact-scoring.md
      beat-aware-pocket.md
      flow-pattern-generator.md
      lyrics.md
      rap-scoring.md
      rap-technique.md
      score-guided-rewrite.md
      song-section-optimizer.md
      verse-optimizer.md
      voice-fingerprint.md
.claude-plugin/
  plugin.json
LICENSE
NOTICE.md
submission/
  LISTING.md
  TEST_CASES.md
scripts/
  validate-plugin.py
```

`plugin.json` is the portable Agent Plugins manifest. The plugin is skills-only and does not need an MCP server, authentication, or external account connection.

## Public submission

Open the OpenAI plugin submission portal, choose **Create plugin → Skills only**, upload the final skill/plugin bundle, complete the public listing, add the included test cases, and submit it for review.

Public submission also requires a verified developer or business identity and Apps Management write permission in the OpenAI Platform organization used for submission.

## Private/workspace distribution

OpenAI also supports workspace/plugin import from GitHub. This package includes a Claude-compatible manifest for that compatibility path.

## Validation

Run:

```bash
python3 scripts/validate-plugin.py
```
