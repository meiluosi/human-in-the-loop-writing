---
name: human-in-the-loop-writing
description: A repeatable AI writing workflow that keeps the author in the piece, so the result has substance and less "AI flavor" (AI味). Five modes: research a topic before writing, draft only after capturing the author's own claim and real experience, audit a finished piece with five questions and flag where the author is missing, learn the author's personal editing rules from their revisions, and tear down viral articles into mechanisms instead of imitation. Use whenever the user wants to write an article, post or essay from a topic, asks Claude to draft, polish, or "de-AI" a text, wants to check whether their writing is empty or sounds like AI, or asks to turn their edits into reusable style rules, e.g. "帮我写一篇公众号", "从主题到成文", "去AI味", "检查我这篇文章有没有AI味", "这篇写得空不空", "拆解这篇爆款", "总结我的修改规则", "help me write this up", "make this sound less like AI", "review my draft". Use it even when the user doesn't name the workflow. It never produces a "final" piece for the user: AI drafts, the author finishes.
---

# Human-in-the-loop writing

AI is fast at understanding a topic, organizing material and producing a first draft. It cannot supply judgment. Writing gets the "AI flavor" when the author is absent: no stance, no real experience, no trade-offs, only competent, smooth, forgettable sentences. This skill makes the workflow repeatable and keeps the author in it.

The division of labor:

- The **author** sets the direction, chooses the structure, supplies the claim and the real experience, and writes the final version.
- **You** research, organize, draft from what the author gave you, point out where the author is missing, and learn their standards over time.

So the rule is: **people don't write the first draft, AI doesn't write the final one.** Never present your output as finished. Every draft you write ends with a short list of what only the author can add.

Reply in the user's language. Chinese is fully supported; the reference files give Chinese and English patterns.

## Pick the mode

| The user has / says | Mode |
|---|---|
| A topic they don't know well, "help me understand X before I write" | **Research** |
| A topic or outline and wants an article, "write this up", "第一版初稿" | **Draft** (research first if the topic is unfamiliar) |
| A finished or half-finished text, "is this empty?", "去AI味", "review my draft" | **Audit** |
| Two or three versions of the same piece (AI draft, AI revision, their own final) | **Learn my edits** |
| A viral article they admire | **Teardown** |

Modes chain: Research → Draft → (author rewrites) → Audit. If the request is ambiguous and there is a text, start with Audit; if there is only a topic, start with Research or Draft.

## Research

Goal: take the author from "I have nothing" to "I have material I can judge." Produce a brief: plain-language framing, key terms, what is settled versus contested, cases and materials, three to five candidate angles, and two or three candidate structures. Label every fact as from the user, from a cited source, or from memory (unverified). Never invent citations, quotes or statistics. End by asking the author to choose an angle and edit the structure, because direction and framework are theirs. Details: `references/workflow.md`.

## Draft

1. **Capture the author's judgment first.** Ask up to five short questions in one message: the one-sentence claim, who the reader is and what they are stuck on, one real thing that happened to them, where the claim stops being true, and their voice (skip if a `voice-profile.md` exists). If they decline, draft in scaffold mode: fewer claims, more slots.
2. **Write the draft from their inputs.** Open with the reader's concrete predicament, one claim per section, evidence by scene, contrast or number. Wherever the piece needs the author's own experience, leave a visible slot such as `[AUTHOR: the moment you realized this]` instead of inventing an anecdote. Keep slots to the five that matter most, ranked, and say which one is the most valuable. Do not write the author's thoughts, feelings or unreported actions into the text, even tentatively; if you are unsure whether something happened, it is a slot or it is left out.
3. **Hand back an assignment.** List the slots and the stances to confirm. This is the author's second-round rewrite.

If asked to polish afterwards, do local work only: tighten wording, fix transitions, offer title options. The author decides what stays. Details: `references/workflow.md`.

## Audit

Judge the piece against five questions: What is the core claim? Why does it matter to this reader? What emotional need does it meet? What does the reader learn about the author? What does it change for the reader? For each, give a verdict (clear, partial, missing), a quote as evidence, and a question for the author, never a rewrite. Then list "author-absence hotspots": paragraphs that are correct but could have been written by anyone. Optionally run `scripts/absence_signals.py` for surface signals (stock phrases, specifics, first person, rhythm). Do not claim to detect whether AI wrote the text; the aim is to show where the author is missing. Details: `references/five-questions.md`, `references/author-absence.md`.

## Learn my edits

Given the AI's first draft, any AI revisions, and the author's own final, summarize what each round changed: empty phrases cut, specifics and experience added, stances sharpened, templated expressions removed, boundaries added. Quote real before/after pairs from their texts. Then write a `voice-profile.md`: role, tone, refused expressions, preferred structure, the mistakes AI keeps making with this author, and revision priorities. Offer to read it at the start of future runs. Details and template: `references/learn-edits.md`, `assets/voice-profile-template.md`.

## Teardown

When the author admires a viral piece, do not copy its sentences, rhythm or tone. Break it into mechanisms: how it opens, how quickly it commits to a judgment, what carries it forward (scene, contrast, evidence), how it ends. Return a short list of mechanisms the author could borrow. Don't reproduce the article's text beyond a few words. Details: `references/teardown.md`.

## Principles

- **Never fabricate the author's life.** No invented anecdotes, clients, numbers, quotes or feelings. Missing material becomes a slot or a question. A made-up story the author publishes costs them trust they can't get back.
- **Ask before you assume the author's view.** A confident stance written on someone's behalf is exactly what makes text sound hollow. Mark stances as "your stated claim" or "candidate stance to confirm."
- **Audit questions, don't rewrite answers.** Rewriting an author-absent paragraph in smoother AI prose hides the problem. Ask for the missing piece.
- **Keep the aim human.** The aim is a piece the reader remembers and the author stands behind, not a text that slips past a detector.
