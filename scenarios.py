"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        # Criterion 1: False positives — at most 1 of 10 of my own writing
        # labeled high-confidence AI.
        # ⚠️ These are my own words. Replace any you want with your own writing.
        "name": "my own writing",
        "criterion": 1,
        "texts": [
            "I keep starting sentences with 'I' and then deleting them because it feels too self-centered, which is ironic given that this is literally a journal. Anyway. Today was one of those days where nothing went badly wrong but nothing felt right either. Made coffee, it was fine. Went to class, took notes I'll probably never read. Ate lunch alone outside which I actually liked, there's a spot by the east entrance where nobody goes.",
            "My first year roommate had this habit of leaving cabinet doors open. Every single one. Walk into the kitchen: open. Walk in again ten minutes later: still open. I never said anything about it because I didn't want to be that person, but it drove me insane in this very specific low-grade way. We ended up being pretty good friends. I still think about those cabinets.",
            "The thing about learning to drive late — I was 22 — is that everyone assumes you're incompetent and also slightly broken. Like there's something wrong with you that you didn't do it at 16. There isn't, I just grew up in a city. But the instructor kept asking if I was nervous in this tone that made me more nervous, so. Took three tries to pass the test. Worth it.",
            "Sometimes I read something I wrote two years ago and I genuinely don't recognize the voice. Not in a bad way, just — that's not quite how I'd say it now. The ideas are mostly the same but the rhythm is off. I'm not sure if that's growth or just drift. Probably some of both. I keep old drafts for this reason, it's like looking at photos.",
            "My grandmother made this soup that I've tried to recreate probably fifteen times. I have the recipe — she wrote it down for me before she died, in this careful handwriting that looked nothing like how she talked — but it never tastes the same. I think there's something in it she didn't write down. Or I'm remembering it differently than it was. Both feel true.",
            "I signed up for a 10k in a moment of optimism and have been training for it with a mix of genuine effort and deep regret. The running itself is fine. The waking up at 6am part is less fine. I did four miles yesterday which is the furthest I've gone and I felt pretty good at the end, which either means I'm improving or I'm still going too slow. Probably the second one.",
            "There's a lecture I keep going back to in my head from two years ago, not because it changed my life or anything, just because the professor said something offhand that I keep thinking applies to things. Something about how the map is not the territory. He said it like everyone already knew it but I hadn't heard it before and it sort of reorganized a thing I was thinking about at the time.",
            "I have a complicated relationship with asking for help. Not in a deep psychological way, just — I always think I can figure it out myself, and usually I can, but it takes twice as long. Yesterday I spent forty minutes on a problem before asking and then it was solved in five. The forty minutes wasn't wasted exactly, I understood what I was looking at by the end, but still.",
            "The best part of traveling somewhere new is the first grocery store. Not the famous stuff, not the sights, just — what do people eat here, what does the packaging look like, what's cheap and what's expensive. You can learn a lot about a place from its bread aisle. I always come back with something odd that I then don't know how to use.",
            "I've been trying to write more and think less before writing, which is against my instincts. Usually I draft everything in my head first. The problem is the head-draft is always better than what comes out, so I spend the whole writing session catching up to something that already happened. Writing before thinking is messier but at least the gap isn't there.",
        ],
    },
    {
        # Criterion 2: Score spread — clearly AI and clearly human differ by >= 0.4
        "name": "score spread",
        "criterion": 2,
        "texts": [
            # Clearly AI: formal, structured, predictable prose
            "Effective communication is a cornerstone of successful organizational management. Research consistently demonstrates that teams with strong communication practices outperform those with weaker ones across multiple performance metrics. Organizations should therefore invest in communication training, establish clear feedback mechanisms, and foster a culture of transparency. By implementing these evidence-based strategies, leaders can drive meaningful improvements in team cohesion, productivity, and overall organizational outcomes.",
            # Clearly human: informal, personal, varied
            "okay so I finally figured out what was wrong with the washing machine and it was the most anticlimactic thing — there was a sock stuck in the pump filter. I found this out after watching three YouTube videos and reading a forum post from 2009. The sock had been there for who knows how long. Machine works perfectly now. I feel like I should frame the sock.",
        ],
    },
    {
        # Criterion 3: Label coverage — all three labels (human/unsure/ai) reachable
        "name": "label coverage",
        "criterion": 3,
        "texts": [
            # Targets "ai" label: smooth, predictable, structured AI-generated text
            "Artificial intelligence has emerged as one of the most transformative technologies of the twenty-first century, with applications spanning healthcare, finance, transportation, and education. The rapid advancement of machine learning algorithms has enabled systems to perform tasks that were previously considered exclusively within the domain of human expertise. As these capabilities continue to expand, it becomes increasingly important to consider both the opportunities and the challenges that this technological revolution presents.",
            # Targets "human" label: casual, varied, personal
            "spent the morning trying to remember the name of that movie — you know the one, with the guy, in the building — and eventually gave up and texted my sister who knew immediately. she always knows. it was a pretty good movie actually, I remembered more of it than I thought once I had the title. the ending is weird but I think that's the point.",
            # Targets "unsure" label: mix of structured and informal
            "I've been thinking about how we measure productivity and whether the metrics actually capture what matters. Hours logged, tasks completed, goals hit — these are easy to count. But some of the most important work I've done doesn't show up in any of those numbers. A conversation that changed how someone was thinking about a problem. Reading something slowly. The metrics aren't wrong exactly, they're just measuring a subset.",
        ],
    },
    {
        # Criterion 4: Appeal path — manually tested; placeholder scenario keeps
        # run_eval.py happy. The appeal path requires a live content_id from a
        # prior submission, which can't be known in advance. See README for the
        # manual test procedure and results.
        "name": "appeal path check",
        "criterion": 4,
        "texts": [
            "This text is submitted so we have a fresh content_id to appeal against. The appeal is then made manually using the content_id returned from this submission.",
        ],
    },
    {
        # Criterion 5: Bad input — missing or empty text returns 400, not 500
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"creator_id": "eval_bad_missing"},
            {"text": "   ", "creator_id": "eval_bad_whitespace"},
            {"text": None, "creator_id": "eval_bad_null"},
            {"text": "", "creator_id": "eval_bad_empty2"},
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
