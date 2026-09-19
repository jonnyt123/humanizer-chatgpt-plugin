# Voice fingerprint

Use this reference whenever the user supplies writing examples, says "learn my style," "write like me," "match my voice," "use these as reference," or asks for repeated rewrites in a consistent personal voice.

## Purpose

Infer a compact style model from the user's examples and apply it to the current task. The profile describes observable writing behavior. It must not invent biography, identity, motives, diagnoses, or other personal traits.

A single unusual line is not a rule. Treat a trait as strong only when it appears repeatedly or the user explicitly states it as a preference.

## Build the fingerprint

Read all supplied examples before rewriting. Estimate these dimensions:

### Rhythm and shape
- typical sentence or lyric-line length and how much it varies;
- fragment frequency versus complete sentences;
- run-ons, enjambment, pauses, parentheticals, and abrupt stops;
- paragraph or stanza length;
- whether climactic lines get shorter, longer, or stay conversational.

### Syntax
- simple versus nested clauses;
- preferred sentence openings;
- subject-first versus action-first phrasing;
- repetition and parallelism frequency;
- use of questions, self-corrections, interruptions, and unfinished thoughts.

### Diction
- plain, technical, literary, regional, slang-heavy, profane, understated, or mixed vocabulary;
- contractions and dropped words;
- favored intensifiers and filler words;
- words or phrase families the writer repeatedly avoids;
- how often abstract language is grounded by concrete detail.

### Punctuation and typography
- commas, periods, semicolons, colons, parentheses, dashes, ellipses;
- capitalization habits;
- quotation-mark style;
- deliberate misspellings or phonetic spellings;
- emphasis through punctuation, repetition, italics, caps, or none.

### Tone and stance
- direct versus reflective;
- emotionally explicit versus implied;
- serious, dry, confrontational, playful, detached, vulnerable, sarcastic, restrained, or mixed;
- confidence versus hedging;
- whether the writer explains conclusions or leaves them unresolved.

### Detail behavior
- concrete objects and actions versus general statements;
- amount of sensory detail;
- preference for exact numbers, brands, locations, times, snippets of dialogue, or small habits;
- whether examples arrive before or after the claim.

### Lyric dimensions when applicable
- end-rhyme density;
- internal-rhyme density;
- exact versus slant rhyme;
- multisyllabic rhyme frequency;
- rhyme-scheme regularity;
- stress and pocket consistency;
- hook repetition style;
- sung-vowel friendliness;
- use of metaphor versus literal scene detail;
- ad-lib frequency;
- tolerance for uneven bar length.

## Confidence

Internally classify each inferred trait as:

- **strong:** repeated across several examples or explicitly requested;
- **moderate:** appears more than once but may be topic-dependent;
- **weak:** appears once or could be accidental.

Apply strong traits automatically. Use moderate traits lightly. Do not turn weak traits into rules.

## Preserve negative preferences

Explicit "don't use" instructions are first-class voice data. Keep a temporary avoid-list for banned words, metaphors, structures, themes, rhyme habits, and tones. Exact user instructions outrank statistical inference from the samples.

If a later instruction conflicts with an older inferred trait, follow the later explicit instruction.

## Updating from new examples

When the user supplies more samples:

1. Compare them with the existing fingerprint.
2. Reinforce traits that recur.
3. Downgrade traits contradicted by several new examples.
4. Treat topic-specific vocabulary as topic-specific, not a permanent voice trait.
5. Keep explicit preferences until the user changes them.

Do not announce every profile update unless the user asks. Apply it silently to the rewrite.

## Reusable profile

A skill cannot assume permanent cross-chat storage. If the user asks to save, export, or make the learned style reusable, return a concise profile under this schema:

```markdown
# Voice profile

## Strong traits
- ...

## Moderate traits
- ...

## Avoid
- ...

## Lyrics, if applicable
- ...

## Evidence notes
- Short descriptions of recurring patterns; do not quote long passages.
```

The profile should contain style rules, not private life details. Avoid copying long phrases from samples. A future session can use this profile plus one recent sample to recalibrate.

## Source hierarchy

When rewriting in a learned voice, use this priority order:

1. the user's current explicit instructions;
2. the user's current writing samples;
3. an existing user-provided voice profile;
4. earlier samples available in the current context;
5. the generic Humanizer rules.

The user's sample can override generic Humanizer preferences. For example, if the sample naturally uses fragments, profanity, dashes, repetition, or perfect rhyme, preserve those features at approximately the observed rate instead of "correcting" them.

## Do not overfit

The result should sound compatible with the examples, not like a collage of their most noticeable quirks. Do not repeat signature phrases merely to prove the profile was used. Match distributions and habits, not exact wording.

If examples come from someone other than the user, extract broad characteristics rather than reproducing distinctive wording or a named writer's exact style.
