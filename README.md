# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

A piece of text travels through seven steps before the writer sees a verdict:

1. An HTTP POST arrives at `/submit` carrying a JSON body with `text` and `creator_id`.
2. `detector.model_signal(text)` runs the text through a local GPT-2 model and returns a 0–1 perplexity score — how predictable the text is to the model.
3. `stylometry.style_signal(text)` measures the *shape* of the text (sentence-length variation, vocabulary diversity, punctuation density) and returns a second 0–1 score.
4. `scoring.combine_signals(model_score, style_score)` merges the two scores into one combined 0–1 score using a weighted average.
5. `scoring.score_to_label(combined_score)` maps that number to a machine-readable guess (`"human"` / `"unsure"` / `"ai"`) and a human-readable label sentence.
6. `audit.log_decision(...)` appends the full record — both signal scores, the combined score, the guess, and the status — to `logs/audit.jsonl`.
7. The response goes back to the caller as JSON with `content_id`, `guess`, `confidence`, `label`, `model_score`, and `style_score`.

### The false-positive trace

A real writer submits their own work — plainly written, short sentences, everyday vocabulary, no semicolons. The model signal scores it 0.78: low perplexity, because common words are exactly what GPT-2 predicts easily. The style signal scores it 0.66: low sentence-length variation, narrower vocabulary than average. Combined score: ~0.72, above the AI threshold of 0.65. The label reads "AI-generated." The writer never wrote a word of AI output.

Their only recourse is `POST /appeal`. They send their `content_id` and explain in their own words. The service logs the appeal and flips their status to `under_review`. No automatic re-scoring happens. A human reviewer — if one exists — would have to look at it. The threshold that produced the wrong accusation is the same threshold every other submission uses, so changing it to fix this case changes it for everyone.

### Endpoint contracts

**POST /submit**

| Direction | Field | Type | Notes |
|-----------|-------|------|-------|
| In | `text` | string | The writing to evaluate |
| In | `creator_id` | string | Identifies the submitter |
| Out | `content_id` | string (UUID) | Stable ID for appeals and log lookup |
| Out | `guess` | `"human"` / `"unsure"` / `"ai"` | Machine-readable verdict |
| Out | `confidence` | float 0–1 | The combined score |
| Out | `label` | string | The sentence a reader actually sees |
| Out | `model_score` | float 0–1 | Signal 1 raw score |
| Out | `style_score` | float 0–1 | Signal 2 raw score |

**POST /appeal**

| Direction | Field | Type | Notes |
|-----------|-------|------|-------|
| In | `content_id` | string (UUID) | Must match an existing log entry |
| In | `reasoning` | string | The writer's explanation |
| Out | `ok` | bool | `true` if the appeal was recorded |
| Out | `content_id` | string | Echoed back |
| Out | `status` | string | `"under_review"` |
| Out | `message` | string | Confirmation the writer can read |

---

## Signals and Scoring

### Signal one — the model signal

**What it measures:** Perplexity — how surprised a GPT-2 language model is by the text. Low perplexity means the model could have predicted each word easily; high perplexity means the text kept surprising it. This is mapped to a 0–1 score where higher means more likely AI.

**Why that might differ between human and AI writing:** AI-generated text is produced by repeatedly choosing statistically likely next tokens, so a language model finds it easy to predict. Human writing wanders — odd word choices, abrupt turns, specific concrete details — producing text the model didn't expect.

**What it can't see:** Predictability is not authorship. Plain writing — short sentences, common vocabulary, clear structure — scores as AI-like regardless of who wrote it. Someone writing in a second language sticking to words they know, a younger writer, anyone writing for clarity: all are at higher risk of a false accusation. The signal also misses intentional AI prose that uses ornate or rare vocabulary, which surprises the model and scores as human.

### Signal two — the style signal

**What it measures:** The surface shape of the text — how much sentence lengths vary, how much vocabulary repeats (type-token ratio), and how much punctuation appears relative to text length — without understanding a single word of meaning.

**Why that might differ between human and AI writing:** AI-generated prose tends toward even, mid-length sentences and a narrower vocabulary band because "most likely next word" averages out variation over time. Human writing is lumpier: a three-word sentence next to a forty-word one, idiosyncratic punctuation habits, repeated pet phrases alongside unusual ones.

**What it can't see:** This signal cannot read. Any surface manipulation that changes the shape without changing the substance defeats it entirely: adding deliberate typos raises vocabulary variety, breaking long sentences raises sentence-spread, pasting in a quoted passage shifts punctuation density. All of these are trivially cheap to do on purpose, and the attack set for Unit 8 is built out of exactly this.

### The combining rule

**The rule:** Weighted average of the two signals. The model signal gets more weight (0.6) than the style signal (0.4) because it reads meaning, not just surface shape — it's harder to fool with simple text edits. When the two signals disagree, the model signal has the deciding say. This also protects plain-writing humans: the style signal tends to read uniform-but-human prose as AI-neutral, so giving it less weight avoids double-penalizing someone for writing clearly.

**The numbers:** `combined = 0.6 × model_score + 0.4 × style_score`

**Where it lives:** `scoring.py::combine_signals`

**A case where my two signals split, and what my rule does with it:** Lightly-edited AI text often retains low perplexity (model_score ~0.75) but acquires higher sentence-length variation from the editing (style_score ~0.35). The weighted rule produces ~0.59, which lands in the "unsure" band rather than "ai" — the editing has earned it genuine uncertainty rather than a confident wrong call. A 50/50 average would give 0.55 (still unsure), so both weightings agree here; the difference appears with more extreme splits.



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.35 | "This looks like it was written by a person. Our analysis found nothing that suggests otherwise." |
| unsure | 0.35 – 0.65 | "We're not certain about this one. Our tools noticed some patterns that can appear in AI-generated writing, but not enough to say so with confidence. This might simply reflect your writing style. If you wrote this yourself, you can submit an appeal." |
| high-confidence AI | 0.65 – 1.00 | "Our tools suggest this was likely written by an AI. If you wrote this yourself, you can submit an appeal and we'll take a closer look." |

**Why I worded the "unsure" one this way:** "Unsure" is the label a real person is most likely to get on work they wrote honestly, so it carries the highest risk of causing harm. It has to admit uncertainty without feeling like a soft accusation. The phrase "this might simply reflect your writing style" does two things: it names a real alternative explanation, and it shifts the frame from "you did something wrong" to "our tool has limits." Pointing to the appeal path gives the writer something to do other than feel accused with no recourse.



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "I stayed up too late finishing this. My eyes hurt and the words stopped making sense around page four, but I kept going because I wanted to get the argument right, not just done. That is probably a bad sign about my priorities.", "creator_id": "student-example"}'
```

```json
{
  "confidence": 0.4327,
  "content_id": "0554f516-bc08-4e0a-8102-9cb688417e73",
  "guess": "unsure",
  "label": "We're not certain about this one. Our tools noticed some patterns that can appear in AI-generated writing, but not enough to say so with confidence. This might simply reflect your writing style. If you wrote this yourself, you can submit an appeal.",
  "model_score": 0.4015,
  "style_score": 0.4794
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "0554f516-bc08-4e0a-8102-9cb688417e73", "reasoning": "I wrote every word of this myself at 1am after re-reading my notes."}'
```

```json
{
  "content_id": "0554f516-bc08-4e0a-8102-9cb688417e73",
  "message": "Your appeal has been recorded. A reviewer will look at this submission.",
  "ok": true,
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.4327,
      "content_id": "0554f516-bc08-4e0a-8102-9cb688417e73",
      "creator_id": "student-example",
      "guess": "unsure",
      "label": "We're not certain about this one. Our tools noticed some patterns that can appear in AI-generated writing, but not enough to say so with confidence. This might simply reflect your writing style. If you wrote this yourself, you can submit an appeal.",
      "model_score": 0.4015,
      "status": "decided",
      "style_score": 0.4794,
      "timestamp": "2026-11-05T01:18:01+00:00"
    },
    {
      "content_id": "0554f516-bc08-4e0a-8102-9cb688417e73",
      "creator_id": "student-example",
      "event": "appeal",
      "reasoning": "I wrote every word of this myself at 1am after re-reading my notes.",
      "status": "under_review",
      "timestamp": "2026-11-05T01:18:06+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* Help implementing the three stylometry measures in `stylometry.py` — specifically how to flip each raw metric so that high values meant AI-like rather than human-like, and how to get them onto a comparable scale before averaging.
- *What came back:* A suggestion to use coefficient of variation (stdev/mean) for sentence spread, subtract TTR from 1.0 for vocabulary, and scale punctuation density by a fixed factor (25×) so a typical value near 0.04 characters per character mapped to roughly 0.0 on the AI scale.
- *What I changed:* Accepted the CV and TTR approaches. For punctuation I changed the scaling factor after testing on sample text — the initial suggestion over-penalized plain prose with normal comma use, so I adjusted the multiplier until midrange human text landed near 0.5.

**Moment 2**

- *What I asked for:* Help wording the "unsure" label — specifically how to admit uncertainty without making a writer feel accused, since the instructions said this was the hardest one.
- *What came back:* Several draft labels, most of which leaned either too technical ("our confidence interval does not support a definitive classification") or too apologetic in a way that would still read as a soft accusation.
- *What I changed:* Wrote the final version myself, keeping only the structural idea from one of the drafts: name an alternative explanation before pointing to the appeal path. The phrase "this might simply reflect your writing style" is mine — none of the drafts used that framing.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 10 per minute, 200 per day

**Why those numbers and not others:**
A real writer submitting their own work might send 2–3 submissions in a sitting, rarely more than once a minute. 10/minute is comfortable for that use case. A threshold-mapping script sending hundreds of variations would hit the limit almost immediately. 200/day gives a writer room across a full workday without enabling bulk automated use.

**What a caller counts as:** Per `creator_id` — if no valid creator_id is present, falls back to remote IP. Per-creator limits mean one script using one identity is blocked, but a household of real writers sharing an IP are not punished together.

**The run of status codes when I pushed past it:**

```
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
```

---

## Attack Run — Before

See [`results/attack_run_2026-11-11_1756_before.md`](results/attack_run_2026-11-11_1756_before.md) for the full table.

Summary of verdicts:
- **Evasion (10):** 1 HELD (EV10 caught), 9 BROKE — AI text evaded as "human" or "unsure"
- **False positive (8):** 2 HELD (FP01, FP08), 6 BROKE — human writing labeled "ai"
- **Prompt injection (6):** 6 HELD — math-based signals can't be injected
- **Malformed content (8):** 2 HELD (whitespace/single-char rejected 400), 6 processed with unreliable scores
- **Malformed requests (12):** 8 HELD (400), 4 BROKE (500 crash — `'int'/'list'/'dict' object has no attribute 'strip'`)
- **Flood (12):** 10 HELD (200), 2 HELD (429 triggered correctly)

**Ten audit log entries from the run**

```json
{"timestamp": "2026-11-11T22:56:48+00:00", "content_id": "e07ca813-0437-4579-b3b7-cf7c25896dc4", "creator_id": "attacker_EV01", "guess": "human", "model_score": 0.1635, "style_score": 0.6129, "combined_score": 0.3433, "label": "This looks like it was written by a person. Our analysis found nothing that suggests otherwise.", "status": "decided"}
{"timestamp": "2026-11-11T22:56:49+00:00", "content_id": "d4dc96e6-97b1-45ff-821f-50d5f79ca9ad", "creator_id": "attacker_EV09", "guess": "unsure", "model_score": 0.7042, "style_score": 0.5494, "combined_score": 0.6423, "label": "We're not certain about this one. Our tools noticed some patterns that can appear in AI-generated writing, but not enough to say so with confidence. This might simply reflect your writing style. If you wrote this yourself, you can submit an appeal.", "status": "decided"}
{"timestamp": "2026-11-11T22:56:49+00:00", "content_id": "29eeb8ff-4386-4f4d-8f0f-bdb06423df30", "creator_id": "attacker_FP02", "guess": "ai", "model_score": 0.7387, "style_score": 0.6811, "combined_score": 0.7157, "label": "Our tools suggest this was likely written by an AI. If you wrote this yourself, you can submit an appeal and we'll take a closer look.", "status": "decided"}
{"timestamp": "2026-11-11T22:56:49+00:00", "content_id": "5855880f-83a0-4e22-bc99-c802ecec03e2", "creator_id": "attacker_FP03", "guess": "ai", "model_score": 0.8051, "style_score": 0.6767, "combined_score": 0.7537, "label": "Our tools suggest this was likely written by an AI. If you wrote this yourself, you can submit an appeal and we'll take a closer look.", "status": "decided"}
{"timestamp": "2026-11-11T22:56:49+00:00", "content_id": "1379a403-3981-400a-8bb3-cef3699dede4", "creator_id": "attacker_FP04", "guess": "ai", "model_score": 0.8329, "style_score": 0.6221, "combined_score": 0.7486, "label": "Our tools suggest this was likely written by an AI. If you wrote this yourself, you can submit an appeal and we'll take a closer look.", "status": "decided"}
{"timestamp": "2026-11-11T22:56:49+00:00", "content_id": "6b92d59a-042b-4f18-967e-5ae53525acb0", "creator_id": "attacker_FP07", "guess": "ai", "model_score": 0.8816, "style_score": 0.6569, "combined_score": 0.7917, "label": "Our tools suggest this was likely written by an AI. If you wrote this yourself, you can submit an appeal and we'll take a closer look.", "status": "decided"}
{"timestamp": "2026-11-11T22:56:49+00:00", "content_id": "27e11826-3b52-47c4-8b1e-096d465cc368", "creator_id": "attacker_PI02", "guess": "human", "model_score": 0.2044, "style_score": 0.4982, "combined_score": 0.3219, "label": "This looks like it was written by a person. Our analysis found nothing that suggests otherwise.", "status": "decided"}
{"timestamp": "2026-11-11T22:56:49+00:00", "content_id": "35c76e52-1abf-49b2-834b-4c4494c05812", "creator_id": "attacker_MF03", "guess": "human", "model_score": 0.0, "style_score": 0.6667, "combined_score": 0.2667, "label": "This looks like it was written by a person. Our analysis found nothing that suggests otherwise.", "status": "decided"}
{"timestamp": "2026-11-11T22:56:49+00:00", "content_id": "d2bb6cd2-92b6-4be1-a6f9-4572eed0cf9c", "creator_id": "attacker_MF06", "guess": "ai", "model_score": 0.9969, "style_score": 1.0, "combined_score": 0.9981, "label": "Our tools suggest this was likely written by an AI. If you wrote this yourself, you can submit an appeal and we'll take a closer look.", "status": "decided"}
{"timestamp": "2026-11-11T22:55:58+00:00", "creator_id": "flood_tester", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "10 per 1 minute"}
```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

**FP03** — a non-native English speaker writing carefully. Labeled `ai` with confidence 0.754 (model: 0.805, style: 0.677). Both signals agreed. The model signal is high because careful, grammatically precise writing is predictable to GPT-2 — it closely resembles patterns in its training data. The style signal is elevated because careful writing tends toward consistent sentence lengths and controlled punctuation density. There is no way to explain to this writer why writing carefully is evidence against them.



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
