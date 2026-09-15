# Mid-September 2026 Wave --- Assembly Acceptance Checklist

Reviewer: Codex, fresh-context acceptance reviewer; no drafting involvement.  
Review date: 2026-09-15.  
Branch: `mid-september-2026-wave`, uncommitted working tree.  
Method: `git diff master`, targeted reads, greps, and read-only structural checks. No web fetching or file modifications. HEAD and master both resolve to `3ec9afbf79ed563a6898a3c65ec7e7b872700c3c`. Citations below refer to current working-tree lines unless explicitly prefixed with `master:`.

**Verdict: 4 of 10 items PASS; 5 PARTIAL; 1 FAIL. Findings: 0 BLOCKER, 3 MAJOR, 3 MINOR.**

## 1. chapters/11-timeline.md --- entries, chronology, placement, sources

**PARTIAL**

- The equivalent of `git diff master -- chapters/11-timeline.md | grep -c '^+### '` returns **10**.
- Nine headings follow the required single-day format. `chapters/11-timeline.md:364` uses `July 29-30, 2026`, a date-range exception. See F6.
- The ten additions are chronological, including their placement among existing entries:

| Date and event | Heading | Matching new Sources bullet |
|---|---|---|
| July 29 --- OpenRouter | `chapters/11-timeline.md:360` | `chapters/11-timeline.md:620` |
| July 29-30 --- three memory papers | `chapters/11-timeline.md:364` | `chapters/11-timeline.md:621` |
| July 30 --- Memory Bank GA | `chapters/11-timeline.md:368` | `chapters/11-timeline.md:622` |
| August 20 --- StateMemBench | `chapters/11-timeline.md:408` | `chapters/11-timeline.md:623` |
| September 1 --- Falcon Guardian and AIR | `chapters/11-timeline.md:416` | `chapters/11-timeline.md:624` |
| September 3 --- GPT-6 Astra | `chapters/11-timeline.md:420` | `chapters/11-timeline.md:625` |
| September 4 --- memory portability | `chapters/11-timeline.md:424` | `chapters/11-timeline.md:626` |
| September 10 --- threat report | `chapters/11-timeline.md:428` | `chapters/11-timeline.md:627` |
| September 11 --- Salesforce | `chapters/11-timeline.md:432` | `chapters/11-timeline.md:628` |
| September 15 --- survival gate | `chapters/11-timeline.md:436` | `chapters/11-timeline.md:629` |

- All ten precede `## The Pattern` at `chapters/11-timeline.md:442`.
- `## Sources` starts at `chapters/11-timeline.md:470`. The diff contains **11 added source-bullet lines**: ten new bullets plus replacement of the existing DeepSeek Harness bullet at `chapters/11-timeline.md:616`.
- URL-truncation grep returns **zero matches**, including the complete new Sources block at `chapters/11-timeline.md:620-629`.

## 2. Chapter integrations and required caveats

**PARTIAL**

Every planned subject is present. One detailed OpenRouter ranking remains unsupported by the recorded verification, despite being removed from the corresponding timeline account. See F1.

| Integration | Working-tree evidence and caveat check |
|---|---|
| Ch01 --- gate outcome | `chapters/01-evolution.md:173` carries circulation survived, distinct-layer status unproved, and exclusion from numbered generations. Its universal vendor-absence wording needs F2. |
| Ch02 --- portability strengthens structured storage | `chapters/02-knowledge-layer.md:101` adds the model-swap argument and 48 synthetic cases; source `chapters/02-knowledge-layer.md:224` names both authors and explicitly calls the result small-sample and unreplicated. |
| Ch03 --- revised context guidance | `chapters/03-context-engineering.md:71` attributes the 80%+ prompt reduction and coding-evaluation result to Anthropic's own evaluations; matching source at `chapters/03-context-engineering.md:113`. |
| Ch03 --- heterogeneous working memory | `chapters/03-context-engineering.md:73` states **55 trajectories**, four object categories, and an open empirical finding; matching source at `chapters/03-context-engineering.md:114`. |
| Ch04 --- `auto` permission policy | `chapters/04-harness-engineering.md:38` carries September 10, per-call outcomes, event fields, reason codes, and explicit single-source attribution to Anthropic documentation; source at `chapters/04-harness-engineering.md:292`. |
| Ch04 --- Astra | `chapters/04-harness-engineering.md:63` carries September 3, the Critical designation, enterprise default, refusal contract, Daybreak path, and monitorability regression. Benchmarks are explicitly OpenAI's and measured without production safeguards; source at `chapters/04-harness-engineering.md:291`. |
| Ch04 --- TTHE and evaluation critique | `chapters/04-harness-engineering.md:103` carries both papers, matched-budget and overfitting objections, the negative empirical result, and explicitly says **“The critique does not name TTHE.”** Sources at `chapters/04-harness-engineering.md:293-294`. |
| Ch04 --- Google and Salesforce | Both integrations appear at `chapters/04-harness-engineering.md:225`: Google's July 30 GA, seven-day runtime and native IAM identity; Salesforce's September 11 announcement, three runtime components, and Hunter's November GA plan. Vendor claims and pilot status are explicit. Sources at `chapters/04-harness-engineering.md:295-296`. |
| Ch05 --- `ant apply` | `chapters/05-skill-systems.md:132` pins September 3 and CLI v1.30.0, explains the resolved-commit lock and `--upgrade`, cites vendor documentation, and distinguishes mitigation from a solution to external-content execution. Source at `chapters/05-skill-systems.md:193`. |
| Ch05 --- fourth security beat | `chapters/05-skill-systems.md:165` carries Falcon Guardian, absence of efficacy figures, AIR's funding and ecosystem counts, brand impersonation, and AIR's unpublished methodology. Sources at `chapters/05-skill-systems.md:191-192` distinguish September 1 announcement from September 3 coverage. |
| Ch06 --- filesystem memory | `chapters/06-agent-memory.md:57` includes the three roles, cheaper retrieval, organizational erosion, absence of answer-quality improvement, and unreplicated status; source at `chapters/06-agent-memory.md:178`. |
| Ch06 --- MemTxn and independent MemTX | `chapters/06-agent-memory.md:83` states **60 accepted / 179 rejected**, small validation set, three mechanisms, and independent teams. Source `chapters/06-agent-memory.md:179` explicitly records no author overlap. |
| Ch06 --- Memory Decoder | `chapters/06-agent-memory.md:91` carries 6.9B plus 410M, 300B training tokens, 29.86 to 37.34 versus 37.24, 39% fewer parameters, and self-reported figures; source at `chapters/06-agent-memory.md:180`. |
| Ch06 --- portability | `chapters/06-agent-memory.md:117` carries **48 synthetic cases, two authors**, write-time loss, raw-source retention, and the corrected qualification that 34/48 repair success applies to **one migration direction**; source at `chapters/06-agent-memory.md:181`. |
| Ch06 --- StateMemBench | `chapters/06-agent-memory.md:121` now introduces five results. `chapters/06-agent-memory.md:131` adds recency, 234 scenarios, the distinct comparators behind the two multiples, context-controlled gains, and unreplicated figures; source at `chapters/06-agent-memory.md:182`. |
| Ch06 --- managed-memory category | `chapters/06-agent-memory.md:137` distinguishes July 30, 2026 GA from July 2025 preview, attributes Google's capabilities, and correctly places TencentDB four days later; source at `chapters/06-agent-memory.md:183`. |
| Ch07 --- per-call authorization | `chapters/07-mcp.md:154` carries the September 10 policy, vendor attribution and Ch04 cross-reference; source at `chapters/07-mcp.md:210`. |
| Ch09 --- ByteDance reorganization | `chapters/09-china-ecosystem.md:35` attributes August 24 reporting to 36kr and preserves the distinction between a reported launch timeframe and company confirmation; source at `chapters/09-china-ecosystem.md:177`. |
| Ch09 --- Qwen-Scope | `chapters/09-china-ecosystem.md:51` and source `chapters/09-china-ecosystem.md:175` carry the corrected **1.7B to 35B** range, 14 groups, seven variants, and per-backbone widths instead of the unsupported aggregate feature count. |
| Ch09 --- Ascend report | `chapters/09-china-ecosystem.md:71` preserves anonymous-source attribution, non-confirmation, inference-only use and supply constraints. `chapters/09-china-ecosystem.md:178` explicitly identifies secondary coverage as the source actually read. |
| Ch09 --- dsh refresh | `chapters/09-china-ecosystem.md:75` and `chapters/09-china-ecosystem.md:174` preserve both dated star/fork snapshots. |
| Ch09 --- Hy4 | `chapters/09-china-ecosystem.md:97` attributes blind-evaluation scores, throughput and self-optimization to Tencent; source at `chapters/09-china-ecosystem.md:176`. |
| Ch09 --- OpenRouter | `chapters/09-china-ecosystem.md:131` keeps the percentages separate and secondary-sourced. The named September 1 ranking and its source treatment at `chapters/09-china-ecosystem.md:180` need F1. |
| Ch09 --- distillation | `chapters/09-china-ecosystem.md:135-137` and source `chapters/09-china-ecosystem.md:179` consistently identify allegations by a competitor without independent adjudication. |
| Ch12 --- Ollama desktop integrations | `chapters/12-local-models.md:102` carries v0.33.0 / August 21 and v0.34.0 / September 5; matching release sources at `chapters/12-local-models.md:159-160`. |
| Ch14 --- restructure | Opening, delegation, production precedent, headcount, course, obituary correction, layer distinction, Chinese-language uncertainty and scorecard are present at `chapters/14-graph-engineering.md:7`, `:67`, `:69`, `:71`, `:73`, `:91`, `:93`, `:131`, `:145`, and `:164-181`. See item 3. |

The original **secondary-only distillation requirement is superseded**, rather than accidentally omitted. The fact sheet labels itself historical at `docs/mid-september-2026/fact-sheet.md:3`; the later checker records a successful primary fetch and explicitly instructs direct attribution at `docs/mid-september-2026/fact-check-findings.md:212-243`. Restoring the obsolete caveat would introduce an error.

## 3. Chapter 14 restructure and verdict alignment

**PARTIAL**

- The opening dates the original assessment to July and the check to September 15; “two weeks old” is historical, not present-tense: `chapters/14-graph-engineering.md:7-11`.
- Codex is pinned to **rust-v0.142.0, June 22, 2026**, and prompt policy is distinguished from enforced authorization: `chapters/14-graph-engineering.md:67-69`.
- Anthropic's June 13, 2025 production account and internal evaluation are present at `chapters/14-graph-engineering.md:71`; headcount's **16 departments / 172 skills** and stale description-field counts are distinguished at `chapters/14-graph-engineering.md:73`.
- Section 14.3 correctly identifies the disputed obituary as **loop engineering's**, with secondary attribution and SmartScope's July 20 assessment boundary: `chapters/14-graph-engineering.md:93`.
- Exact comparison returned:

  ```text
  CORE master137-146 equals working153-162 = True
  ```

  Thus the operative July prose, four signals and “If those arrive” consequence remain verbatim at `chapters/14-graph-engineering.md:153-162`. The entire section is **not** deletion-free: its heading, introductory sentence and former closing paragraph were changed (`master:chapters/14-graph-engineering.md:133`, `:135`, `:148`). Those changes sit outside the preserved core; the original gate criteria were not rewritten.
- The dated scorecard is **NOT-MET / MET weakly / MET retrospectively / MET**, matching `docs/mid-september-2026/survival-gate-verdict.md:66-70` and `chapters/14-graph-engineering.md:170-173`.
- The aggregation explanation is explicit at `chapters/14-graph-engineering.md:175`. The interim-date arithmetic at `chapters/14-graph-engineering.md:166` is wrong; see F5.

### Verdict quotations

| Surface | Exact verdict wording |
|---|---|
| Decision record | “**SURVIVES the circulation test; distinct-layer status unproved.**” --- `docs/mid-september-2026/survival-gate-verdict.md:66` |
| Ch14 opening | “The term survived the circulation test the gate actually stated; its status as a distinct engineering layer remains unproved.” --- `chapters/14-graph-engineering.md:9` |
| Ch14 conclusion | “Verdict, September 15, 2026: the term survived the circulation test; its status as a distinct engineering layer is unproved.” --- `chapters/14-graph-engineering.md:179` |
| Ch01 | “The verdict recorded there is that the term survived as a contested name for multi-agent coordination and that its status as a distinct layer is unproved, so it stays outside the numbered generations.” --- `chapters/01-evolution.md:173` |
| Glossary | “The guide's September 15, 2026 survival check found the term still circulating --- independent essays, a paid course teaching the agent-organization sense --- but no vendor using it in product vocabulary, and recorded the verdict as circulation survived, distinct-layer status unproved.” --- `glossary.md:75` |
| README TL;DR | “Six weeks later came a fifth claim, *graph engineering*, put under a survival gate that was checked on September 15, 2026: it remained in circulation as a contested name for multi-agent coordination, and a distinct fifth layer is unproved” --- `README.md:52` |
| README Evolution | “Graph engineering, the July 2026 claim covered in [Ch14](chapters/14-graph-engineering.md), would wrap even that -- the wiring of multiple loops into a designed organization -- and the September 15, 2026 check of that chapter's own survival gate left the question open on purpose: the term circulates, but no vendor uses it in product vocabulary, two vendors shipped the governance it names without it, and its status as a real fifth layer rather than three-year-old practice with a new name (LangChain's counter) is unproved.” --- `README.md:113` |
| README chapter row | “The contested fifth claim -- wiring the organization of agents; it survived its September 2026 circulation gate and is still unproved as a distinct layer” --- `README.md:237` |

The substantive verdict is aligned. The scoped evidence limitation in the scorecard does not survive into every summary's vendor-absence claim; see F2.

## 4. glossary.md --- new entries

**PASS**

- Exactly two new entries:
  - **Sparse Autoencoder (SAE)** at `glossary.md:203`, between **Skill Supply-Chain Attack** (`glossary.md:200`) and **State Supersession** (`glossary.md:206`).
  - **State Supersession** at `glossary.md:206`, between **Sparse Autoencoder (SAE)** (`glossary.md:203`) and **System Prompt** (`glossary.md:209`).
- Both follow the adjacent bold-term / definition-paragraph format, with chapter references: `glossary.md:204`, `glossary.md:207`.
- Decoded Unicode counts: **U+2014 = 0; U+2013 = 0**, unchanged from master.

## 5. README.md What's-new block

**PASS**

- Summary says September 2026 at `README.md:8`.
- Introduction leads with this wave and names late-August and early-August predecessors at `README.md:10`.
- Exactly ten new bullets, most-recent-first. Dates match the timeline one-for-one:

| Date | README bullet | Timeline heading |
|---|---|---|
| September 15 | `README.md:12` | `chapters/11-timeline.md:436` |
| September 11 | `README.md:13` | `chapters/11-timeline.md:432` |
| September 10 | `README.md:14` | `chapters/11-timeline.md:428` |
| September 4 | `README.md:15` | `chapters/11-timeline.md:424` |
| September 3 | `README.md:16` | `chapters/11-timeline.md:420` |
| September 1 | `README.md:17` | `chapters/11-timeline.md:416` |
| August 20 | `README.md:18` | `chapters/11-timeline.md:408` |
| July 30 | `README.md:19` | `chapters/11-timeline.md:368` |
| July 29-30 | `README.md:20` | `chapters/11-timeline.md:364` |
| July 29 | `README.md:21` | `chapters/11-timeline.md:360` |

- The earlier-wave marker is at `README.md:23`; the August bullets follow it at `README.md:25-34`.
- The July 17-22 announcement now carries “checked September 15, 2026: circulation survived, distinct-layer status unproved” at `README.md:40`.
- Footer is exactly `*Last updated: September 2026*` at `README.md:273`.
- `Test-Path -PathType Leaf`, the PowerShell equivalent of `test -f`, returned **True for all eight distinct chapter paths** linked from `README.md:12-21`: Ch01, Ch02, Ch04, Ch05, Ch06, Ch09, Ch11 and Ch14.
- This structural PASS does not clear the wording findings in F2 and F4.

## 6. CHANGELOG.md

**FAIL**

- Correct placement: `## September 2026` at `CHANGELOG.md:9`, one H3 dated 2026-09-15 at `CHANGELOG.md:11`, before August at `CHANGELOG.md:15`.
- The body overclaims that every timeline item was checked against its primary source, contradicting its own secondary-only caveat. See F3.
- The remaining Caveats passage at `CHANGELOG.md:13` was checked against the described chapters:

| Caveat | Matching shipped evidence |
|---|---|
| Split gate; retrospective production case; weak course; Chinese continuation unverified | `chapters/14-graph-engineering.md:145`, `:170-179` |
| Vendor-documentation sourcing for `auto` and `ant apply` | `chapters/04-harness-engineering.md:38`; `chapters/05-skill-systems.md:132` |
| OpenRouter measurements separate and secondary-only | `chapters/09-china-ecosystem.md:131`, `:180` |
| Ascend report unconfirmed and indirectly sourced | `chapters/09-china-ecosystem.md:71`, `:178` |
| Distillation figures from primary, still allegations | `chapters/09-china-ecosystem.md:135-137`, `:179` |
| Astra enterprise default, pricing-source correction and unavailable context/output specifications | `chapters/04-harness-engineering.md:63`; `chapters/11-timeline.md:625` |
| AIR methodology unpublished; CrowdStrike efficacy unspecified | `chapters/05-skill-systems.md:165` |
| Salesforce vendor claims and Hunter pilot | `chapters/04-harness-engineering.md:225` |
| Google and Tencent capability attribution | `chapters/06-agent-memory.md:137`; `chapters/09-china-ecosystem.md:97` |
| Small or unreplicated research bases | `chapters/03-context-engineering.md:73`; `chapters/06-agent-memory.md:83`, `:117`, `:131` |
| Doubao launch reported, not company-confirmed | `chapters/09-china-ecosystem.md:35` |

## 7. Ripple sweep

**PARTIAL**

- Required process-token regex over README, CHANGELOG, glossary and all chapters returned **zero matches**, exit code **1**.
- The old gate's “as of writing: none found” survives only within the explicitly preserved July passage at `chapters/14-graph-engineering.md:158`, contextualized at `chapters/14-graph-engineering.md:151`. The historical July announcement at `README.md:40` also carries the new outcome.
- Newly categorical vendor-absence claims need F2.
- Ch05's three-disclosure sentence still refers to the first three incidents, before the fourth commercial beat. However, June 22 to August 6 is **45 days**, not exactly six weeks: `chapters/05-skill-systems.md:157-161`. See F5.
- The named September OpenRouter snapshot survived only in Ch09 after the timeline was narrowed; see F1.

| Cross-file fact | Result |
|---|---|
| Astra launch: September 3 | Consistent at `chapters/04-harness-engineering.md:63`, `chapters/11-timeline.md:420-422`, `README.md:16`. |
| Astra benchmarks | Shared values agree: ExploitBench 100% / 78.5%, ExploitGym 42.4%, SRE-Bench 88.0% first attempt. Ch04 and Ch11 also carry 99.2% within four; README omits it rather than contradicting it. Same citations as above. |
| dsh: 224,004 / 26,637, checked September 15 | Consistent at `chapters/09-china-ecosystem.md:75`, `:174`, `chapters/11-timeline.md:398`, `:616`. August 24's 190,630 / 21,319 is preserved separately. |
| Codex release | `rust-v0.142.0`, June 22, 2026 agrees at `chapters/14-graph-engineering.md:67`, `:199`, `chapters/11-timeline.md:438`, `:629`. |
| headcount | 16 departments / 172 skills agrees at `chapters/14-graph-engineering.md:73`, `:200`; 15+ / 125+ is explicitly identified as stale metadata. |
| Memory Bank GA | July 30 agrees at `chapters/04-harness-engineering.md:225`, `chapters/06-agent-memory.md:137`, `chapters/11-timeline.md:368-370`, `README.md:19`. |

## 8. Sources hygiene and line endings

**PASS**

### List continuity

- **Ch02 is not numbered.** Master and working tree both use dash bullets. The last old entry is OpenSPG/KAG at `chapters/02-knowledge-layer.md:223`; the new Goyal/Ray entry follows at `chapters/02-knowledge-layer.md:224`. A last-old/first-new number pair is inapplicable.
- **Ch06:** old **23** at `chapters/06-agent-memory.md:177`; first new **24** at `:178`; additions continue through **29** at `:183`. Full sequence is 1-29, without gaps or duplicates.
- **Ch07:** old **23** at `chapters/07-mcp.md:209`; new **24** at `:210`. Full sequence is 1-24, without gaps or duplicates.
- New dash-list entries match their surroundings: `chapters/03-context-engineering.md:113-114`, `chapters/04-harness-engineering.md:291-296`, `chapters/05-skill-systems.md:191-193`, `chapters/09-china-ecosystem.md:175-180`, `chapters/11-timeline.md:620-629`, `chapters/12-local-models.md:159-160`, `chapters/14-graph-engineering.md:197-204`.
- Exact duplicate source bullets: **zero** in every changed chapter. Subject inspection found no duplicate new event entries; separate releases, distinct Anthropic features, and MemTxn/MemTX are legitimately separate subjects.

### Unicode and checkout format

Counts were performed on decoded UTF-8 characters for **U+2014** and **U+2013**, not UTF-8 bytes.

| Files | Master em/en | Working em/en | Introduced |
|---|---:|---:|---:|
| Ch01, Ch02, Ch03, Ch04, Ch05, Ch06, Ch07, Ch09, Ch12, Ch14, glossary | 0/0 each | 0/0 each | 0/0 each |
| Ch11 | 2/0 | 2/0 | 0/0 |

Both pre-existing em-dashes are on `chapters/11-timeline.md:11`.

All 14 changed files use CRLF with zero bare LF. Git reports `i/lf w/crlf`, including untouched chapters, with `core.autocrlf=true`. `git diff --numstat master` reports **216 insertions / 30 deletions**, with no whole-file rewrite; the largest addition is Ch11's 52 added / 2 deleted lines. Final `git diff --check master` returned **exit 0**.

## 9. Register spot-check

**PARTIAL**

All ten timeline bodies and all ten README bullets were read end to end.

- Every timeline entry opens on its event, supplies concrete details, and closes with the house-style interpretive beat and chapter references: `chapters/11-timeline.md:362`, `:366`, `:370`, `:410`, `:418`, `:422`, `:426`, `:430`, `:434`, `:438`.
- All ten README bullets close with relevant chapter links: `README.md:12-21`.
- Research results retain limitations rather than becoming settled findings: the filesystem paper's negative results, MemTxn's small validation set, StateMem's controls, and portability's migration-direction qualification survive at `chapters/11-timeline.md:366`, `:410`, `:426`.
- AIR's figures, OpenAI's benchmarks, Google's capabilities and Anthropic's allegations remain attributed at `chapters/11-timeline.md:418`, `:422`, `:370`, `:430`.
- Nothing reads truncated or unfinished.
- Salesforce's rollout wording conflicts with its own pilot/first-user qualifications: `README.md:13`, `chapters/11-timeline.md:434`. See F4.
- The gate summaries overstate the scope of the negative evidence. See F2.

## 10. Editorial selection sanity

**PASS --- advisory**

**Included items judged to fail the bar: none on the supplied evidence. Rejected items judged clearly to pass: none established by the rejection record.**

The relevant test is whether an item introduces, validates or operationalizes a tracked primitive, pattern or narrative beat, rather than merely being newsworthy: `CONTRIBUTING.md:34-36`.

The closest calls were checked explicitly:

- **AIR funding:** inclusion rests on the ecosystem measurement and runtime-containment commercialization, jointly with Falcon Guardian, rather than the raise alone: `docs/mid-september-2026/fact-sheet.md:27`, `chapters/05-skill-systems.md:165`. That supplies the structural argument required by `CONTRIBUTING.md:76-78`.
- **Hy4 preview:** the defensible chapter-only contribution is Tencent's reported participation in its own development process, explicitly awaiting replication; ordinary model-size and score improvements would not suffice: `docs/mid-september-2026/fact-sheet.md:48`, `chapters/09-china-ecosystem.md:97`, `CONTRIBUTING.md:48-50`.
- **Memory Decoder scaling:** the separate-memory parameter-efficiency result answers an existing architectural question, making it a new research result rather than an isolated benchmark update: `chapters/06-agent-memory.md:91`, `CONTRIBUTING.md:60-62`.
- **The guide's own gate:** publishing the outcome completes an explicit test already promised to readers: `chapters/14-graph-engineering.md:155-162`, `chapters/11-timeline.md:438`.
- The rejected list contains version bumps, implementations of covered patterns, unresolved dates, inaccessible primaries and future events. Its summaries do not establish a clear omission that overrides those reasons: `docs/mid-september-2026/fact-sheet.md:57`. This is not a claim that every rejected candidate would fail after further evidence.

## Findings needing a maintainer decision

### F1 --- MAJOR: Ch09 retains an unverified named September OpenRouter ranking

**Location:** `chapters/09-china-ecosystem.md:131`.

**Exact text:**

> a snapshot dated September 1 still showed four of the top five as Chinese-origin --- DeepSeek's V4 Flash 0731 first, Zhipu's GLM-5.3 Flash second, GPT-5.6 Luna third as the sole US entry, then Xiaomi's MiMo-V2.5 and Tencent's Hy3.

The corresponding source entry at `chapters/09-china-ecosystem.md:180` assigns both the percentage split and this snapshot to Yahoo Finance and StockAlarm.

**Why it is wrong:** The named ordering remains **unverified**, not demonstrated false. The fact-check record says Yahoo contains neither “GLM-5.3,” “Luna” in a ranking context, nor “September 1”; StockAlarm returned 429 twice (`docs/mid-september-2026/fact-check-findings.md:342-349`, `:612-616`). The timeline now omits this snapshot and cites Yahoo specifically for the share split (`chapters/11-timeline.md:362`, `:620`). Removing token totals did not establish the remaining model names and ordering.

**Suggested minimal fix:** Delete the September 1 named-ranking clause from Ch09 and narrow its source note to the verified percentage split. Retain the detailed ranking only with a recorded successful source check.

### F2 --- MAJOR: Scoped non-adoption evidence becomes a universal absence claim

**Locations and exact text:**

- `README.md:12` and `README.md:113`: “no vendor uses it in product vocabulary”
- `chapters/01-evolution.md:173`: “while no vendor adopted the term in its own product vocabulary”
- `chapters/14-graph-engineering.md:181`: “Neither had happened by September 15, 2026.”

**Why it is wrong:** The scorecard explicitly says:

> No systematic dated audit of every vendor's documentation was run, so this is NOT-MET on the evidence gathered rather than a proven universal absence.

That qualification is at `chapters/14-graph-engineering.md:170`. The summary claims exceed the stated search coverage. The concluding sentence also extends the absence claim to conference tracks despite the bounded conference evidence at `chapters/14-graph-engineering.md:171`.

**Suggested minimal fix:** Use “no vendor adoption was found in the documentation checked” and “neither was established by the evidence gathered.” Preserve the split verdict and apply the same scope consistently across summaries.

### F3 --- MAJOR: CHANGELOG overstates primary-source verification

**Location:** `CHANGELOG.md:13`.

**Exact text:**

> each fact-checked against its primary source

**Why it is wrong:** The same line states that the OpenRouter share figures are secondary-only. The timeline explicitly carries the sweep and percentages from secondary analyses because no dated primary record was available (`chapters/11-timeline.md:362`, `:620`). The universal verification claim contradicts the documented sourcing.

**Suggested minimal fix:** Replace with “checked against the available sources, with secondary-only evidence identified explicitly.”

### F4 --- MINOR: Salesforce wording conflates the portfolio, runtime adoption and GA

**Locations and exact text:**

- `README.md:13`: “shipped under seven job-scoped agents”
- `chapters/11-timeline.md:434`: “shipped it underneath a portfolio of seven job-scoped agents”
- Same paragraph: “the agent built to demonstrate it has not shipped.”

**Why it is wrong:** The same timeline paragraph says Hunter is the **first** agent on the runtime and others will move onto it; it also says Hunter is in pilot. Ch04 accurately distinguishes the portfolio announcement from Hunter's initial runtime adoption and planned GA (`chapters/04-harness-engineering.md:225`). The current wording suggests deployment across all seven, then treats pilot availability as no shipment.

**Suggested minimal fix:** Say “announced alongside a portfolio of seven agents, with Hunter the first on the runtime in pilot.” Replace “has not shipped” with “is not yet generally available.”

### F5 --- MINOR: Calendar intervals need correction or explicit rounding

**New error:** `chapters/14-graph-engineering.md:166`.

> An interim count was taken on August 24, 2026, five weeks before the gate

August 24 to the September 15 check is **22 days**, or three weeks and one day. The check date is explicit at `chapters/14-graph-engineering.md:164`.

**Suggested minimal fix:** Replace “five weeks” with “22 days.”

**Pre-existing precision issue explicitly requested for this review:** `chapters/05-skill-systems.md:161`.

> Across three disclosures in six weeks

The cited first and third disclosures are June 22 and August 6 (`chapters/05-skill-systems.md:157`, `:161`): **45 days**, or six weeks and three days. The fourth beat does not change the historical count of three, but the interval is rounded.

**Suggested minimal fix:** Use “Across three disclosures in just over six weeks.”

### F6 --- MINOR: One timeline heading violates the requested single-day format

**Location:** `chapters/11-timeline.md:364`.

**Exact text:**

```text
### July 29-30, 2026 --- Three Memory Papers in Two Days
```

**Why it is wrong:** This is a date range, while the assembly rule specifies `### Month DD, YYYY --- Title`; the same rule is recorded at `docs/mid-september-2026/fact-sheet.md:62`. The combined event itself is intentional and supported by the selection at `docs/mid-september-2026/fact-sheet.md:34`.

**Suggested minimal fix:** Date the combined milestone July 30, retain July 29-30 in its title or body, and update `README.md:20` to keep the pair aligned. Alternatively, explicitly accept the range as a house-style exception.

## Non-issues noted for the record

- **Primary-source corrections properly supersede drafting caveats.** Direct attribution for distillation, Astra's enterprise default, and Qwen-Scope's corrected range follows the later verification record: `docs/mid-september-2026/fact-check-findings.md:40-90`, `:212-243`; current text at `chapters/09-china-ecosystem.md:51`, `:137`, `chapters/04-harness-engineering.md:63`.
- **Ch09 source-count bookkeeping:** the report says seven new bullets at `docs/mid-september-2026/per-chapter-changes.md:58`; the diff actually contains six new bullets plus the edited dsh bullet, covering all seven planned subjects at `chapters/09-china-ecosystem.md:174-180`.
- **Ch02 numbering premise:** its Sources list was already a dash list, so no numbering repair is warranted: `chapters/02-knowledge-layer.md:204-224`.
- **Historical gate language is visibly historical.** The old absence statements remain inside the preserved July test, followed by explicit corrections and the September outcome: `chapters/14-graph-engineering.md:151-179`.
- **Repeated publishers are not duplicate subjects.** MemTX and MemTxn are independent proposals, and separate Anthropic features have separate source entries: `chapters/06-agent-memory.md:179`, `chapters/04-harness-engineering.md:292`, `chapters/05-skill-systems.md:193`.

---

## Maintainer decisions (editor, 2026-09-15, after the review above)

- F1, F2, F3, F4, F5: applied as suggested (second fix round; 16 exact-once string swaps across README.md, CHANGELOG.md, glossary.md, chapters/01, 05, 09, 11, 14). F2's narrowing was also applied at two further sites the reviewer did not list (glossary.md "Graph Engineering" entry; chapters/11-timeline.md gate entry). The chapters/11-timeline.md September 1 snapshot clause and its StockAlarm citation had already been removed before this review ran; F1's description of the timeline state was stale, and the Ch09 deletion it asked for was applied.
- F6: accepted as a house-style exception --- `### July 29-30, 2026` keeps its date range because the file already carries `### July 17-18, 2026` and `### July 17-22, 2026` headings on master.
- Bookkeeping: docs/mid-september-2026/per-chapter-changes.md corrected (Ch09 six new bullets plus the edited dsh bullet; the Qwen-Scope and distillation lines updated to the post-fact-check text).
