# The five-question audit

Use this when the author wants to check a finished or nearly finished piece. The goal is to find out whether the piece has been thought through, and where the author is missing.

## Contents
- The five questions
- Report format
- Reading the answers
- Rules

## The five questions

### 1. What is the core claim?
Many pieces carry a lot of information, but the reader remembers one idea. Can you state it in one sentence from the text alone?
- **Clear:** one sentence, and every section serves it.
- **Partial:** two or three candidate claims compete, or the claim is stated only as a topic ("this is about X").
- **Missing:** you can only say what the piece is about, not what it argues.
- **Ask the author:** "If a reader remembers one sentence, which one should it be?"

### 2. Why does this matter to this reader?
Is there a visible link between the piece and the reader's situation, problem or desire? Without it the piece is the author talking to themselves.
- **Clear:** the opening shows a situation the reader recognizes, and the piece returns to it.
- **Partial:** the reader is named ("for beginners") but their problem isn't shown.
- **Missing:** the piece could be read by anyone and be about no one.
- **Ask the author:** "What was your reader doing last week that made this matter to them?"

### 3. What emotional need does it meet?
Different pieces make readers feel understood, reminded, encouraged, or more certain. Identify which one this is, and whether the text delivers it or only intends to.
- **Clear:** you can name the need and point to the passage that meets it.
- **Partial:** the intended feeling is announced ("don't worry!") but not earned by anything specific.
- **Missing:** informative but emotionally flat; nothing is at stake for the reader.
- **Ask the author:** "What should the reader feel by the last paragraph, and which sentence makes them feel it?"

### 4. What does the reader learn about the author?
After reading, does the reader know what this person is good at, what they believe, and who they help? If readers remember only the lesson and not the person, the piece builds little trust.
- **Clear:** a stance, a real experience and a voice are all present.
- **Partial:** a few first-person lines, but no experience that only this author could have had.
- **Missing:** no discernible author.
- **Ask the author:** "What do you know about this that someone who only read about it wouldn't?"

### 5. What does it change for the reader?
Pick one: they understand a problem better, they have something to do, or they have corrected a belief. The **change test**: finish the sentence "After reading, the reader can/now believes/no longer ___."
- **Clear:** the sentence completes easily and specifically.
- **Partial:** it completes only vaguely ("thinks more about AI").
- **Missing:** it can't be completed; the piece seems fine but lands nowhere.
- **Ask the author:** "What is the one thing the reader will do or think differently tomorrow?"

If the author cannot answer these themselves, the piece usually isn't thought through yet. Typical causes: too many ideas and no focus, fluent language with a weak link to the reader, correct statements with nothing memorable.

## Report format

```markdown
# Audit: <title or first line>

## Five questions
| # | Question | Verdict | Evidence (quote) | What I need from you |
|---|---|---|---|---|
| 1 | Core claim | clear / partial / missing | "…" | question |
| 2 | Why it matters to the reader | | | |
| 3 | Emotional need | | | |
| 4 | What the reader learns about you | | | |
| 5 | What it changes | | | |

## Author-absence hotspots
- Paragraph N ("opening words…"): correct but generic. Question to ask: …
- …

## Signals (optional, from scripts/absence_signals.py)
<paste the report; remind that these are hints, not a verdict>

## Start with these three
1. …
2. …
3. …
```

## Reading the answers
- Two or more "missing" among questions 1, 2 and 5 means the structure needs rethinking, not line editing.
- A "missing" on question 4 alone is the classic AI-flavor case: sound structure, no person. The fix is a real experience and a stance, supplied by the author.
- Strong on all five but flat to read: check rhythm and specifics with `references/author-absence.md`.

## Rules
- Quote the text as evidence. Don't give verdicts you can't point to.
- Ask the author a question for every gap; do not fill the gap yourself.
- Don't comment on whether AI wrote the text. If asked, say you can't tell and that it doesn't change the advice.
- Keep the report short enough to act on: three priorities at the end.
