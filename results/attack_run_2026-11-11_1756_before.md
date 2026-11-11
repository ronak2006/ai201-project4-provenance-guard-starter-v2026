# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-11 17:56
- Auto-marked BROKE (5xx, crash, no response): **4**
- Left for you to judge: **52**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `e07ca813-0437-4579-b3b7-cf7c25896dc4` | human | 0.343 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `04e23749-f108-46f1-9042-6fe8333c46c7` | unsure | 0.567 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `adced2e9-727f-43b5-b1b0-506fe058a04a` | unsure | 0.621 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `c7c310e8-3d0f-4fc1-8eac-4fb4a11b5d97` | unsure | 0.606 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `2689b9e5-e4ca-4f06-9046-38b5b8627a0b` | unsure | 0.386 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `774a8fb7-0af4-4733-8910-74a3efe4f6a4` | unsure | 0.556 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `ef6d0676-194f-46c5-9833-37ea65676e95` | unsure | 0.551 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `da65a095-acb2-4931-8b8f-e8192f6c1069` | unsure | 0.384 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `d4dc96e6-97b1-45ff-821f-50d5f79ca9ad` | unsure | 0.642 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `3bb9f4e0-8e6b-4fd8-9ba1-de5b9f7c17f7` | ai | 0.907 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `9b47f9f1-1e1e-431c-8d5b-a14eced9e749` | unsure | 0.621 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `29eeb8ff-4386-4f4d-8f0f-bdb06423df30` | ai | 0.716 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `5855880f-83a0-4e22-bc99-c802ecec03e2` | ai | 0.754 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `1379a403-3981-400a-8bb3-cef3699dede4` | ai | 0.749 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `72942954-0e31-4613-bb25-9ef17f283337` | ai | 0.756 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `48569ed7-5b2d-46ac-b58f-88bbff480a70` | ai | 0.776 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `6b92d59a-042b-4f18-967e-5ae53525acb0` | ai | 0.792 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `7094bec3-13b5-4aa8-a8bb-30f8943f2e76` | unsure | 0.420 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `3b179d63-e2b6-4198-a846-fda65609feba` | unsure | 0.500 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `27e11826-3b52-47c4-8b1e-096d465cc368` | human | 0.322 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `74338635-dd95-495f-8d2f-cb1b232f4f5c` | unsure | 0.593 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `1f0e8224-0011-4f4e-9d2b-3e8af6abf37e` | unsure | 0.523 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `68ab3da7-a63e-4e7f-829a-247cebce9b78` | unsure | 0.518 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `178fcc1b-b8f4-4516-9f6a-4ef422d24403` | unsure | 0.588 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `35c76e52-1abf-49b2-834b-4c4494c05812` | human | 0.267 |  |
| MF04 | malformed | text is only punctuation | 200 | `cc4bd170-7201-4967-9e4f-63875be02367` | human | 0.273 |  |
| MF05 | malformed | text is a very long single word | 200 | `78c6be69-deb6-439e-b012-f95892e5d157` | ai | 0.865 |  |
| MF06 | malformed | text is emoji only | 200 | `d2bb6cd2-92b6-4be1-a6f9-4572eed0cf9c` | ai | 0.998 |  |
| MF07 | malformed | text is right-to-left script | 200 | `401df1cc-1a6c-4d22-81e5-e7f183540dbf` | ai | 0.944 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `8bdbbec5-4bf4-4d9d-aeab-9d1c3c373e42` | ai | 0.939 |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `816f3900-4830-479b-b304-02e132e66853` | unsure | 0.410 |  |
| RQ03 | malformed | text is a number | 500 | `—` | — | — | BROKE |
| RQ04 | malformed | text is a list | 500 | `—` | — | — | BROKE |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `4fc26307-0722-44ed-b8d3-1b4921d79121` | human | 0.296 |  |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 500 | `—` | — | — | BROKE |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e0b825d9-0cd2-4ed7-8ecc-97e814dd570a` | human | 0.284 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ba7af89e-84a0-49c9-9655-1e5d2b336a32` | human | 0.284 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9ecb916a-ad77-48f5-bb57-500b54a6f8ce` | human | 0.284 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `693549bf-ebc3-4ce0-98a1-90965c6c26be` | human | 0.284 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `16eb0294-f1b8-459b-b12e-07f316ebfd35` | human | 0.284 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `75b34844-ad01-4761-b91e-496510290747` | human | 0.284 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `73da9c7f-c382-42ee-a096-84b26e9c2892` | human | 0.284 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7cd5a5b8-3581-460f-9421-9a61800f4866` | human | 0.284 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `89b1e5bf-54e7-4e67-bdc8-851607742c04` | human | 0.284 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1486f88e-710b-468e-8471-a547dadea87f` | human | 0.284 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 4 | 16 |
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
  "content_id": "e07ca813-0437-4579-b3b7-cf7c25896dc4",
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
  "content_id": "04e23749-f108-46f1-9042-6fe8333c46c7",
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
  "content_id": "adced2e9-727f-43b5-b1b0-506fe058a04a",
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
  "content_id": "c7c310e8-3d0f-4fc1-8eac-4fb4a11b5d97",
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
  "content_id": "2689b9e5-e4ca-4f06-9046-38b5b8627a0b",
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
  "content_id": "774a8fb7-0af4-4733-8910-74a3efe4f6a4",
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
  "content_id": "ef6d0676-194f-46c5-9833-37ea65676e95",
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
  "content_id": "da65a095-acb2-4931-8b8f-e8192f6c1069",
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
  "content_id": "d4dc96e6-97b1-45ff-821f-50d5f79ca9ad",
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
  "content_id": "3bb9f4e0-8e6b-4fd8-9ba1-de5b9f7c17f7",
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
  "content_id": "9b47f9f1-1e1e-431c-8d5b-a14eced9e749",
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
  "content_id": "29eeb8ff-4386-4f4d-8f0f-bdb06423df30",
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
  "content_id": "5855880f-83a0-4e22-bc99-c802ecec03e2",
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
  "content_id": "1379a403-3981-400a-8bb3-cef3699dede4",
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
  "content_id": "72942954-0e31-4613-bb25-9ef17f283337",
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
  "content_id": "48569ed7-5b2d-46ac-b58f-88bbff480a70",
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
  "content_id": "6b92d59a-042b-4f18-967e-5ae53525acb0",
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
  "content_id": "7094bec3-13b5-4aa8-a8bb-30f8943f2e76",
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
  "content_id": "3b179d63-e2b6-4198-a846-fda65609feba",
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
  "content_id": "27e11826-3b52-47c4-8b1e-096d465cc368",
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
  "content_id": "74338635-dd95-495f-8d2f-cb1b232f4f5c",
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
  "content_id": "1f0e8224-0011-4f4e-9d2b-3e8af6abf37e",
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
  "content_id": "68ab3da7-a63e-4e7f-829a-247cebce9b78",
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
  "content_id": "178fcc1b-b8f4-4516-9f6a-4ef422d24403",
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
  "content_id": "35c76e52-1abf-49b2-834b-4c4494c05812",
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
  "content_id": "cc4bd170-7201-4967-9e4f-63875be02367",
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
  "content_id": "78c6be69-deb6-439e-b012-f95892e5d157",
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
  "content_id": "d2bb6cd2-92b6-4be1-a6f9-4572eed0cf9c",
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
  "content_id": "401df1cc-1a6c-4d22-81e5-e7f183540dbf",
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
  "content_id": "8bdbbec5-4bf4-4d9d-aeab-9d1c3c373e42",
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
  "content_id": "816f3900-4830-479b-b304-02e132e66853",
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
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;int&#39; object has no attribute &#39;strip&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=ye",
  "verdict": "BROKE"
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;list&#39; object has no attribute &#39;strip&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=y",
  "verdict": "BROKE"
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
  "content_id": "4fc26307-0722-44ed-b8d3-1b4921d79121",
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
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;list&#39; object has no attribute &#39;get&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes",
  "verdict": "BROKE"
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
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;dict&#39; object has no attribute &#39;strip&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=y",
  "verdict": "BROKE"
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "e0b825d9-0cd2-4ed7-8ecc-97e814dd570a",
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
  "content_id": "ba7af89e-84a0-49c9-9655-1e5d2b336a32",
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
  "content_id": "9ecb916a-ad77-48f5-bb57-500b54a6f8ce",
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
  "content_id": "693549bf-ebc3-4ce0-98a1-90965c6c26be",
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
  "content_id": "16eb0294-f1b8-459b-b12e-07f316ebfd35",
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
  "content_id": "75b34844-ad01-4761-b91e-496510290747",
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
  "content_id": "73da9c7f-c382-42ee-a096-84b26e9c2892",
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
  "content_id": "7cd5a5b8-3581-460f-9421-9a61800f4866",
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
  "content_id": "89b1e5bf-54e7-4e67-bdc8-851607742c04",
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
  "content_id": "1486f88e-710b-468e-8471-a547dadea87f",
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
