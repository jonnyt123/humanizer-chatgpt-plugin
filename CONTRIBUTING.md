# Contributing

## Development workflow

1. Create a branch from `main`.
2. Keep behavioral changes inside `skills/humanizer/` unless the plugin manifest or submission metadata also needs an update.
3. Update `plugin.json` and `CHANGELOG.md` when releasing a new version.
4. Run `python3 scripts/validate-plugin.py` before opening a pull request.
5. Keep claims, scoring rules, and rewrite behavior deterministic enough to test with examples in `submission/TEST_CASES.md`.

## Versioning

Humanizer uses semantic versioning:

- PATCH: wording fixes or non-breaking rule refinements.
- MINOR: new scoring, rewrite, lyric, flow, or analysis capabilities.
- MAJOR: incompatible plugin structure or behavior changes.
