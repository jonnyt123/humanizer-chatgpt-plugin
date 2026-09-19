# Lyric humanization mode

Use this reference whenever the user asks to humanize, rewrite, finish, critique, or generate song lyrics while avoiding AI-sounding writing.

## Goal

Make the lyric sound written by a specific person with a specific reason for saying each line. Preserve the user's facts, point of view, emotional posture, profanity, slang, rough grammar, and intentional awkwardness. Do not polish away personality.

Speech cadence comes before rhyme. Meaning comes before symmetry. A line that sounds natural but rhymes imperfectly is usually stronger than a perfect rhyme that sounds manufactured.

## Strong lyric-specific AI tells

Flag these aggressively when they are not clearly part of the supplied voice sample:

1. **Generic emotional abstractions.** Lines built from broad words such as pain, demons, scars, darkness, light, healing, broken, chaos, poison, memories, forever, destiny, or soul without a concrete event or behavior attached.
2. **Stock image systems.** Storms, rain, fire and ashes, roads and journeys, mirrors, ghosts, cages, drowning, war inside the mind, cold hearts, shattered pieces, stars, or rising from the ashes used as ready-made emotional shorthand.
3. **Slogan bars.** Lines that could be motivational captions, moral lessons, universal truths, or merch slogans instead of something this narrator would actually say.
4. **Explanation bars.** A line explains the meaning of the previous line instead of adding a new detail, consequence, image, or action.
5. **Therapy-language substitution.** Clinical or self-help language replaces lived detail: trauma, healing, closure, toxic, triggers, boundaries, inner demons, self-worth, and similar terms when the writer did not naturally use them.
6. **Mechanical stanza symmetry.** Every verse has the same line count, sentence shape, stress pattern, or escalation whether the content needs it or not.
7. **Perfect-rhyme pressure.** Exact end rhyme on every line, obvious AABB/AAAA patterns, predictable setup-punchline rhyme pairs, or word choice bent mainly to land the rhyme.
8. **Parallelism by default.** Several lines repeat the same grammar with one noun swapped out: "I did X / I did Y / I did Z" or "You were X / You were Y / You were Z" without a deliberate rhetorical reason.
9. **Generic scene-setting.** "Late nights," "city lights," "empty room," "cold streets," "smoke in the air," "3 A.M.," or similar atmosphere appears without an unusual physical detail that belongs to the scene.
10. **Over-neat narrative transitions.** Lines such as "then I realized," "that's when I knew," "now I understand," or "looking back" explain the arc instead of letting the details imply it.
11. **Lesson at the end.** The verse or bridge resolves into growth, strength, survival, forgiveness, or a moral simply because songs are expected to conclude cleanly.
12. **Decorative ad-libs.** "Yeah," "woah," "oh-oh," crowd calls, or vocal tags are inserted to make the page look like a song rather than because the cadence needs them.
13. **Rhyme-dictionary diction.** A word is noticeably more formal, archaic, poetic, or abstract than the speaker's surrounding vocabulary just to satisfy sound.
14. **Fake specificity.** Invented dates, brands, streets, amounts, messages, objects, injuries, crimes, relationships, or memories are added to make the lyric seem personal. Never do this unless the task is explicitly fictional.

These are editing signals, not permanent bans. If the user's own sample repeatedly uses one of them naturally, treat that as voice evidence and preserve it.

## What to replace them with

Prefer details that reveal the emotion indirectly:

- a thing the narrator did, avoided, counted, hid, broke, bought, kept, deleted, drove past, or left untouched;
- an exact object, place, time, amount, message, sound, smell, bodily reaction, or small habit supplied by the user;
- a contradiction the narrator does not resolve;
- subtext: let the listener infer the feeling from what happened;
- imperfect speech, contractions, fragments, interruptions, and self-corrections that fit the sample;
- internal rhyme, consonance, vowel echoes, and near rhyme when they occur naturally;
- uneven line lengths when the thought needs more or less space.

Do not manufacture "tiny lived details". Specificity must come from the user's source material, supplied notes, an explicitly fictional brief, or details already established in the conversation.

## Rhyme and cadence

When rhyme is requested:

1. Identify the natural spoken stress of the line first.
2. Preserve the strongest content words.
3. Look for internal rhyme or slant rhyme before changing the line-ending fact.
4. Avoid forcing every line to rhyme.
5. Let rhyme density rise and fall across a verse.
6. Keep repeated rhyme schemes only when the user or sample clearly prefers them.
7. Never add a semantically weaker line just to complete a rhyme pair.

For rap, prioritize pocket, stress placement, internal multisyllabic rhyme, consonance, and conversational syntax over perfect end rhyme. For sung lyrics, prioritize vowel shape, singable phrase length, and emotional phrasing over page-perfect meter.

## Structure

Preserve section labels, hook placement, rhyme scheme, syllable target, or line count only when the user asks to preserve them. Otherwise the structure may change to remove repetition or artificial symmetry.

Do not automatically add a pre-chorus, bridge, final chorus variation, intro monologue, spoken outro, or ad-lib section. Use only the sections the song needs.

## Voice protection

Never sanitize profanity, slang, dialect, grammatical roughness, taboo subject matter, or emotionally uncomfortable details merely to make the writing "cleaner." Keep them when they are part of the user's voice and task.

If a line is unusually specific, memorable, or clearly authored by the user, prefer preserving it and rewrite around it unless the user specifically asks to replace it.

## Final lyric check

Before returning lyrics, check:

- Could five unrelated songs plausibly contain this line unchanged? If yes, make it more specific or cut it.
- Did a rhyme choice weaken the meaning? Restore the meaning.
- Did the rewrite explain an emotion the original implied? Restore the implication.
- Did the rewrite add a moral, recovery arc, or tidy conclusion? Remove it unless requested.
- Did the rewrite introduce personal facts the user never supplied? Remove them.
- Does every section use the same syntactic pattern? Break the pattern unless clearly intentional.
- Are the strongest lines the ones with the most concrete or surprising information? If not, strengthen the weaker lines with source-supported detail.
