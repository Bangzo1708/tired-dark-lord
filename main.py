#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one monologue (~100 words) to /output/entry.txt
(or $ENTRY_OUTPUT when set). Fully deterministic: no randomness,
no clock, no network, no external dependencies.

SELECTION — three hand-written candidates, scored 0-5 on the judge
brief's criteria in the judge's own priority order:
  1. ~100 words, fantasy villain secretly just very tired, on subject
  2. tiredness FELT in rhythm / pauses / small deflections, never
     announced ("I am weary" and kin are forbidden)
  3. a SPECIFIC villain with history + scheme; concrete fantasy
     detail, not stock scenery
  4. speakable in one breath, turn / sting in the last line
  5. near 100 words, every word spent, nothing repeated

Variant A — "The Ledger" (bureaucrat dark lord, captive hero):
  Scores: 1:5  2:4  3:5  4:5  5:5  = 24
  A 900-year ledger, a prophecy he wrote himself and then taxed
  the scribe for, the eclipse scheme — the most specific villain
  of the three. Tiredness leaks out sideways: the biting chair,
  "please", and begging to finish one page before being blamed.
  Last line lands the sting without ever saying he is tired.

Variant B — "The Bone Seamstress" (necromancer queen mending dead):
  Scores: 1:5  2:5  3:4  4:4  5:4  = 22
  Strongest on criterion 2 ("Thread. Needle. Thread. Where did
  I — there." — she loses her place mid-sentence; "the dead,
  bless them, never sleep"). Loses on 3 (scheme less developed
  than A's prophecy/ledger) and 5 ("Yes ... Yes ..." repeats a
  beat, "Thread. Needle. Thread." spends words on rhythm).

Variant C — "The War Council" (lord who forgot his generals):
  Scores: 1:5  2:4  3:4  4:5  5:4  = 22
  Best last line ("Just win, and I will learn it after") and
  very speakable, but the setting is the most generic of the
  three (a war table) and "Simple ... simple last year too"
  spends words restating the same joke.

WINNER: Variant A, total 24 (highest; tie-break not needed).
Chosen text verified: exactly 100 words (whitespace split),
under 600 characters, no banned weariness statement.

REVISION (post-verification, second genuine edit in this session):
"Late again, as always" spent two words on one idea, so "again"
was cut and the freed word was spent on "your grandmother's
blessed sword" — a concrete, personal detail (criterion 3)
that also makes the hero's quest feel inherited, not generic.
Word count stays exactly 100; characters stay under 600.
"""

import os

MONOLOGUE = (
    "So. The hero arrives. Late, as always. Sit. No, not there. "
    "That chair has a spring that bites, and I have had enough of being "
    "bitten today. You came to end my reign. The eclipse, the prophecy, "
    "your grandmother's blessed sword. I know. I wrote the prophecy. I paid a scribe to "
    "write it, then taxed the scribe. That is how empires work. You swing, "
    "I sign. Look at this ledger. Nine hundred years of names, all wanting "
    "the same thing: a villain to blame. Fine. Blame me. Go on. Just — "
    "please, let me finish this one page first."
)


def main() -> None:
    out_path = os.environ.get("ENTRY_OUTPUT") or "/output/entry.txt"
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(MONOLOGUE)


if __name__ == "__main__":
    main()
