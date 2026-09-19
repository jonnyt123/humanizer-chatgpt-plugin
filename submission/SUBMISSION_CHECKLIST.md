# OpenAI directory submission checklist

Humanizer is packaged as a **skills-only** plugin.

## Automated checks in this repository
- [x] Root Agent Plugins `plugin.json`
- [x] Valid semantic version and synchronized manifests
- [x] `author.name` and OpenAI `developerName`
- [x] Directory-length display name and short description
- [x] Supported category and capability list
- [x] At most three one-line starter prompts within final-directory limits
- [x] Square logo and composer icon included in the package
- [x] Public website, privacy, terms, and support URLs
- [x] No MCP or app manifest in the skills-only submission bundle
- [x] At least one valid skill with all referenced files
- [x] Five positive and three negative review test cases
- [x] Reproducible ZIP build with archive boundary/size checks

Run:

```bash
python3 scripts/validate-plugin.py
python3 scripts/build-submission.py
```

The resulting archive is `dist/humanizer-plugin-v3.8.1.zip`.

## Manual publisher requirements
- [ ] Sign in to the OpenAI plugin submission portal.
- [ ] Ensure the publishing OpenAI Platform organization has Apps Management write permission (organization owners already satisfy this).
- [ ] Select the verified individual or business identity that will publish Humanizer.
- [ ] Choose **Create plugin → Skills only**.
- [ ] Upload `dist/humanizer-plugin-v3.8.1.zip`.
- [ ] Confirm the generated listing fields against `submission/LISTING.md`.
- [ ] Add the three starter prompts.
- [ ] Add the five positive and three negative tests from `submission/TEST_CASES.md`.
- [ ] Choose availability countries/regions.
- [ ] Review the automated skill safety/information-security scan and resolve any finding.
- [ ] Submit for OpenAI review.
- [ ] After approval, publish the approved version from the portal when ready.

## Notes
The README screenshots are repository documentation, not submission screenshots. Humanizer is skills-only and has no custom MCP UI.

The included SVG is a production-valid square brand asset. Replace it before submission only if you want different final branding; if replaced, keep both `interface.logo` and `interface.composerIcon` pointing to valid square image assets.
