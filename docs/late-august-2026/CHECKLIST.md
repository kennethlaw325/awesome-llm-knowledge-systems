# Late-August 2026 Wave --- Assembly Acceptance Checklist

Reviewer: fresh-context acceptance pass (no prior wave context).
Review date: 2026-08-24. Branch: `late-august-2026-wave`, uncommitted working tree.
Method: `git diff master` plus targeted file reads and greps. No web fetching (facts were
independently verified in the prior adversarial fact-check pass). Read-only on all shipped
surfaces; this file is the only write.

Verdict: **9 of 9 items PASS**, with four findings that need a maintainer decision (one
factual, three cosmetic). None of the four is a BLOCKER for the wave's factual accuracy
except finding F1, which asserts something false about the calendar.

---

## 1. chapters/11-timeline.md --- ten entries, order, placement, sources, ASCII dashes

**PASS**

- Exactly ten added `### ` headings (`git diff master -- chapters/11-timeline.md | grep -c '^+### '` = 10).
- Heading format is `### Month DD, YYYY --- Title` in all ten; ASCII `---`, no Unicode em-dash.
- Chronological in file order: L360 Aug 2, L364 Aug 3, L368 Aug 6 (Paperclip), L372 Aug 6
  (AgentCore), L376 Aug 7, L380 Aug 10, L384 Aug 13, L388 Aug 19 (Skills API), L392 Aug 19
  (Codex), L396 Aug 22. Matches the required 2/3/6/6/7/10/13/19/19/22 sequence.
- All ten sit before `## The Pattern` (chapters/11-timeline.md:402).
- Exactly ten added `- ` lines under `## Sources` (heading at L430; new block L570-L579),
  one per entry, no duplicates. The two `Anthropic` entries are distinct subjects
  (cross-session messaging L573; Skills API release notes L577).
- See finding F3 for a cosmetic ordering nit inside the new Sources block.

## 2. Notion Agent APIs (W11) --- chapter-only

**PASS**

- Present: chapters/08-tools-landscape.md:23 (body paragraph) and :120 (Sources entry 16).
- Absent from timeline: the only `Notion` hits in chapters/11-timeline.md are the
  pre-existing September 2025 Notion 3.0 entry (L69, L71) and its source (L443).
- Absent from README What's-new: the only `Notion` hit in README.md is L225, the chapter
  table row for Ch08 --- outside the What's-new `<details>` block (L7-L40). No bullet exists.

## 3. Chapter integrations all present; ch14 14.7 untouched

**PASS**

| Chapter | Integration | Evidence |
|---|---|---|
| ch03 | KV compaction (arXiv 2608.00902) | chapters/03-context-engineering.md:55 + Sources L108 |
| ch04 | AgentCore Temporal Policies / Dogwood / Runtime Instances | chapters/04-harness-engineering.md:36 + Sources L281 |
| ch04 | Codex as a Platform | chapters/04-harness-engineering.md:167 + Sources L282 |
| ch05 | Paperclip campaign | chapters/05-skill-systems.md:159 + Sources L185 |
| ch05 | Skills API GA + GitHub-hosted skills | chapters/05-skill-systems.md:38, :40 + Sources L186 |
| ch06 | TencentDB Team Memory | chapters/06-agent-memory.md:125 + Sources entry 23, L165 |
| ch07 | MCP roadmap | chapters/07-mcp.md:162-171 (new dated section) + Sources entry 23, L207 |
| ch09 | DeepSeek Harness (dsh) | chapters/09-china-ecosystem.md:65-67 + :119 + Sources L156 |
| ch12 | Muse Glimmer | chapters/12-local-models.md:124 + Sources L165 |
| ch14 | Cross-session messaging | chapters/14-graph-engineering.md:63 + Sources L163 |

ch14 §14.7 zero diff confirmed: `git diff master -U0 -- chapters/14-graph-engineering.md`
returns exactly two hunks, `@@ -62,0 +63,2 @@` (inside §14.2, L37-66) and `@@ -160,0 +163 @@`
(inside `## Sources`, L152+). §14.7 spans L133-L151 --- no hunk touches it.

## 4. glossary.md --- one new entry, alphabetical, ASCII dashes

**PASS**

- Exactly one added entry: **Temporal Policies**, glossary.md:211.
- Alphabetical: Task Budget (L208) -> Temporal Policies (L211) -> Titans (L214). Correct.
- ASCII dashes only; no Unicode em-dash anywhere in glossary.md.

## 5. README.md What's-new block

**PASS**

- Intro (README.md:10) leads with the late-August wave, then names the early-August (Metis)
  and late-July waves as what it builds on.
- Ten new bullets (L12-L21), most-recent-first: Aug 22, 19, 19, 13, 10, 7, 6, 6, 3, 2.
  Dates match the timeline headings one-for-one.
- Codex bullet (L13) says **August 19**. Correct.
- TencentDB bullet (L20) says **August 3** and sits between the Aug 6 AgentCore bullet (L19)
  and the Aug 2 KV-compaction bullet (L21). Correct date order.
- Early-August wave demoted: `*From earlier waves*` marker at L23, immediately followed by
  the three July 29 bullets (Metis, LangChain Deep Agents v0.7, MinIO AIStor Memory).
- Footer: README.md:267 `*Last updated: August 2026*`.
- All nine distinct chapter link paths in the new bullets resolve to files that exist
  (03, 04, 05, 06, 07, 09, 11, 12, 14 --- each verified with `test -f`).

## 6. CHANGELOG.md

**PASS**

- New H3 at CHANGELOG.md:11, `### 2026-08-24 --- Late-August 2026 wave: ...`, directly under
  `## August 2026` (L9) and above the prior `### 2026-08-03` entry (L16). Top of section.
- Body (L13) and Caveats (L14) are consistent with the shipped text:
  - TencentDB v2.0.0 pinned to **August 3, 2026** with the GitHub releases API `published_at`
    and MarkTechPost cited as agreeing; the Aug 13 PRNewswire announcement carried as a
    separate event. **No leftover "no day-precision source exists" claim** --- grep for
    `day-precision` / `no day-precision` returns zero hits across all four shipped surfaces.
  - Codex caveat reflects the primary page's own "Aug 19, 2026" stamp above the author
    byline, and notes that some secondary coverage dates it August 20. Correct framing.
  - dsh sub-agent capability described as **first-party** ("the repository ships
    `@deepseek-ai/dsh-subagent-claude-code` and `@deepseek-ai/dsh-subagent-codex` packages
    ... with press coverage reporting it from that code"). Correct.

## 7. Ripple sweep (defects from re-dated / re-framed facts)

### 7a. "August 20" tied to Codex-as-a-Platform --- **PASS (zero defects)**

Five `August 20` hits across shipped surfaces, all legitimate:
- chapters/05-skill-systems.md:186 --- Anthropic companion blog post, correctly dated Aug 20.
- chapters/08-tools-landscape.md:23, :120 --- Notion Agent APIs, genuinely Aug 20.
- chapters/11-timeline.md:390, :577 --- Anthropic blog / release-note one-day discrepancy,
  explicitly framed as publish lag; timeline entry itself dated Aug 19.
- README.md:14 --- same Anthropic discrepancy, correctly framed.
Codex-related mentions of Aug 20 (chapters/11-timeline.md:578, CHANGELOG.md:14) both appear
only as "some secondary coverage dates it August 20" against a primary Aug 19 --- deliberate
and correct, not a leftover.

### 7b. "early August 2026" / "August 13" as the TencentDB v2.0.0 SHIP date --- **PASS**

- Zero hits for `early August` anywhere in chapters/, glossary.md, README.md, CHANGELOG.md.
- All eight TencentDB/Team Memory locations state Aug 3 as the ship date and Aug 13 as the
  separate PRNewswire announcement: chapters/06-agent-memory.md:125, :165;
  chapters/11-timeline.md:364, :366, :575; README.md:20; CHANGELOG.md:13, :14.

### 7c. Press-coverage-only attribution of the dsh sub-agent capability --- **PASS**

All three descriptions state it as first-party and cite the shipped packages:
chapters/09-china-ecosystem.md:67 ("a first-party feature rather than a press claim"),
chapters/11-timeline.md:386 ("is a first-party feature"), CHANGELOG.md:14 ("is first-party").
The ch09 Sources entry (L156) and ch11 Sources entry (L576) both name the packages and mark
the secondaries as reporting *from that code*.

### 7d. ch04/ch09 pairing language vs. the six-day gap --- **FAIL (one hit)**

dsh = Thursday 2026-08-13; Codex-as-a-Platform = Wednesday 2026-08-19. Six days apart,
different calendar weeks (week of Aug 10 vs week of Aug 17). Audit of every pairing phrase:

| Location | Phrase | Verdict |
|---|---|---|
| chapters/09-china-ecosystem.md:119 | "The timing makes the point sharply: **the same week**, on the other side of the Pacific ..." | **INACCURATE** --- see F1 |
| chapters/09-china-ecosystem.md:119 | "... within days of each other" (same sentence) | Accurate |
| chapters/04-harness-engineering.md:167 | "lands a week after DeepSeek shipped ... **within seven days**" | Accurate (6 days) |
| chapters/11-timeline.md:386 | "the harness layer went open-source on both sides of the Pacific **inside a week**" | Accurate |
| README.md:10 | "goes open-source on both sides of the Pacific **inside a week**" | Accurate |
| CHANGELOG.md:13 | "explicitly paired with the OpenAI beat **one week later**" | Loose rounding of 6 days; defensible, left alone |

### 7e. "Vertex AI" tied to the Skills API --- **PASS**

One `Vertex AI` hit in all shipped surfaces: chapters/11-timeline.md:200, attached to the
Claude Opus 4.7 GA entry (Feb/Mar 2026), unrelated to the Skills API. Every Skills API
availability statement names only "the Claude Platform and Microsoft Foundry"
(chapters/05-skill-systems.md:38, chapters/11-timeline.md:390).

### 7f. Leftover process-meta tokens --- **PASS (zero hits)**

`grep -rn "VENDOR-CLAIM\|PIN-DATE\|COPY-EXACT\|fact-sheet\|\bTODO\b\|\bDRAFT\b"` and
`grep -rnE "\bW(1[01]?|[2-9])\b"` over chapters/, glossary.md, README.md, CHANGELOG.md both
return zero matches. (docs/ planning files legitimately retain these; not flagged.)

## 8. Sources hygiene

**PASS**

- Numbered-list chapters continue without gap or duplicate: ch06 ends 22 -> new 23 (L165);
  ch07 ends 22 -> new 23 (L207); ch08 ends 15 -> new 16 (L120).
- Dash-list chapters (03, 04, 05, 09, 11, 12, 14) match the surrounding bullet format;
  8 added bullets across 03/04/05/09/12/14 plus 10 in ch11, no duplicate subjects.
- No URL contains `...` or other truncation:
  `grep -rn 'https\?://[^)" ]*\.\.\.'` returns zero hits.
- No Unicode em-dash introduced in chapters/ or glossary.md. The single em-dash in the tree
  is chapters/11-timeline.md:11 (pre-existing, exempt). README.md and CHANGELOG.md use
  Unicode em-dashes throughout as their pre-existing house style; the new bullets match it.
- See finding F4 for a low-specificity-citation note.

## 9. Register spot-check (ten timeline entries + README bullets, read end-to-end)

**PASS**

- All ten entries are complete: each opens with the event, carries specifics, and closes with
  the standard "The beat that matters for this guide:" clause plus a chapter cross-reference.
  None reads unfinished or truncated.
- Vendor-claim attribution is consistently explicit and never stated as finding: Meta's DFlash
  and Gemma4/Qwen3.6 comparisons (chapters/11-timeline.md:382, chapters/12-local-models.md:124),
  OpenAI's ARC-AGI-3 13.3%->38.3% and production users (chapters/11-timeline.md:394,
  chapters/04-harness-engineering.md:167), every Team Memory governance mechanism
  (chapters/11-timeline.md:366, chapters/06-agent-memory.md:125), the >1.7M Paperclip counter
  framed as aggregate-not-unique (chapters/11-timeline.md:370), and the dsh star/fork counts
  carried with a GitHub-API check date and a re-check note.
- Cross-entry consistency holds on the substantive claims: the Aug 6 AgentCore entry's 14-day
  session is cross-referenced *against* (not as corroboration of) the June 18 Terminal-Bench
  null result; the Aug 7 cross-session-messaging entry and Ch14 both state outright that
  Anthropic never uses the phrase "graph engineering".
- Two internal wording contradictions found, both cosmetic --- see F2 and F3.

---

## Findings needing a maintainer decision

### F1 --- FACTUAL. "the same week" is wrong by the calendar. (most severe)

`chapters/09-china-ecosystem.md:119`:

> The timing makes the point sharply: the same week, on the other side of the Pacific,
> OpenAI open-sourced the execution engine behind Codex (Chapter 4) ...

dsh shipped Thursday August 13; Codex-as-a-Platform published Wednesday August 19. Those are
different calendar weeks. Every other pairing phrase in the wave already uses a correct form
("within seven days", "inside a week", "within days of each other"), so this is the single
outlier and the fix is one phrase.

**Suggested minimal fix:** `the same week,` -> `days later,` (or `the same month,`). The rest
of the sentence already says "within days of each other" and needs no change.

### F2 --- WORDING. "the week before" contradicts "twelve days earlier" in the same paragraph.

Skills API GA = Wednesday August 19; GitHub-hosted skills = Friday August 7. That is twelve
days and two calendar weeks apart, and the body text says so --- but the heading and the ch05
prose both say "the week before":

- `chapters/11-timeline.md:388` heading: "... with GitHub-Hosted Skills the Week Before",
  while `:390` body says "Twelve days earlier, on **August 7**".
- `chapters/05-skill-systems.md:40`: "A second change landed the week before, on **August 7**".
- `README.md:14` already says "twelve days earlier" --- correct.

Self-contradicting within one paragraph. **Suggested minimal fix:** heading -> "with
GitHub-Hosted Skills Twelve Days Earlier" (or "Earlier the Same Month"); ch05:40 -> "A second
change landed twelve days earlier, on **August 7**".

### F3 --- COSMETIC. TencentCloud Sources bullet sits at its old (Aug 13) position.

The ten new bullets at `chapters/11-timeline.md:570-579` run Aug 2, 6, 6, 7, 10, **3**, 13, 19,
19, 22. The TencentCloud entry (L575) sits between Meta/Aug 10 (L574) and DeepSeek/Aug 13
(L576) --- exactly where an Aug-13-dated entry would have gone before the fact-check re-dated
it to Aug 3. A residual of the re-date; the entry text itself is correct.

Low severity: the pre-existing Sources list is only loosely chronological already (L563 July 28
precedes L564 July 20). **Suggested fix if desired:** move L575 to sit directly after L570
(the Aug 2 arXiv entry).

### F4 --- COSMETIC. Bare-domain secondary citations.

Four secondaries in `chapters/09-china-ecosystem.md:156` (`https://cryptobriefing.com`,
`https://mindstudio.ai/blog`, `https://digitalapplied.com`, `https://flowtivity.ai`) and one in
`chapters/12-local-models.md:165` (`https://www.ghacks.net`) cite a domain rather than an
article URL. Not truncation --- nothing was cut --- but a reader cannot verify the specific
claim from them. Both entries carry the load-bearing facts on primary sources (GitHub API,
research.meta.ai), so this affects verifiability of the framing only.

### Non-issue noted for the record

`docs/late-august-2026/per-chapter-changes.md:21` says ch05 gets "three bullets" of sources;
the shipped file adds two (Zenity Labs, Anthropic), with the Anthropic bullet carrying all
three Anthropic URLs inline. Planning-doc bookkeeping, not a shipped-text gap --- every source
named in the plan is present.

### Cosmetic, out of checklist scope

`chapters/12-local-models.md:116` heading still reads "2026: Local Models Get an OS-Native API
and Vendor QAT" while the section intro at L118 now says "Three 2026 releases". Muse Glimmer is
neither an OS-native API nor a QAT release. Pre-existing heading, correctly left untouched by a
surgical integration; flagged only so a maintainer can decide.
