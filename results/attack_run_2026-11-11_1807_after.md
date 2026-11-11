# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-11 18:07
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `becc5139-9133-469e-8e5d-dae8e4348f7d` | human | 0.343 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `da90dc43-06fb-4f0d-961c-29cfcc9b44f4` | unsure | 0.567 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `43b3f90a-4d90-435f-91dc-ece3dcd912b6` | unsure | 0.621 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `0fb37d06-1fa7-4dbd-8089-c94e11b279a8` | unsure | 0.606 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `b0b11c39-a8f6-4ef6-ad35-91c3e86dc14e` | unsure | 0.386 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `1271ba44-c94f-4640-9c15-dbc4ab1cdfb4` | unsure | 0.556 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `457b5e96-69e2-4c87-9bfc-378c00c9af24` | unsure | 0.551 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `0aa13919-52d6-4537-95ec-eba9acc1af4f` | unsure | 0.384 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `47c3b26b-a168-4d7e-86a8-3046e4b119d2` | unsure | 0.642 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `3d5e5f6a-e1a8-4be2-9e77-0d2039a9d947` | ai | 0.907 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `48a20aac-09dd-4e34-ba00-a9738df6c322` | unsure | 0.621 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `a7a116a4-a533-488b-a4be-f4bf8e6f95b4` | ai | 0.716 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `af1ea694-92fc-4165-b4af-b446ccf02563` | ai | 0.754 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `d660ed19-59cb-4acd-9132-bb1c07a31013` | ai | 0.749 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `0818188a-ef7e-46f4-a926-4bb1c9c60320` | ai | 0.756 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `ff282738-abf4-472f-94f5-bd593348cb1e` | ai | 0.776 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `d9f083b3-7b37-4611-b78a-840224e3dd73` | ai | 0.792 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `9a162b9c-6f42-43cd-b886-681dbbd2d7da` | unsure | 0.420 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `673a3e96-1d6d-4bc8-802d-72db9d23bdfe` | unsure | 0.500 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `543667e7-e5c2-464d-9c13-adc4920f5a7b` | human | 0.322 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `ae8a2991-5078-4dcc-8278-0b3790517107` | unsure | 0.593 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `61cf6c28-9aea-4609-96b2-3bc7caa4c9b5` | unsure | 0.523 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `599e705f-bef6-45e0-a5f7-1ffe69c098c6` | unsure | 0.518 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `9ee6f8ff-7d29-44c8-ab71-5e7c2f74b484` | unsure | 0.588 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `542cec91-4976-4015-923d-aa28c7924eff` | human | 0.267 |  |
| MF04 | malformed | text is only punctuation | 200 | `48fba2df-ab7c-4ccb-bd16-db009b5b7d4e` | human | 0.273 |  |
| MF05 | malformed | text is a very long single word | 200 | `5ddd25dd-f9a3-4fd2-a836-ea3913f8a997` | ai | 0.865 |  |
| MF06 | malformed | text is emoji only | 200 | `8443717f-4ebf-4d0f-a619-23ce6b47bbf5` | ai | 0.998 |  |
| MF07 | malformed | text is right-to-left script | 200 | `b7797b8b-e81c-4974-97b4-77f918e7c0ba` | ai | 0.944 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `0c7b9898-74f3-460c-a7fc-10763fa2d9da` | ai | 0.939 |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `85f1bf74-8e70-475c-82ac-2a1fd361ee7f` | unsure | 0.410 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `cf6e85de-01ce-4fd3-9a4c-bc2592ae6727` | human | 0.296 |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `789b4ce6-7fec-476a-a596-d44cb7603b70` | human | 0.284 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e39491d4-243c-427c-be9e-151b4b250c0d` | human | 0.284 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f057c678-91ea-40d4-9cba-68a27a5146de` | human | 0.284 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9aedd39c-3459-48e4-b6b6-b069da0f704f` | human | 0.284 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d2cfd6e7-5c04-4186-b123-8f3305fb4a20` | human | 0.284 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `bfc49e6a-07a8-4757-a497-352dcd4a0650` | human | 0.284 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9f6cd17e-0c76-4a24-91ea-e73c1af5ea75` | human | 0.284 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d74cb59a-c860-434e-bc88-d8aef44bf424` | human | 0.284 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `dda48ef5-f467-40d0-bb4a-914cf669620e` | human | 0.284 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `47c515ee-90fd-4f0a-88ce-d05338a32523` | human | 0.284 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "becc5139-9133-469e-8e5d-dae8e4348f7d",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.3433,
  "model_score": 0.1635,
  "style_score": 0.6129,
  "label": "This looks like it was written by a person. Our analysis found nothing that suggests otherwise.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "da90dc43-06fb-4f0d-961c-29cfcc9b44f4",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.5666,
  "model_score": 0.5943,
  "style_score": 0.5251,
  "label": "We're not certain about this one. Our tools noticed some patterns that can appear in AI-generated writing, but not enough to say so with confidence. This might simply reflect your writing style. If you wrote this yourself, you can submit an appeal.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "43b3f90a-4d90-435f-91dc-ece3dcd912b6",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.621,
  "model_score": 0.6662,
  "style_score": 0.5532,
  "label": "We're not certain about this one. Our tools noticed some patterns that can appear in AI-generated writing, but not enough to say so with confidence. This might simply reflect your writing style. If you wrote this yourself, you can submit an appeal.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "0fb37d06-1fa7-4dbd-8089-c94e11b279a8",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.6055,
  "model_score": 0.6114,
  "style_score": 0.5966,
  "label": "We're not certain about this one. Our tools noticed some patterns that can appear in AI-generated writing, but not enough to say so with confidence. This might simply reflect your writing style. If you wrote this yourself, you can submit an appeal.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "b0b11c39-a8f6-4ef6-ad35-91c3e86dc14e",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.3858,
  "model_score": 0.3212,
  "style_score": 0.4827,
  "label": "We're not certain about this one. Our tools noticed some patterns that can appear in AI-generated writing, but not enough to say so with confidence. This might simply reflect your writing style. If you wrote this yourself, you can submit an appeal.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "1271ba44-c94f-4640-9c15-dbc4ab1cdfb4",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.5557,
  "model_score": 0.5727,
  "style_score": 0.5301,
  "label": "We're not certain about this one. Our tools noticed some patterns that can appear in AI-generated writing, but not enough to say so with confidence. This might simply reflect your writing style. If you wrote this yourself, you can submit an appeal.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "457b5e96-69e2-4c87-9bfc-378c00c9af24",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5507,
  "model_score": 0.5862,
  "style_score": 0.4975,
  "label": "We're not certain about this one. Our tools noticed some patterns that can appear in AI-generated writing, but not enough to say so with confidence. This might simply reflect your writing style. If you wrote this yourself, you can submit an appeal.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "0aa13919-52d6-4537-95ec-eba9acc1af4f",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.3844,
  "model_score": 0.2452,
  "style_score": 0.5932,
  "label": "We're not certain about this one. Our tools noticed some patterns that can appear in AI-generated writing, but not enough to say so with confidence. This might simply reflect your writing style. If you wrote this yourself, you can submit an appeal.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "47c3b26b-a168-4d7e-86a8-3046e4b119d2",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.6423,
  "model_score": 0.7042,
  "style_score": 0.5494,
  "label": "We're not certain about this one. Our tools noticed some patterns that can appear in AI-generated writing, but not enough to say so with confidence. This might simply reflect your writing style. If you wrote this yourself, you can submit an appeal.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "3d5e5f6a-e1a8-4be2-9e77-0d2039a9d947",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.9071,
  "model_score": 0.9792,
  "style_score": 0.799,
  "label": "Our tools suggest this was likely written by an AI. If you wrote this yourself, you can submit an appeal and we'll take a closer look.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "48a20aac-09dd-4e34-ba00-a9738df6c322",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.6214,
  "model_score": 0.6175,
  "style_score": 0.6273,
  "label": "We're not certain about this one. Our tools noticed some patterns that can appear in AI-generated writing, but not enough to say so with confidence. This might simply reflect your writing style. If you wrote this yourself, you can submit an appeal.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "a7a116a4-a533-488b-a4be-f4bf8e6f95b4",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.7157,
  "model_score": 0.7387,
  "style_score": 0.6811,
  "label": "Our tools suggest this was likely written by an AI. If you wrote this yourself, you can submit an appeal and we'll take a closer look.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "af1ea694-92fc-4165-b4af-b446ccf02563",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7537,
  "model_score": 0.8051,
  "style_score": 0.6767,
  "label": "Our tools suggest this was likely written by an AI. If you wrote this yourself, you can submit an appeal and we'll take a closer look.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "d660ed19-59cb-4acd-9132-bb1c07a31013",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.7486,
  "model_score": 0.8329,
  "style_score": 0.6221,
  "label": "Our tools suggest this was likely written by an AI. If you wrote this yourself, you can submit an appeal and we'll take a closer look.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "0818188a-ef7e-46f4-a926-4bb1c9c60320",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7563,
  "model_score": 0.8005,
  "style_score": 0.6901,
  "label": "Our tools suggest this was likely written by an AI. If you wrote this yourself, you can submit an appeal and we'll take a closer look.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "ff282738-abf4-472f-94f5-bd593348cb1e",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.7759,
  "model_score": 0.8814,
  "style_score": 0.6177,
  "label": "Our tools suggest this was likely written by an AI. If you wrote this yourself, you can submit an appeal and we'll take a closer look.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "d9f083b3-7b37-4611-b78a-840224e3dd73",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.7917,
  "model_score": 0.8816,
  "style_score": 0.6569,
  "label": "Our tools suggest this was likely written by an AI. If you wrote this yourself, you can submit an appeal and we'll take a closer look.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "9a162b9c-6f42-43cd-b886-681dbbd2d7da",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.4197,
  "model_score": 0.3223,
  "style_score": 0.5659,
  "label": "We're not certain about this one. Our tools noticed some patterns that can appear in AI-generated writing, but not enough to say so with confidence. This might simply reflect your writing style. If you wrote this yourself, you can submit an appeal.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "673a3e96-1d6d-4bc8-802d-72db9d23bdfe",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.4999,
  "model_score": 0.4625,
  "style_score": 0.556,
  "label": "We're not certain about this one. Our tools noticed some patterns that can appear in AI-generated writing, but not enough to say so with confidence. This might simply reflect your writing style. If you wrote this yourself, you can submit an appeal.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "543667e7-e5c2-464d-9c13-adc4920f5a7b",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.3219,
  "model_score": 0.2044,
  "style_score": 0.4982,
  "label": "This looks like it was written by a person. Our analysis found nothing that suggests otherwise.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "ae8a2991-5078-4dcc-8278-0b3790517107",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5925,
  "model_score": 0.5943,
  "style_score": 0.5897,
  "label": "We're not certain about this one. Our tools noticed some patterns that can appear in AI-generated writing, but not enough to say so with confidence. This might simply reflect your writing style. If you wrote this yourself, you can submit an appeal.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "61cf6c28-9aea-4609-96b2-3bc7caa4c9b5",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.5227,
  "model_score": 0.4998,
  "style_score": 0.5571,
  "label": "We're not certain about this one. Our tools noticed some patterns that can appear in AI-generated writing, but not enough to say so with confidence. This might simply reflect your writing style. If you wrote this yourself, you can submit an appeal.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "599e705f-bef6-45e0-a5f7-1ffe69c098c6",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.5185,
  "model_score": 0.6401,
  "style_score": 0.3362,
  "label": "We're not certain about this one. Our tools noticed some patterns that can appear in AI-generated writing, but not enough to say so with confidence. This might simply reflect your writing style. If you wrote this yourself, you can submit an appeal.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "9ee6f8ff-7d29-44c8-ab71-5e7c2f74b484",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5883,
  "model_score": 0.5583,
  "style_score": 0.6332,
  "label": "We're not certain about this one. Our tools noticed some patterns that can appear in AI-generated writing, but not enough to say so with confidence. This might simply reflect your writing style. If you wrote this yourself, you can submit an appeal.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "542cec91-4976-4015-923d-aa28c7924eff",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.2667,
  "model_score": 0.0,
  "style_score": 0.6667,
  "label": "This looks like it was written by a person. Our analysis found nothing that suggests otherwise.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "48fba2df-ab7c-4ccb-bd16-db009b5b7d4e",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.2734,
  "model_score": 0.0112,
  "style_score": 0.6667,
  "label": "This looks like it was written by a person. Our analysis found nothing that suggests otherwise.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "5ddd25dd-f9a3-4fd2-a836-ea3913f8a997",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.8652,
  "model_score": 0.9976,
  "style_score": 0.6667,
  "label": "Our tools suggest this was likely written by an AI. If you wrote this yourself, you can submit an appeal and we'll take a closer look.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "8443717f-4ebf-4d0f-a619-23ce6b47bbf5",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.9981,
  "model_score": 0.9969,
  "style_score": 1.0,
  "label": "Our tools suggest this was likely written by an AI. If you wrote this yourself, you can submit an appeal and we'll take a closer look.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "b7797b8b-e81c-4974-97b4-77f918e7c0ba",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.9438,
  "model_score": 0.9064,
  "style_score": 1.0,
  "label": "Our tools suggest this was likely written by an AI. If you wrote this yourself, you can submit an appeal and we'll take a closer look.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 200,
  "content_id": "0c7b9898-74f3-460c-a7fc-10763fa2d9da",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.939,
  "model_score": 0.9876,
  "style_score": 0.8661,
  "label": "Our tools suggest this was likely written by an AI. If you wrote this yourself, you can submit an appeal and we'll take a closer look.",
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "85f1bf74-8e70-475c-82ac-2a1fd361ee7f",
  "creator_id": null,
  "guess": "unsure",
  "confidence": 0.4104,
  "model_score": 0.2395,
  "style_score": 0.6667,
  "label": "We're not certain about this one. Our tools noticed some patterns that can appear in AI-generated writing, but not enough to say so with confidence. This might simply reflect your writing style. If you wrote this yourself, you can submit an appeal.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "cf6e85de-01ce-4fd3-9a4c-bc2592ae6727",
  "creator_id": {
    "id": "x"
  },
  "guess": "human",
  "confidence": 0.2962,
  "model_score": 0.0492,
  "style_score": 0.6667,
  "label": "This looks like it was written by a person. Our analysis found nothing that suggests otherwise.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "789b4ce6-7fec-476a-a596-d44cb7603b70",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2839,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "This looks like it was written by a person. Our analysis found nothing that suggests otherwise.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "e39491d4-243c-427c-be9e-151b4b250c0d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2839,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "This looks like it was written by a person. Our analysis found nothing that suggests otherwise.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "f057c678-91ea-40d4-9cba-68a27a5146de",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2839,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "This looks like it was written by a person. Our analysis found nothing that suggests otherwise.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "9aedd39c-3459-48e4-b6b6-b069da0f704f",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2839,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "This looks like it was written by a person. Our analysis found nothing that suggests otherwise.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "d2cfd6e7-5c04-4186-b123-8f3305fb4a20",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2839,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "This looks like it was written by a person. Our analysis found nothing that suggests otherwise.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "bfc49e6a-07a8-4757-a497-352dcd4a0650",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2839,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "This looks like it was written by a person. Our analysis found nothing that suggests otherwise.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "9f6cd17e-0c76-4a24-91ea-e73c1af5ea75",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2839,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "This looks like it was written by a person. Our analysis found nothing that suggests otherwise.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "d74cb59a-c860-434e-bc88-d8aef44bf424",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2839,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "This looks like it was written by a person. Our analysis found nothing that suggests otherwise.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "dda48ef5-f467-40d0-bb4a-914cf669620e",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2839,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "This looks like it was written by a person. Our analysis found nothing that suggests otherwise.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "47c515ee-90fd-4f0a-88ce-d05338a32523",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2839,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "This looks like it was written by a person. Our analysis found nothing that suggests otherwise.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
