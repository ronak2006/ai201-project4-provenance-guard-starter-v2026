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

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** _(To be decided in Milestone 4 after calibration runs.)_

**The numbers:** _(To be filled in after Milestone 4.)_

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human |  |  |
| unsure |  |  |
| high-confidence AI |  |  |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "...", "creator_id": "..."}'
```

```json

```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "...", "reasoning": "..."}'
```

```json

```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json

```

---

## How I Used AI

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



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
