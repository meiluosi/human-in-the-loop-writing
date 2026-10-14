#!/usr/bin/env python3
"""Surface signals that the author may be absent from a piece of writing.

This is a heuristic helper, not an AI detector. It cannot tell who wrote a text.
It counts things that tend to be thin when an author's own judgment and experience
are missing: first-person statements, concrete specifics, stock phrases, evenly
paced sentences, and paragraphs with nothing particular in them.

Usage:
    python3 absence_signals.py article.md
    python3 absence_signals.py article.md --json
    cat article.md | python3 absence_signals.py -

Works on Chinese, English, or a mix. Standard library only.
"""

import argparse
import json
import re
import statistics
import sys

CJK = re.compile(r"[一-鿿]")

STOCK_ZH = [
    "总而言之", "综上所述", "总的来说", "值得注意的是", "不可否认",
    "众所周知", "在当今", "赋能", "抓手", "闭环", "本质上", "让我们",
    "希望对你有所帮助", "不仅如此", "毫无疑问", "至关重要", "深入探讨", "全方位", "多维度",
]
STOCK_EN = [
    "in today's fast-paced", "it's important to note", "it is important to note", "delve",
    "tapestry", "in conclusion", "game-changer", "game changer", "unlock the", "navigate the",
    "landscape", "let's dive in", "in the realm of", "at the end of the day", "plays a crucial role",
    "a testament to", "moreover", "furthermore",
]
HEDGE_ZH = ["可能", "或许", "也许", "一定程度上", "某种程度上", "相对来说", "似乎", "往往", "通常"]
HEDGE_EN = ["perhaps", "maybe", "might", "arguably", "somewhat", "in some cases", "generally", "typically"]
ENUM_ZH = re.compile(r"^\s*(首先|其次|再次|最后|第[一二三四五六七八九十](点|步|，|、|：|:)|一方面|另一方面)")
ENUM_EN = re.compile(r"^\s*(first(ly)?|second(ly)?|third(ly)?|finally|lastly|in addition)\b", re.I)

SPECIFIC_NUM = re.compile(r"\d+(?:[.,]\d+)?%?")
SPECIFIC_LATIN = re.compile(r"(?<![A-Za-z])[A-Za-z][A-Za-z0-9_\-]{1,}")
QUOTED = re.compile(r"[「『“《\"][^」』”》\"]{1,30}[」』”》\"]")
TRIAD_ZH = re.compile(r"[^、，。；！？\n]{1,10}、[^、，。；！？\n]{1,10}、[^、，。；！？\n]{1,10}")
TRIAD_EN = re.compile(r"\b\w+(?:\s\w+){0,2},\s\w+(?:\s\w+){0,2},\s(?:and|or)\s\w+", re.I)
PAIR_ZH = re.compile(r"不仅[^。！？]{1,30}(而且|还|更)|既[^。！？]{1,20}又|一方面[^。！？]{1,40}另一方面")

SENT_SPLIT = re.compile(r"(?<=[。！？!?；])|(?<=[.!?])\s+|\n+")


def is_cjk(text):
    letters = len(CJK.findall(text))
    return letters > 0.3 * max(1, len(re.sub(r"\s", "", text)))


def size(text, cjk):
    return len(re.sub(r"\s", "", text)) if cjk else len(re.findall(r"\b\w+\b", text))


COMMON_TOKENS = {"ai", "app", "ok", "vs"}


def count_specifics(text, cjk):
    """Count distinct concrete items: numbers, quoted terms, names and technical tokens.

    Distinct, so that one buzzword repeated twenty times does not look specific.
    """
    items = set(SPECIFIC_NUM.findall(text))
    items |= set(QUOTED.findall(text))
    if cjk:
        items |= {t.lower() for t in SPECIFIC_LATIN.findall(text) if t.lower() not in COMMON_TOKENS}
    else:
        # in English, count capitalised words that do not start a sentence
        for sent in SENT_SPLIT.split(text):
            words = re.findall(r"[A-Za-z][A-Za-z0-9_\-']*", sent)
            items |= {w.lower() for w in words[1:] if w[0].isupper() and w != "I" and w.lower() not in COMMON_TOKENS}
    return len(items)


def count_first_person(text, cjk):
    """Count singular first-person statements ('I did', '我试过'). Collective 'we' is ignored on purpose."""
    if cjk:
        singular = len(re.findall(r"我(?!们)", text)) + len(re.findall(r"\b(I|I'm|I've|I'd|me|my)\b", text))
        return singular
    return len(re.findall(r"\b(I|I'm|I've|I'd|I'll|me|my|mine)\b", text))


STOCK_ZH_RE = {
    "首先/其次/最后，": re.compile(r"(?:^|[\u3002\uff01\uff1f\n])\s*(?:首先|其次|再次|最后)[，,]"),
    "随着…的发展": re.compile(r"随着[^，。]{2,12}的(?:快速)?(?:发展|进步|普及|深入|兴起)"),
}


def count_phrases(text, phrases):
    low = text.lower()
    hits = {}
    for p in phrases:
        n = low.count(p.lower())
        if n:
            hits[p] = n
    return hits


def analyze(text):
    cjk = is_cjk(text)
    unit = "chars" if cjk else "words"
    total = size(text, cjk)
    per_k = (1000.0 / total) if total else 0.0

    stock = count_phrases(text, STOCK_ZH + STOCK_EN)
    for label, rx in STOCK_ZH_RE.items():
        n = len(rx.findall(text))
        if n:
            stock[label] = n
    hedges = count_phrases(text, HEDGE_ZH + HEDGE_EN)
    triads = len(TRIAD_ZH.findall(text)) + len(TRIAD_EN.findall(text))
    pairs = len(PAIR_ZH.findall(text))

    sentences = [s.strip() for s in SENT_SPLIT.split(text) if s and s.strip()]
    lengths = [size(s, cjk) for s in sentences if size(s, cjk) > 0]
    cv = None
    if len(lengths) >= 8 and statistics.mean(lengths) > 0:
        cv = statistics.pstdev(lengths) / statistics.mean(lengths)

    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    min_len = 80 if cjk else 40
    generic, enum_opens = [], 0
    for i, p in enumerate(paragraphs, 1):
        if p.startswith("#") or set(p) <= set("-*=_ \n"):
            continue
        if ENUM_ZH.match(p) or ENUM_EN.match(p):
            enum_opens += 1
        if size(p, cjk) >= min_len and count_specifics(p, cjk) == 0 and count_first_person(p, cjk) == 0:
            generic.append({"paragraph": i, "starts": p[:36].replace("\n", " ")})
    body_paras = [p for p in paragraphs if not p.startswith("#")]

    m = {
        "language": "zh" if cjk else "en",
        "length": total,
        "unit": unit,
        "first_person_per_1000": round(count_first_person(text, cjk) * per_k, 1),
        "specifics_per_1000": round(count_specifics(text, cjk) * per_k, 1),
        "stock_phrase_hits": stock,
        "stock_phrase_total": sum(stock.values()),
        "hedge_hits": sum(hedges.values()),
        "list_of_three": triads,
        "paired_frames": pairs,
        "sentence_length_variation": None if cv is None else round(cv, 2),
        "enumerated_paragraph_openers": enum_opens,
        "generic_paragraphs": generic,
        "paragraph_count": len(body_paras),
    }

    flags = []
    if total < (300 if cjk else 150):
        flags.append("Text is short, so every signal below is noisy.")
    if total >= (600 if cjk else 300):
        if m["first_person_per_1000"] < (2 if cjk else 3):
            flags.append("Few first-person statements: the author rarely says what they did, saw or believe.")
        if m["specifics_per_1000"] < (6 if cjk else 12):
            flags.append("Few concrete specifics (numbers, names, quoted terms): claims stay abstract.")
    if m["stock_phrase_total"] >= 3:
        flags.append("Several stock phrases or transitions (see list).")
    if m["list_of_three"] + m["paired_frames"] >= 3:
        flags.append("Many tidy lists of three or paired frames ('not only... but also').")
    if cv is not None and cv < 0.35:
        flags.append("Sentence length is very even: the rhythm never changes.")
    if body_paras and len(generic) / len(body_paras) >= 0.3:
        flags.append("Many paragraphs have no specific, no number and no first person.")
    if enum_opens >= 3:
        flags.append("Three or more paragraphs open with an enumerator (first, second, finally).")
    m["flags"] = flags
    return m


def render(m):
    out = ["# Author-absence signals", ""]
    out.append(f"Language: {m['language']}, length: {m['length']} {m['unit']}, paragraphs: {m['paragraph_count']}")
    out.append("")
    out.append("| Signal | Value |")
    out.append("|---|---|")
    out.append(f"| First-person statements per 1000 | {m['first_person_per_1000']} |")
    out.append(f"| Concrete specifics per 1000 | {m['specifics_per_1000']} |")
    out.append(f"| Stock phrases | {m['stock_phrase_total']} |")
    out.append(f"| Lists of three / paired frames | {m['list_of_three']} / {m['paired_frames']} |")
    out.append(f"| Sentence length variation | {m['sentence_length_variation']} |")
    out.append(f"| Paragraphs opening with an enumerator | {m['enumerated_paragraph_openers']} |")
    out.append(f"| Generic paragraphs | {len(m['generic_paragraphs'])} of {m['paragraph_count']} |")
    out.append("")
    if m["stock_phrase_hits"]:
        out.append("Stock phrases found: " + ", ".join(f"{k} x{v}" for k, v in m["stock_phrase_hits"].items()))
        out.append("")
    if m["generic_paragraphs"]:
        out.append("Generic paragraphs (nothing specific, no first person):")
        for g in m["generic_paragraphs"]:
            out.append(f"- paragraph {g['paragraph']}: \"{g['starts']}...\"")
        out.append("")
    out.append("Flags:" if m["flags"] else "No flags raised.")
    for f in m["flags"]:
        out.append(f"- {f}")
    out.append("")
    out.append("These are hints about where the author may be missing. They do not show who wrote the text.")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path", help="text or markdown file, or - for stdin")
    ap.add_argument("--json", action="store_true", help="print JSON instead of a markdown report")
    args = ap.parse_args()
    text = sys.stdin.read() if args.path == "-" else open(args.path, encoding="utf-8").read()
    if not text.strip():
        print("Empty input.", file=sys.stderr)
        return 1
    m = analyze(text)
    print(json.dumps(m, ensure_ascii=False, indent=2) if args.json else render(m))
    return 0


if __name__ == "__main__":
    sys.exit(main())
