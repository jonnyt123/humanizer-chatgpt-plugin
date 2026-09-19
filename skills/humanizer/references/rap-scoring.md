# Rap technique scoring

Use this reference when the user asks to score, grade, compare, or diagnose rap technique. Read `references/rap-technique.md` first so the scores follow the same definitions.

The scores describe **how strongly and effectively a technique appears in the text**. They are not an overall quality score. A sparse narrative bar can be excellent with a low multis score or low rhyme-density score. Do not reward density for its own sake.

When no beat, BPM, audio, or performance is supplied, pocket and cadence scores are **text-only estimates** based on natural speech stress, phrase shape, breath, and likely rhythmic placement. Say so once in the report. Do not claim exact beat alignment.

## Four scores: 0 to 5

### 1. Multisyllabic rhyme: 0–5

Score the quality and integration of multisyllabic rhyme families, not just how many matching syllables appear.

- **0 — none:** no meaningful multisyllabic rhyme. This is not automatically a weakness.
- **1 — incidental:** one loose or accidental multi, with little structural role.
- **2 — basic:** at least one clear two-or-more-syllable match, but mostly isolated or end-rhyme dependent.
- **3 — developed:** recurring multi families, some internal placement, and mostly natural diction.
- **4 — strong:** sustained or evolving multi chains with internal placement, slant variation, and little rhyme-forcing.
- **5 — exceptional:** complex phonetic chains recur across positions and bars while syntax, meaning, and voice stay natural. The chain evolves instead of repeating one exact sound mechanically.

Lower the score when the rhyme requires unnatural word order, obvious rhyme-dictionary diction, filler, or semantic weakening. Verify by sound, not spelling.

### 2. Pocket: 0–5

Score how naturally the line or passage suggests a stable, performable stress pattern.

- **0 — unclear:** prose-like or rhythmically unstable; no convincing recurring stress shape is apparent.
- **1 — weak:** a few workable stresses, but connector words, bar length, or phrasing make the line hard to place consistently.
- **2 — workable:** a basic rhythmic shape is present, though some phrases feel crowded, underfilled, or dependent on awkward pronunciation.
- **3 — solid:** natural stresses form a repeatable pocket and most lines sound speakable without obvious cramming.
- **4 — strong:** the passage establishes clear anchors, uses pickups/rests/space well, and varies subdivisions without losing the pocket.
- **5 — exceptional:** stress placement feels highly controlled and performable, with deliberate space, syncopation, or displacement that still preserves a clear rhythmic center.

With text only, score **pocket potential**, not actual beat fit. If audio or a beat grid is available, score the performed/observed alignment instead.

### 3. Cadence: 0–5

Score the control of phrase shape across multiple bars: stress, pause, speed, vowel length, endings, breath, and variation.

- **0 — flat/unclear:** no coherent phrase shape or the passage reads as prose broken into lines.
- **1 — repetitive:** one cadence repeats mechanically with little expressive reason.
- **2 — basic:** a recognizable cadence exists, but endings, pauses, or bar boundaries are predictable.
- **3 — controlled:** cadence is consistent enough to establish a motif and varies in useful places.
- **4 — dynamic:** the passage controls acceleration, pauses, enjambment, breath, and line endings without sounding random.
- **5 — exceptional:** cadence changes reinforce meaning or emphasis while remaining musically legible; repetition and variation feel deliberate across the section.

Cadence is inherently multi-line. For a single isolated line, return `N/A` or a provisional score and explain that the surrounding bars are needed for a reliable rating.

### 4. Rhyme density: 0–5

Score **effective density**, not raw rhyme count. Also label the observed amount as `sparse`, `light`, `medium`, `dense`, or `very dense`.

- **0 — none:** no meaningful recurring rhyme material.
- **1 — sparse:** occasional rhyme with little structural role.
- **2 — light:** intentional rhyme is present, but most recurrence is at line endings or in short isolated pockets.
- **3 — balanced:** internal and/or end rhyme recur often enough to shape the verse without crowding meaning.
- **4 — dense and controlled:** multiple rhyme positions or chains operate at once while diction stays natural and semantic movement remains clear.
- **5 — very dense and effortless:** high phonetic recurrence, varied placement, and sustained chains coexist with clear meaning, natural syntax, and enough space for performance.

A deliberately sparse section can still be strong writing. Do not lower an overall judgment merely because density is low. If density is high but meaning stalls, tag `RHYME_OVER_CONTENT` and reduce this score.

## Diagnostic tags

Use only tags that explain a meaningful weakness:

- `MULTI_FORCED` — multi exists but bends syntax or diction.
- `MULTI_THIN` — claimed multi is mostly spelling similarity or a weak one-syllable echo.
- `END_RHYME_DEPENDENT` — most rhyme weight sits on final words.
- `CHAIN_BREAK` — an established sound family drops for no clear musical or semantic reason.
- `POCKET_CRAMMED` — too many low-value syllables are packed between likely stress anchors.
- `POCKET_LOOSE` — stress placement changes without a clear recurring anchor.
- `STRESS_COLLISION` — natural speech stress fights the likely rhythmic emphasis.
- `CADENCE_FLAT` — the same phrase ending or stress shape repeats mechanically.
- `CADENCE_RANDOM` — cadence changes before a recognizable motif is established.
- `BREATH_HEAVY` — likely performance phrasing gives too little room to breathe.
- `DENSITY_THIN` — rhyme presence is too weak for a section intended to be technically dense.
- `DENSITY_OVERLOAD` — recurrence is so packed that clarity or performance space suffers.
- `RHYME_OVER_CONTENT` — rhyme pressure reduces semantic movement.

## Line-level vs section-level scoring

Some techniques cannot be judged equally well on one line.

### Line level

For each substantive bar, you may score:
- multisyllabic rhyme;
- pocket potential;
- local rhyme density.

Cadence should usually be scored across 2–8 bars. If the user explicitly requests a cadence score on every line, treat each line as a **cadence contribution** score rather than pretending a single line contains a complete cadence pattern.

### Section level

For each verse/hook/block, score all four dimensions. Section scores should consider whether the technique develops across bars, not simply average the line scores.

## Default visible report

For a short verse, use:

| Line | Multis | Pocket | Cadence* | Density | Notes |
|---|---:|---:|---:|---:|---|
| 1 | 3/5 | 4/5 | 3/5 | 3/5 | Internal slant multi; natural stress anchors; medium density. |

`*Cadence` at line level means contribution to the section's cadence unless enough surrounding context makes a direct local judgment useful.

Then add a section summary:

- **Multis:** 3/5 — brief reason.
- **Pocket:** 4/5 — brief reason.
- **Cadence:** 3/5 — brief reason.
- **Rhyme density:** 4/5 (`dense`) — brief reason.
- **Main constraint:** one or two tags that explain the biggest technical limitation.

For long songs, score by 4-bar or 8-bar block unless the user explicitly asks for every line.

## Rewrite behavior after scoring

Do not mechanically raise every number toward 5.

1. Preserve techniques that already fit the voice.
2. Fix the lowest score only when it is actually limiting the requested style.
3. Improve multis by finding sound-compatible language that already belongs in the thought.
4. Improve pocket by removing filler, shifting phrase boundaries, or changing stress placement before changing the story.
5. Improve cadence by establishing a motif before adding variation.
6. Improve density by adding internal/slant rhyme where natural, not by stacking end rhymes.
7. Re-score internally after the rewrite.

A technically successful rewrite can intentionally keep a 1 or 2 in one dimension when the section needs space, directness, or narrative clarity.
