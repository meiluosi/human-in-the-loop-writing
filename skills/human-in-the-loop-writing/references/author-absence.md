# Author-absence: what it looks like and how to fix it

"AI flavor" (AI味) is not a style. It is what text looks like when the author's judgment, experience, trade-offs, taste and way of speaking never entered it. The text is complete and correct, and still leaves no impression. AI is best at making things complete and worst at holding a position, so unless the author shows up, the result is smooth, balanced and forgettable.

## Contents
- Patterns to look for
- Fixing: ask, don't smooth
- Using the helper script
- What the script cannot tell you

## Patterns to look for

| Pattern | What it looks like | Why it signals absence |
|---|---|---|
| **Generic opening** | A sweeping line about "this era" or "today's world" before any situation | Nobody in particular is being spoken to |
| **Stock transitions** | 首先…其次…最后; 总而言之; 值得注意的是; "moreover", "in conclusion", "it is important to note" | Structure announced, not earned |
| **Tidy triads** | Three parallel items in every list; "不仅…而且…" frames | Balance without a choice |
| **Abstract nouns, no scene** | 赋能、打造、闭环、生态; "unlock potential", "navigate the landscape" | Nothing the reader can picture |
| **Owner-less claims** | "人们常说", "many believe", "studies show" with no study | No one is accountable for the claim |
| **Hedged stance** | 可能、或许、在一定程度上 stacked on every claim | The author never commits |
| **Even rhythm** | Sentences all about the same length; paragraphs the same shape | No emphasis, so nothing stands out |
| **Restating summary** | A closing paragraph that repeats the piece | Filling space instead of ending |
| **Moral stapled on** | A lesson sentence the piece didn't earn | Conclusion without a person who reached it |
| **Everything covered, nothing chosen** | Comprehensive, no trade-off, no "I'd skip this" | No taste |

## Fixing: ask, don't smooth

Rewriting an author-absent paragraph in smoother prose makes the problem harder to see. Instead, for each hotspot, ask the author for the missing ingredient:

| Missing | Ask |
|---|---|
| A scene | "When did you last see this happen? Who was there, what did they say?" |
| A number | "How big, how long, how many, compared with what?" |
| A stance | "Do you actually believe this? Would you tell a friend to do it?" |
| A trade-off | "What did you give up, or what would you skip?" |
| A boundary | "When is this advice wrong?" |
| A voice | "How would you say this out loud to a colleague?" |

Then help place the answer, tighten it, and keep their wording.

## Using the helper script

```bash
python3 scripts/absence_signals.py article.md          # markdown report
python3 scripts/absence_signals.py article.md --json   # machine-readable
```

It reports: singular first-person statements and distinct concrete specifics per 1000 characters (or words), stock phrases found, lists of three and paired frames, variation in sentence length, paragraphs that open with an enumerator, and paragraphs that contain no specific and no first person. Thresholds are rough and only meant to point you at places to look.

How to use the output:
1. Run it on the author's text.
2. Look at the flags and the generic paragraphs; read those paragraphs yourself.
3. Use them as hotspots in the audit, with a question for each.

## What the script cannot tell you
- **Who wrote the text.** A careful human can score badly and an AI draft with the author's facts pasted in can score well. Never present the result as detection.
- **Whether the ideas are good.** Concrete is not the same as insightful.
- **Short texts.** Under about 300 Chinese characters or 150 words, every signal is noise.
- **Genre.** Technical docs and legal text legitimately avoid first person. Read flags in context.
