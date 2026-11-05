# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. False positives — at most 1 in 10 pieces of my own writing is labeled high-confidence AI

Of 10 pieces I wrote myself, at most 1 receives the `"ai"` guess across all three evaluation trials.

**Why this target:** A wrong accusation lands on a real person. On any writing platform, being told your own work is AI-generated is damaging and hard to dispute. Missing some AI-generated text costs the site a little friction; falsely accusing a writer costs that person their credibility. I allow 1 in 10 rather than 0 because the blind spot in signal one is real — plain, clearly-written prose can legitimately score high — but I'm not willing to go higher than that.

---

## 2. Score spread — clearly AI and clearly human text differ by at least 0.4

Given one piece of text I judge clearly AI-generated and one I judge clearly human-written, their combined scores differ by at least 0.4 in all three trials.

**Why this target:** If the two signals together can't separate an obvious case, the system isn't detecting anything useful — it's just generating noise around 0.5. A spread of 0.4 (e.g., 0.7 vs. 0.3) means the labels "ai" and "human" are actually reachable from real inputs. Anything smaller means the thresholds are sitting in a range the system never actually reaches.

---

## 3. Label coverage — all three labels are reachable from real input

I can produce each of the three labels — `"human"`, `"unsure"`, and `"ai"` — by submitting real (not synthetic) text. All three appear in the audit log by the end of Milestone 5.

**Why this target:** A label that no input ever produces is a dead branch. If the thresholds are set such that "unsure" is unreachable, the service is binary when it claims to be three-way. The "unsure" label matters most: it's what the system should return when it genuinely doesn't know, and if it never fires, the system is overclaiming certainty on every borderline case.

---

## 4. Appeal path — every appeal changes status and appears in the log

Of 5 appeals submitted via `POST /appeal` with valid `content_id` values, all 5 return `ok: true`, flip the entry's status to `under_review`, and appear as appeal events in `logs/audit.jsonl`.

**Why this target:** The appeal path is the only recourse a falsely-accused writer has. If it silently fails — returns 200 but doesn't write to the log, or changes nothing — the writer believes they've been heard when they haven't. This criterion is binary: it either works every time or it doesn't work. 4 out of 5 is not acceptable for someone's only way to dispute a wrong verdict.

---

## 5. Bad input — missing or empty text returns a 4xx, not a crash

When `text` is missing from the JSON body, or is an empty string, the service returns a 400-level status code with a JSON error body. It does not return a 500 and does not raise an unhandled exception, across all three trials.

**Why this target:** A crash on malformed input is one of the most common real production failures and one of the most embarrassing. If `detector.model_signal("")` raises an exception and the route doesn't catch it, the service returns a 500 that looks like the whole system is broken — when really it's just bad input. A 400 tells the caller what went wrong; a 500 tells them nothing useful and breaks monitoring.



---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
