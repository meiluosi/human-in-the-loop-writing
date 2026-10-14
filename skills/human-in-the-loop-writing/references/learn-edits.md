# Learn my edits

The best way to teach AI an author's standards is to show it what the author actually changed. Prompts written from scratch describe taste in the abstract; edits show it.

## Contents
- What to ask for
- How to analyze the rounds
- Output: the edit summary
- Output: voice-profile.md
- Using the profile later

## What to ask for
Ask the author for as many of these as they have, for the same piece:

1. The AI's **first draft**.
2. Any **AI revision(s)** after feedback.
3. The author's **own final** (or their own heavily edited version).

Two versions are enough to start. Three are better, because the second round shows what the author asked AI to fix and the third shows what AI still couldn't.

## How to analyze the rounds
Compare each version with the one before it. Look for these kinds of change and quote the actual before and after text, not paraphrases:

| Kind of change | What to look for |
|---|---|
| **Empty phrases cut** | Sentences or openers deleted because they said nothing |
| **Specifics added** | Real experience, scenes, numbers, names added |
| **Stances sharpened** | Hedged claims turned into positions; or positions the author rejected |
| **Templated expressions removed** | Stock phrases, tidy triads, symmetric structures replaced |
| **Boundaries added** | "This works when… / not when…" statements added |
| **Structure moved** | Sections reordered, merged or dropped |
| **Voice** | Word choices, sentence length, level of formality that changed |

For each kind, ask: what rule is the author applying? State it as an instruction you could follow next time ("Open with the reader's situation, never with a general statement about the era").

Only claim a rule when you can show at least one real before/after pair for it. If only one example exists, label it as a tentative rule.

## Output: the edit summary

```markdown
# What changed, round by round

## Round 1 (AI draft -> AI revision)
- <kind of change>: "<before>" -> "<after>"

## Round 2 (AI revision -> your final)
- <kind of change>: "<before>" -> "<after>"

## Rules I infer
1. <rule> (evidence: pair #…; confidence: high/tentative)
2. …

## Things I couldn't infer
- <where the sample is too small or the changes seem inconsistent>
```

## Output: voice-profile.md
Draft the profile from the author's edits, using `assets/voice-profile-template.md`. Only include what the edits support; leave a template line blank rather than guessing. Ask the author to confirm or correct each section, then save the file where they keep their projects.

## Using the profile later
At the start of Draft and Audit modes, check the working directory for `voice-profile.md`. If it exists, read it and follow it: the author no longer has to re-explain their standards each time. Update it when the author makes new edits that show a changed preference, and say what you changed.
