"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    Coefficient of variation of sentence word-lengths (stdev / mean).

    Higher spread = more varied sentence lengths = more human-like.
    Returns 0.0 for a single sentence (no spread to measure).
    """
    sents = sentences(text)
    if len(sents) < 2:
        return 0.0
    lengths = [len(words(s)) for s in sents]
    mean = statistics.mean(lengths)
    if mean == 0:
        return 0.0
    return statistics.stdev(lengths) / mean


def type_token_ratio(text: str) -> float:
    """
    Unique words / total words. Higher means more varied vocabulary.

    Returns 0.0 for empty text.
    """
    ws = words(text)
    if not ws:
        return 0.0
    return len(set(ws)) / len(ws)


def punctuation_density(text: str) -> float:
    """
    Expressive punctuation (commas, semicolons, colons, dashes, exclamation
    marks, question marks) relative to total characters.

    Skips full stops — they're too uniform across writers to be useful.
    Higher density = more varied punctuation habits = more human-like.
    Returns 0.0 for empty text.
    """
    if not text:
        return 0.0
    expressive = set(",;:—–-!?")
    count = sum(1 for ch in text if ch in expressive)
    return count / len(text)


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. Higher means more likely AI.

    Each measure points toward human at its high end, so each needs
    flipping to match the direction of model_signal (high = AI):

      spread:  low spread → uniform sentences → AI-like → AI score = 1/(1+spread)
      ttr:     low TTR → repetitive vocab → AI-like → AI score = 1 - ttr
      punct:   low expressive punct → plain/uniform → AI-like → AI score = 1 - min(punct*20, 1)

    The three flipped scores are averaged equally.
    """
    spread = sentence_length_spread(text)
    ttr = type_token_ratio(text)
    punct = punctuation_density(text)

    # Flip each so that high value = more AI
    spread_ai = 1.0 / (1.0 + spread)          # spread=0 → 1.0 (AI); spread=2 → 0.33 (human)
    ttr_ai = 1.0 - ttr                         # ttr=0.4 → 0.6 (AI-ish); ttr=0.9 → 0.1 (human)
    punct_ai = 1.0 - min(punct * 25, 1.0)     # scale: 0.04 punct/char ≈ neutral; above → human

    score = (spread_ai + ttr_ai + punct_ai) / 3.0
    return round(min(max(score, 0.0), 1.0), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
    print("\nAll zeros? These are stubs — Milestone 4 is where you build them.")
