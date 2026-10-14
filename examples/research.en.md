> **About this example:** real output from `human-in-the-loop-writing` in Research mode, with the body unedited and only this note added.
>
> Request: "I'm a founder and I know almost nothing about retrieval-augmented generation (RAG). I want to write a LinkedIn article for other non-technical founders about whether they actually need it. Help me get up to speed first, then we'll write it."
>
> The model used web search; facts are labelled by where they came from. Check the links before quoting anything.

---

# Research brief: do non-technical founders actually need RAG?

Research comes first, then the draft. By the end of this brief you should be able to disagree with it, which is the point. I did a few web searches. Facts are labeled **[source]** (with a link), **[memory, unverified]** (from my own knowledge, so check before you publish), or **[from you]** (nothing yet, since you've told me nothing about your own situation).

## 1. Framing

A language model like Claude or ChatGPT knows what it learned in training. It does not know your company's pricing sheet, last week's policy change, or your customer contracts. It also can't tell you when it doesn't know. It tends to answer anyway, fluently and sometimes wrongly.

**RAG (retrieval-augmented generation)** is one way to fix that. Before the model answers, a separate step looks up the relevant pieces of your own documents and puts them in front of the model, which then answers using them. It's an open-book exam instead of a closed-book one. The model doesn't learn your documents. It reads the relevant pages each time someone asks.

The idea comes from a 2020 research paper by Patrick Lewis and colleagues at Facebook AI Research. The paper's argument was to keep the model's knowledge separate from the model, so you can update the knowledge without retraining the model. **[source: [summary of Lewis et al. 2020](https://latenode.com/news/rag-lewis-2020-paper-understanding-original-retrieval-augmented-generation-research); the primary source is arXiv 2005.11401, and I have only read secondary summaries]**

Why a founder would care: vendors, consultants and your own engineers will say "we need RAG" for anything involving AI plus company data. Sometimes that's right. Often it's the expensive answer to a cheap question. That gap is your article.

## 2. Key terms

| Term | One-line meaning | Commonly misused? |
|---|---|---|
| **RAG** | Look up relevant passages from your documents, hand them to the model, let it answer from them. | Yes. It's often used to mean "any AI that knows our data". |
| **Retrieval** | The lookup step. Usually a search that matches by meaning rather than exact keywords. | |
| **Embeddings / vector database** | The technique and storage that make "search by meaning" work. As a founder you only need to know it's plumbing, not the point. | Yes. It's sold as the product, but it's a component. |
| **Context window** | How much text the model can read in a single request. Modern ones are big enough to take a long handbook. | |
| **Long context ("just paste it in")** | Skipping retrieval entirely and putting all your documents into the prompt. | Often overlooked as the cheap alternative. |
| **Fine-tuning** | Further training the model on your examples. It changes *behavior* (tone, format, specialized skill), not reliably *facts*. | Yes. Many people think it's how you "teach the AI your data". |
| **Hallucination** | The model stating something false with confidence. | RAG reduces it. It doesn't eliminate it. |
| **Grounding / citations** | Making the answer point to the source document so a human can check it. | |

## 3. What's settled and what's contested

**Broadly agreed** (the sources below are mostly vendor and practitioner blogs, so treat the numbers as rules of thumb, not benchmarks):

- RAG makes sense when knowledge is large, changes often, or answers must be traceable to a source. Fine-tuning is poor at adding facts, since facts go stale. **[source: [Unite.ai comparison](https://www.unite.ai/long-context-vs-rag-vs-fine-tuning-which-should-you-use/), [Denser.ai guide](https://denser.ai/blog/rag-vs-fine-tuning/), [AI Builder Club](https://www.aibuilderclub.com/blog/rag-vs-long-context-vs-fine-tuning)]**
- If the material is small and stable, you can often paste it into the prompt and skip RAG. One practitioner puts the line at roughly 50K tokens (about a few dozen pages) that rarely change, and calls RAG for a 30-page handbook "premature engineering". Another guide puts RAG as the best bet above roughly 500 pages. **[source: same comparison guides, [aggregated search result](https://www.aibuilderclub.com/blog/rag-vs-long-context-vs-fine-tuning); these thresholds are single-author heuristics and I could not confirm them against a neutral benchmark]**
- These approaches are layers, not rivals. Production systems often combine them. **[source: same guides]**

**Contested or unsettled** (this is where your article can have a position):

- **Where the "just paste it in" line really is.** Context windows keep growing, which keeps moving the line. One comparison notes that quality can degrade as you stuff more text in. **[source: [myscale comparison](https://myscale.com/blog/rag-vs-large-context-llms/), a vendor blog]** I'd also expect a lot of disagreement on cost per question at scale **[memory, unverified]**.
- **How reliable RAG really is.** I recall academic work showing that commercial RAG-based legal research tools still produced wrong answers at a notable rate, so "RAG" does not mean "trustworthy". **[memory, unverified: I believe this was a Stanford study on legal AI tools in 2024, but I don't have the exact figures or a link. Do not quote numbers until we find the paper.]**
- **Whether a small company should build or buy.** Many off-the-shelf tools ("chat with your docs", help-desk bots, enterprise search) already contain RAG. Whether a founder should ever build their own is a judgment call and opinions differ. **[memory, unverified]**

## 4. Cases and materials

**Air Canada chatbot (a cautionary tale about unchecked company chatbots, but not clearly a RAG case).** In February 2024, British Columbia's Civil Resolution Tribunal ruled that Air Canada was responsible for wrong advice its chatbot gave a customer about bereavement fares. The airline argued the chatbot was a separate legal entity, and the tribunal rejected that. Sources disagree on the exact award (figures between about CAD $650 and $812 appear), so check the decision before quoting a number. **[source: [Daily Hive](https://dailyhive.com/canada/air-canada-chatbot-decision), [Kiplinger](https://kiplinger.com/personal-finance/travel/air-canada-to-pay-a-partial-refund-for-chatbot-error), [Fox Business](https://foxbusiness.com/lifestyle/air-canada-chatbot-gave-customer-wrong-info-airline-pay)]** Caution: I found nothing confirming the chatbot used RAG. I'd use it only as "the company owns what its bot says", not as "RAG failed".

**The original RAG paper (2020).** Useful for one sentence of history: the idea is about keeping knowledge outside the model so it can be updated. **[source: see above]**

**Your own material.** **[from you: none yet.]** This is the gap. Everything above is public background that any writer could assemble. The material that makes your article yours is the "we considered this and here's what happened" part, which only you have. See the questions at the end.

**Things I could not find or verify and will not invent:** typical costs of a RAG project for a small company, failure rates in real deployments, or a named startup that wasted money on RAG unnecessarily. If you want these, the best source is people you know. Ask two or three founders or engineers what it actually cost them.

## 5. Candidate angles

Each angle is a claim you'd have to stand behind. These are candidates for you to accept, reject or replace. They are not your views.

1. **"Probably not yet: paste the documents in first."** Reader: a founder with a small pile of documents (policies, FAQs, product docs) being pitched a RAG build. Claim: for small, stable material, long context or an off-the-shelf tool is enough, and RAG is something you graduate to.
2. **"The real question is not RAG, it's what your AI is allowed to get wrong."** Reader: a founder about to put a bot in front of customers. Claim: the decision should start from the cost of a wrong answer (the Air Canada logic), and RAG is one tool for citations and traceability, not a guarantee.
3. **"Three questions that tell you if you need RAG."** Reader: a founder who needs a quick decision rule. Claim: you need it only if your knowledge is big, changing, or must be cited. Practical and shareable, but the easiest to make generic.
4. **"Don't confuse RAG with fine-tuning (and what that costs you)."** Reader: a founder who's heard both words and thinks they mean "teach the AI our data". Claim: untangling them saves real money. Narrow, but a real confusion.
5. **"Buy, don't build."** Reader: a founder without an engineering team. Claim: if you need RAG, you almost certainly want a product that already includes it. This depends on your actual experience.

## 6. Candidate structures

**A. Decision tree (suits angle 1 or 3).** Open with the pitch moment ("someone told you that you need RAG") → what it is, in one open-book-exam analogy → the three cheaper things to try first → the three signs you've outgrown them → what to ask your vendor or engineer.

**B. One story, then the principle (suits angle 2 or 5).** Open with a specific scene (yours, once you tell me one) → what went right or wrong → the explanation of RAG that scene needed → the rule you took from it → what to do on Monday.

**C. Myth-busting (suits angle 4).** Three common beliefs ("AI needs to be trained on our data", "RAG stops hallucinations", "we need a vector database") → what's true in each → what to ask instead.

## 7. What I need from you

Direction and structure are yours. Please do these:

1. **Pick an angle** (or write your own) and **edit a structure**. A pick like "angle 2, structure B, but skip the history" is plenty.
2. **Tell me the one-sentence claim** you want a reader to remember.
3. **Tell me about a real moment.** Have you been pitched RAG, been tempted to build something, or used a "chat with our docs" tool? A scene, a number, a mistake. That's what the article is built on.
4. **Who exactly is the reader and what are they stuck on?** "Non-technical founders" is broad. Pre-revenue or at scale? Do they have an engineer? Are they customer-facing?
5. **Where does your claim stop being true?** For example, at what size or risk level would you say yes, build it?
6. **Your voice**, in a line: blunt or warm, jargon allowed or not, words you refuse. Or paste something you've written and I'll learn from it.

If you'd rather skip some of these, say "just write it" and I'll produce a scaffold draft: structure and explanations, with clearly marked slots where your stance and experience go. It won't be a finished piece, because you finish it.

**Before you publish anything from this brief,** check the items marked memory, unverified, and read the original paper (arXiv 2005.11401) if you plan to describe it.

Sources:
- [Lewis et al. 2020 summary (Latenode)](https://latenode.com/news/rag-lewis-2020-paper-understanding-original-retrieval-augmented-generation-research)
- [Long Context vs RAG vs Fine-Tuning (Unite.ai)](https://www.unite.ai/long-context-vs-rag-vs-fine-tuning-which-should-you-use/)
- [RAG vs Fine-Tuning decision guide (Denser.ai)](https://denser.ai/blog/rag-vs-fine-tuning/)
- [RAG vs Long Context vs Fine-Tuning (AI Builder Club)](https://www.aibuilderclub.com/blog/rag-vs-long-context-vs-fine-tuning)
- [RAG vs large context LLMs (MyScale)](https://myscale.com/blog/rag-vs-large-context-llms/)
- [Air Canada chatbot decision (Daily Hive)](https://dailyhive.com/canada/air-canada-chatbot-decision)
- [Air Canada partial refund (Kiplinger)](https://kiplinger.com/personal-finance/travel/air-canada-to-pay-a-partial-refund-for-chatbot-error)
- [Air Canada chatbot (Fox Business)](https://foxbusiness.com/lifestyle/air-canada-chatbot-gave-customer-wrong-info-airline-pay)
