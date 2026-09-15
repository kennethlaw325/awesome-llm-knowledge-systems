ADVERSARIAL FACT-CHECK — mid-september-2026-wave
Target: <repo>, branch mid-september-2026-wave
Scope: git diff master -- chapters/ glossary.md (11 chapters + glossary, 179 added lines)
Checker: read-only. No repo file was modified.
Run: 2026-09-15


================================================================================
SUMMARY
================================================================================

4 BLOCKER / 19 MAJOR / 9 MINOR

Fetch statistics
  URLs/endpoints tried ............ 63
  OK .............................. 59
  Failed .......................... 4   (2 recovered via Exa, see RE-SCAN)
  GitHub API calls ................ 14  (all 200)
  arXiv abs/full-text fetched ..... 12
  WebSearch used .................. 0   (budget was <=10; not needed — every
                                        claim resolved against a named source)

Method note. Every URL below was fetched by this check, not taken from
docs/mid-september-2026/. Where a drafter's note asserted a source "did not
return on fetch", the fetch was re-run rather than the note trusted — one of
those notes is wrong (M-09) and one whole caveat paragraph rests on it.

Scope discipline. chapters/02-knowledge-layer.md line 101 renders as one long
added line, but `git diff --word-diff` shows only two genuine additions in that
file (the September 2026 portability sentence and the Goyal/Ray sources entry).
The Agents-K1 / 2.46-million-paper material on that line is pre-existing master
text and was therefore NOT audited. Same technique applied to 01/05/07/12 and
glossary.


================================================================================
BLOCKERS
================================================================================

[BLOCKER] chapters/09-china-ecosystem.md:51 — Qwen-Scope parameter range is
fabricated.
  Claim: "an open suite of 14 groups of sparse autoencoders trained across seven
  Qwen3 and Qwen3.5 variants, dense and MoE, spanning 0.5B to 72B parameters"
  Source (arXiv 2605.11887 v1 full text, https://arxiv.org/html/2605.11887v1):
  the suite covers exactly seven backbones, enumerated in the paper body —
  Qwen3-1.7B, Qwen3-8B, Qwen3-30B-A3B, Qwen3.5-2B, Qwen3.5-9B, Qwen3.5-27B,
  Qwen3.5-35B-A3B. Grep over the 127 KB full text: zero occurrences of "72B",
  zero of "0.5B" and zero of "0.6B" as parameter sizes. The complete set of
  "<n>B" tokens in the paper is: 2B 3B 7B 8B 9B 27B 30B 35B.
  No model in the release is 0.5B, and none is 72B. The real span is 1.7B-35B.
  Minimal fix: "spanning 0.5B to 72B parameters" -> "spanning 1.7B to 35B
  parameters (Qwen3-1.7B through Qwen3.5-35B-A3B)".

[BLOCKER] chapters/09-china-ecosystem.md:51 and :175 — "33 million interpretable
features" has no support in the cited paper.
  Claim (:51): "covering more than 33 million interpretable features"
  Claim (:175): "33M+ features"
  Source: arXiv 2605.11887 full text. Greps returning zero hits: "33 million",
  "33M", "million features", and the regex "[0-9.]+ ?[Mm]illion" over the whole
  paper (no occurrence of the word "million" anywhere). The paper's Table 1
  reports per-model SAE width, expansion factor and sparsity, and states MoE
  backbones get wider SAEs "up to 64x" — but states no aggregate feature count.
  This is "searched and not found in the v1 full text", not "proven nonexistent";
  it may be derivable by summing Table 1 widths x trained layers. Either way the
  chapter presents it as a reported figure and it is not one.
  Minimal fix: drop the clause, or replace with "covering SAEs whose widths and
  sparsity levels are tabulated per backbone in the paper" — or, if the number is
  computed, say so and show the derivation.

[BLOCKER] chapters/11-timeline.md:621 — the sources note makes two negative
claims about the OpenAI pages that those pages refute.
  Claim: "Pricing, context-window, and max-output figures appear on none of the
  three OpenAI pages and are not cited here; neither does an enterprise
  off-by-default access control, which appears only in secondary coverage and is
  therefore not claimed in the entry."
  Source, https://openai.com/index/gpt-6-astra/ (fetched via Exa; plain curl
  returns 403), Availability section, verbatim:
    "Enterprise administrators can enable Astra for their workspace; access is
     off by default at launch."
    "OpenAI API Standard pricing is $10 per million input tokens and $50 per
     million output tokens. Separate rates apply to cache reads and writes."
  Both the pricing figures and the enterprise off-by-default control are on the
  primary launch page. Only the context-window / max-output half of the sentence
  survives.
  Minimal fix: "Pricing, context-window, and max-output figures appear on none of
  the three OpenAI pages" -> "Context-window and max-output figures appear on
  none of the three OpenAI pages and are not cited here. The launch page does
  carry API pricing ($10 / $50 per million input / output tokens) and states that
  enterprise access is off by default at launch; neither is load-bearing for this
  entry."
  Why BLOCKER: a negative claim about a primary source, contradicted by that
  source, inside the note whose job is to tell the reader what was checked.

[BLOCKER] chapters/14-graph-engineering.md:93 and :202 — SmartScope footer quote
not found on the source.
  Claim (:93): "its own footer states that its articles are 'AI-researched,
  written, and fact-checked before publication'"
  Claim (:202): same string repeated in the sources list.
  Source: three surfaces of the site fetched and grepped, rendered text and raw
  HTML both — the article itself
  (https://smartscope.blog/en/blog/graph-engineering-loop-engineering-logic-review/,
  13.5 KB text / 47.8 KB HTML), https://smartscope.blog/en/about/ and
  https://smartscope.blog/en/. Zero hits for "AI-research" and zero for the regex
  "fact.check" on all three.
  Stated honestly: not found on three fetched surfaces, which is not the same as
  proven absent (the footer could be client-rendered, or on a page not fetched).
  But a quoted string that cannot be located must not stand as a quotation.
  Minimal fix: either re-fetch and cite the exact page carrying the string, or
  drop the quotation marks and the clause. The second caveat in that sentence
  (the July 20 self-bound) is verified and can stand alone.


================================================================================
MAJOR
================================================================================

[MAJOR] chapters/09-china-ecosystem.md:51 and :175 — count error: three uses vs
the paper's four.
  Claim (:51): "the paper presents SAE features as development tooling across
  three uses --- inference-time steering ..., data classification and
  organization, and post-training support for supervised fine-tuning and RL"
  Claim (:175): "steering, data classification, and post-training uses"
  Source (2605.11887 abstract, verbatim): "practical interfaces for model
  development along four directions: (i) inference-time steering ...; (ii)
  evaluation analysis, where activated SAE features provide a representation-
  level proxy for benchmark redundancy and capability coverage; (iii) data-
  centric workflows ...; (iv) post-training optimization ..."
  The dropped direction is (ii) evaluation analysis.
  Minimal fix: "across three uses" -> "across four directions", and insert
  "evaluation analysis that proxies benchmark redundancy and capability
  coverage," into the list in both places.

[MAJOR] chapters/14-graph-engineering.md:67 — the bolded lede contradicts its own
paragraph and two other passages.
  Claim (heading): "A second vendor shipped it first, seven weeks before the name
  existed."
  Same paragraph, last sentence: "That is a month before Steinberger's post and
  seven weeks before Anthropic's cross-session messaging."
  Arithmetic: PR #29324 merged 2026-06-22 (GitHub API merged_at
  2026-06-22T08:05:36Z); the name dates from 2026-07-17/18. That is 26 days, i.e.
  "a month", not seven weeks. Seven weeks from June 22 is ~August 10, which is
  what the body attaches to Anthropic's cross-session messaging — a different
  event. chapters/01-evolution.md:173 and chapters/14-graph-engineering.md:179
  both say "a month before the term existed", agreeing with the body.
  Minimal fix: heading -> "A second vendor shipped it first, a month before the
  name existed."

[MAJOR] chapters/14-graph-engineering.md:91 — "Perez's anchors" attributes the
lesson to a person the source never names.
  Claim: "runs eleven lessons on routing, fan-out and fan-in, supervisor-
  specialist hierarchies, merge logic and Perez's anchors"
  Source: https://graphengineerings.com/course/module-2.html — Lesson 2.11 is
  titled "Anchors -- and earning the scale". Grep for "perez", case-insensitive,
  over both the rendered text and the raw HTML of module-2 AND the course home
  page: zero hits on all four. The only named expert lenses on Module 2 are
  "Chi Wang, João Moura".
  The chapter's own sources entry (:201) says "merge logic and anchors" with no
  Perez — so the body line is the outlier.
  Minimal fix: "merge logic and Perez's anchors" -> "merge logic and anchors"
  (matching :201). Eleven lessons is correct: LESSON 2.1 through 2.11, verified
  by enumeration.

[MAJOR] chapters/14-graph-engineering.md:91 and :204 — AgentEng's discipline list
is non-exhaustive, and the chapter reads it as exhaustive to support an absence.
  Claim (:91): 'AgentEng London ... names its disciplines as "context, harness,
  memory, evaluation, inference, protocols, and agentic coding" --- no graph
  track'. Repeated at :170 ("AgentEng London's published disciplines contain no
  graph") as Signal 1 / Signal 2 evidence.
  Source (https://agentengineering.world/london/, verbatim): "Talks cover
  disciplines such as context, harness, memory, evaluation, inference, protocols,
  and agentic coding."
  "such as" makes the list illustrative. Reading an illustrative list as a
  complete taxonomy is what turns it into evidence of absence, and that inference
  feeds the scorecard.
  (The underlying absence does hold on the evidence available: grep for "graph"
  over the whole fetched page returns zero hits. The problem is the warrant, not
  the conclusion.)
  Minimal fix: 'names its disciplines as "..."' -> 'lists its disciplines as
  "disciplines such as context, harness, memory, evaluation, inference,
  protocols, and agentic coding" --- an illustrative list, on which graph does not
  appear, and the word "graph" appears nowhere else on the page either'.

[MAJOR] chapters/09-china-ecosystem.md:35 and :177 — "No launch date ...
confirmed" is contradicted by the cited article.
  Claim (:35): "No launch date for the combined app has been confirmed."
  Claim (:177): "the launch date of the combined app is not confirmed in the
  reporting"
  Source (https://eu.36kr.com/en/p/3953230805876099, verbatim): "We also learned
  that Doubao will launch an independent AI office product 'Doubao Work' as soon
  as this week, serving as the unified product and brand of ByteDance for the AI
  office scenario."
  The reporting gives a timeframe ("as soon as this week", i.e. w/c 2026-08-24).
  It is unconfirmed by ByteDance, which is a different statement.
  Minimal fix: "No launch date for the combined app has been confirmed." ->
  "36kr reported the combined app would launch 'as soon as this week'; ByteDance's
  own response addressed only the reorganisation, so the date is reported rather
  than company-confirmed."

[MAJOR] chapters/09-china-ecosystem.md:35 — "aimed at Tencent's WorkBuddy" is not
in the only source cited for the reorg.
  Claim: "TRAE Work and Coze combine with Doubao's office features under a single
  forthcoming brand, 'Doubao Work,' aimed at Tencent's WorkBuddy."
  Source: the 36kr piece (:177 is the only citation for this paragraph). Grep for
  "Tencent" over the fetched article: zero hits. Grep for "WorkBuddy": zero hits.
  The article's competitive framing is entirely internal to ByteDance (TRAE and
  Coze moving out of the Product R&D and Engineering Architecture Department,
  reporting to Zhao Qi, Head of Doubao Products).
  Minimal fix: delete "aimed at Tencent's WorkBuddy", or cite a source that makes
  the comparison. (WorkBuddy does exist and is Tencent's — it appears on the
  Tencent Hy4 page cited at :176 — but that page does not tie it to Doubao Work.)

[MAJOR] chapters/09-china-ecosystem.md:137 and :179; chapters/11-timeline.md:430
and :623 — the "did not return on fetch" caveat is wrong; the primary is
readable and every figure checks out against it.
  Claim (09:137): "those specific numbers are drawn from secondary coverage of
  the report rather than read from its distillation section directly --- ... its
  full distillation text did not return on fetch, so the figures should be
  re-verified against the report itself before being reused."
  Same caveat at 09:179, 11:430, 11:623.
  Source: https://www.anthropic.com/threat-intelligence-report-september-2026
  fetched with plain `curl -sSL -A "Mozilla/5.0 ..."`, HTTP 200, 1.22 MB HTML /
  259 KB rendered text. The distillation section returns in full. Verbatim:
    "In one instance, over a ten-day period, Moonshot relayed almost 300,000
     customer requests to Anthropic, the vast majority of which were routed to
     Opus. Moonshot used a proxy service network of 5,380 fraudulent accounts,
     most of which appeared to be located in Singapore and Japan."
    "Scale of distillation attacks attributable to Moonshot between May and July
     2026: over 23 million exchanges observed."
    "This report covers activity we disrupted between December 2025 and August
     2026 across seven harm areas: cyber operations, influence operations,
     surveillance, scams and fraud, biological misuse, conventional weapons
     development, and distillation."
    "Our investigation revealed that DeepSeek targeted the reasoning traces of
     Opus ... DeepSeek used this technique to exfiltrate reasoning traces that
     would have otherwise been summarized."
  Every figure the chapters carry is confirmed against the primary: 5,380, almost
  300,000, ten-day period, over 23 million, May-July 2026, mostly Opus, Singapore
  and Japan, seven harm areas, DeepSeek cross-session replay against Opus traces.
  The chapters are accurate; the caveat about them is not.
  Minimal fix: delete the "did not return on fetch" clause in all four places and
  attribute the figures to the report directly, keeping the "Anthropic's own
  allegation, not independently adjudicated" caveat, which remains correct and
  is the one that matters.
  Related, worth a decision rather than a fix: the report also states "Scale of
  distillation attacks attributable to Alibaba between May and July 2026: over
  151 million exchanges observed" — 6.5x the Moonshot figure the chapters lead
  with — and names SenseTime alongside the five labs the chapters list. An entry
  headed "Industrial-Scale Distillation" that leads on the smaller number is a
  selection call the editor should make knowingly.

[MAJOR] chapters/06-agent-memory.md:117, :181; chapters/11-timeline.md:426, :622
— the "34 of 48" result loses the qualifier that bounds it.
  Claim (06:117): "while keeping the raw source history alongside the compressed
  memory enabled successful repair in 34 of them"
  Claim (11:426): "makes repair succeed in 34 of 48"
  Claim (06:181 / 11:622): "raw source retained enables repair in 34/48"
  Source (arXiv 2609.05339 abstract, verbatim): "whereas retaining the raw source
  history enables successful recovery in 34 of 48 cases for one tested direction."
  The paper's own framing elsewhere in the same abstract is that the effects are
  direction-asymmetric (that is the point of the +9.91 / -13.28 split). Dropping
  "for one tested direction" turns a one-direction result into a general one.
  Minimal fix: append "in one of the two tested migration directions" at each of
  the four sites.
  (Everything else in this paper's reporting verifies exactly: 48 synthetic
  cases; +0.0004 +/- 0.0020; +9.91 / -13.28; 4.96 vs 11.90 points; 80% attributed
  to construction-time loss; store-only repair never reaching 90% recovery in all
  48. Two authors, Goyal and Ray. Submitted 4 Sep 2026.)

[MAJOR] chapters/04-harness-engineering.md:103 and :294 — arXiv 2607.12227 is
described as a methodology critique, suppressing the empirical result it reports.
  Claim (:103): "puts an accounting problem to the sub-literature: harness-
  evolution methods have to be benchmarked against simple task-level search
  baselines ... Read together, the two papers mark the moment harness evolution
  ... became a field with a measurement dispute"
  Claim (:294): "methodology critique of the harness-evolution literature"
  Source (2607.12227 abstract, verbatim): "Experiments on Terminal-Bench 2.1 with
  GPT-5.4 and Claude Opus 4.6 show that automatic harness evolution does not
  consistently outperform simple test-time scaling methods and exhibits limited
  generalization."
  The paper did not only propose a fairer protocol; it ran it and reported that
  harness evolution failed under it. A section that opens "Evolution moves to
  test time, and gets its first methodology check" and closes on "a measurement
  dispute" reads as procedural when the cited finding is substantive.
  Minimal fix: after "obvious overfitting risk", add: "Run under that protocol on
  Terminal-Bench 2.1 with GPT-5.4 and Claude Opus 4.6, the authors report that
  automatic harness evolution does not consistently beat simple test-time
  scaling and generalizes poorly to held-out tasks." Update :294 from
  "methodology critique" to "methodology critique plus a negative empirical
  result".
  (Verified and correct in the same passage: TTHE = arXiv 2607.08124, Nie et al.,
  submitted 9 Jul 2026; 2607.12227 v1 14 Jul 2026, v2 27 Aug 2026 — exactly five
  days apart, exactly as written; Wang et al. is the right first author; and
  "the critique does not name TTHE" holds — its harness-evolution citations are
  Lee et al. 2026, Lin et al. 2026, Zhang et al. 2026.)

[MAJOR] chapters/06-agent-memory.md:57, :178; chapters/11-timeline.md:366, :617 —
the filesystem-memory paper's negative findings are dropped, and the passage reads
as validation.
  Claim (06:57): "Its headline finding is the one that matters ...: keeping the
  store organized roughly halves retrieval cost once the store is large. That is
  the empirical claim ByteRover's design has been making implicitly ... the work
  of keeping the tree tidy is not housekeeping but the retrieval budget itself."
  Source (arXiv 2607.26637 abstract, verbatim): "What organization reliably buys
  is search economy: organized stores roughly halve retrieval cost where material
  is large. Today's agents, however, fall short of the default's promise: in our
  growth study, organization erodes for all but the strongest management agent,
  and no agent we measure converts organization itself into better answers."
  The half the chapter quotes is real. The half it omits says the pattern does
  not hold up in practice and buys no answer-quality gain — which cuts directly
  against "ByteRover's design has been making implicitly".
  Minimal fix: after "the retrieval budget itself", add: "The same paper is
  blunter than that reading allows: organization erodes for all but the strongest
  management agent in its growth study, and no agent it measures converts
  organization into better answers. Cheaper search, not better answers, is what
  the tidy tree buys." Mirror one clause into :178 and the 11:366 entry.
  (Verified: title exact; Sizhe Zhou + 10 coauthors = 11 authors, correct;
  submitted 29 Jul 2026; three roles exactly as described.)

[MAJOR] chapters/11-timeline.md:616 — KuCoin is cited for figures it does not
carry, from a different snapshot date.
  Claim: "September continuation: [yahoo] and [stockalarm] and
  [https://www.kucoin.com/news/flash/chinese-models-dominate-openrouter-weekly-token-usage-ranking]
  --- the 46.4% / 35.7% split and the September 1 top-five snapshot."
  Source (KuCoin, fetched HTTP 200, verbatim): "As of August 5, 2026, new token
  listings dominated the OpenRouter weekly token usage ranking, with Chinese
  models occupying eight of the top ten spots. DeepSeek V4 Flash 0423 led with
  692 billion tokens, followed by Xiaomi MiMo-V2.5 and Tencent Hy3. ... Zhipu GLM
  5.2, MiniMax M3, and Jieyue Step 3.7 Flash also appeared."
  Wrong date (August 5, not September 1), wrong model versions (V4 Flash 0423 not
  0731; GLM 5.2 not 5.3 Flash), wrong magnitude (692 billion, not 12.1 trillion),
  top-ten not top-five, and no 46.4% / 35.7% anywhere on the page.
  Minimal fix: remove the KuCoin URL from this entry, or re-cite it for what it
  actually supports (an August 5 snapshot in which Chinese models held eight of
  the top ten).

[MAJOR] chapters/11-timeline.md:362 — the September 1 top-five token figures are
currently unverified.
  Claim: "a snapshot dated September 1, 2026 still shows four of the top five
  Chinese-origin (DeepSeek V4 Flash 0731 at 12.1T weekly tokens, GLM-5.3 Flash at
  10T, OpenAI's GPT-5.6 Luna at 9.52T, Xiaomi MiMo-V2.5 at 7.2T, Tencent Hy3 at
  5.89T)."
  What was checked: the Yahoo Finance piece cited alongside it carries the
  46.4% / 35.7% split verbatim ("Chinese-origin models now account for 46.4% of
  routed tokens, compared to 35.7% for US-origin models") but contains no hit for
  "12.1", "GLM-5.3", "Luna" in a ranking context, or "September 1". KuCoin is the
  wrong snapshot (above). StockAlarm returned HTTP 429 on two attempts — see
  RE-SCAN.
  So five specific trillion-token figures, presented as a dated snapshot, rest on
  one source that could not be fetched.
  Minimal fix: hold the five figures until StockAlarm (or another source) is
  fetched and confirms them; until then cut the parenthesis and keep "a snapshot
  dated September 1, 2026 still showed four of the top five Chinese-origin", which
  is the part the surrounding sources support. Same parenthesis appears only
  here, so it is a single-site fix.

[MAJOR] chapters/11-timeline.md:621 and chapters/04-harness-engineering.md:291 —
the OpenAI launch page is cited under a title it does not have.
  Claim: 'OpenAI, "Introducing GPT-6 Astra": https://openai.com/index/gpt-6-astra/'
  Source: the page's own title is "GPT-6 Astra: A new generation of intelligence"
  (document title, confirmed on fetch; the page's opening H2 is "A new generation
  of intelligence"). "Introducing GPT-6 Astra" appears nowhere on it.
  Minimal fix: '"Introducing GPT-6 Astra"' -> '"GPT-6 Astra: A new generation of
  intelligence"' in both places.

[MAJOR] chapters/14-graph-engineering.md:93 — "both September pieces that cite it"
overstates the dating evidence by one source.
  Claim: "an essay title: 'Loop Engineering Is Dead. Enter Graph Engineering,'
  attributed to Hamel Husain and dated July 18, 2026 by both September pieces
  that cite it."
  Source A, SmartScope, supports it: "Peter Steinberger's one-line post at 00:34
  UTC on July 18, 2026 ... About four and a half hours later, Hamel Husain
  published an X Article titled 'Loop Engineering Is Dead. Enter Graph
  Engineering.'"
  Source B, Towards Data Science, does not: it says only "In mid-2026, Peter
  Steinberger ... posted a twelve-word question on X" and "a few hours later, AI
  engineer Hamel Husain answered it directly". Grep for "July 18" over the
  fetched TDS page returns exactly one hit, and it is an unrelated sidebar
  article ("Chad Isenberg July 18, 2023").
  Minimal fix: "dated July 18, 2026 by both September pieces that cite it" ->
  "dated July 18, 2026 by SmartScope, which times it about four and a half hours
  after Steinberger's 00:34 UTC post; the Towards Data Science piece names the
  title and author but gives no date".

[MAJOR] chapters/14-graph-engineering.md:91 — "names no instructor and no company"
is contradicted by the footer the same sentence cites.
  Claim: "It is also close to anonymous: the site names no instructor and no
  company, carries only a '© 2026 GraphEngineerings.com' footer and a Newark,
  California address"
  Source (https://graphengineerings.com/ footer, verbatim): "© 2026
  GraphEngineerings.com · Graph Engineering Mastery -- Course Version 1 prompts →
  context → harness → loops → graphs · The Case006 for Justdoit.work 8407 Central
  Ave, Newark, CA 94560 · (650) 889-5124"
  The footer names a second entity (Justdoit.work) and publishes a phone number
  alongside the Newark address. "No instructor" holds; "no company" does not.
  Minimal fix: "the site names no instructor and no company" -> "the site names
  no instructor, and identifies itself only as 'The Case006 for Justdoit.work'".
  (Verified and correct in the same passage: $6.93 lifetime / $19.63 monthly,
  six modules, Module 2 title, eleven lessons 2.1-2.11, the unit-testable pure
  function exercise quote, the "not presented as formal faculty or endorsers"
  quote, Newark CA, and no accreditation claim — "accredit" returns zero hits.)

[MAJOR] chapters/04-harness-engineering.md:63 — a superlative broader than the
source supports.
  Claim: "the first time a frontier lab has declared a model across the top tier
  of its own published risk ladder"
  Source (https://openai.com/index/path-to-astra/, verbatim): "It is the first
  model we are designating at this level" — a first for OpenAI, on OpenAI's
  ladder. The safety overview likewise says "Astra is our first model to reach
  the Critical level" (emphasis on "our"). Neither page makes, and neither could
  make, a claim about every frontier lab's ladder.
  Minimal fix: "the first time a frontier lab has declared a model across the top
  tier of its own published risk ladder" -> "the first model OpenAI has designated
  at the top tier of its own published risk ladder".

[MAJOR] chapters/11-timeline.md:422 — Daybreak routing is stated in the present
tense for something OpenAI describes as planned, and conflates two access paths.
  Claim: "OpenAI routes legitimate defensive use --- vulnerability and proof-of-
  concept validation, malware analysis, detection engineering --- through a
  separate vetted-tester program, Daybreak, rather than loosening the default."
  Source, launch page, verbatim: "Through OpenAI Daybreak, we plan to expand
  access and roll out less restrictive safeguards in the coming weeks. This will
  enable more defensive workflows, including vulnerability and proof-of-concept
  validation, malware analysis, and detection engineering."
  Source, path-to-astra, verbatim: "Access to Astra for advanced cybersecurity
  workflows will initially be available to a small group of alpha testers, with
  access through Daybreak Blue expanding afterward to support defensive use."
  So: the defensive workflows are a stated plan, not a shipped route; the initial
  vetted group is "a small group of alpha testers"; and the named expansion
  vehicle is Daybreak Blue.
  Minimal fix: "OpenAI routes ... through a separate vetted-tester program,
  Daybreak" -> "OpenAI says advanced cybersecurity access will go first to a small
  group of alpha testers, with Daybreak and Daybreak Blue named as the planned
  path by which vetted defenders get less restrictive safeguards for vulnerability
  and proof-of-concept validation, malware analysis, and detection engineering".
  (chapters/04-harness-engineering.md:63 already words this correctly — "OpenAI
  names Daybreak and Daybreak Blue as the path by which..." — so this is a
  Ch11-only fix and also removes a cross-file inconsistency.)

[MAJOR] Three arXiv papers are cited under descriptive paraphrases instead of
their titles.
  chapters/02-knowledge-layer.md:224, chapters/06-agent-memory.md:181,
  chapters/11-timeline.md:622: "Goyal, Ankit and Ray, Jaideep. Controlled study of
  agent-memory portability across model upgrades."
    Real title: "Does Your Agent's Memory Survive a Model Upgrade? A Controlled
    Study of Memory Portability" (arXiv 2609.05339).
  chapters/03-context-engineering.md:114: "Chen, Le et al. Nine-author study of
  heterogeneous working memory in coding agents."
    Real title: "Measure Before You Manage: Evaluating Agent Working Memory in
    Coding Agents" (arXiv 2608.31057). Nine authors is correct: Le Chen, Zishen
    Wan, Baixi Sun, Xiaolong Ma, Chih-Hsuan Yang, Feng Yan, Sheng Di, Franck
    Cappello, Rajeev Thakur.
  chapters/06-agent-memory.md:182 and chapters/11-timeline.md:619: '"StateMemBench,"
  arXiv 2608.19652' — quotation marks make a benchmark name look like a title.
    Real title: "Can Agent Memory Systems Track Evolving State?" (arXiv
    2608.19652). Authors verified as the five named at 11:410: Xinyi Fan, Miri
    Liu, Ruozhen Yang, Siru Ouyang, Jiawei Han.
  Every other citation in the wave gives the real title, so these five sites are
  the exception rather than a house style.
  Minimal fix: substitute the real titles; keep the descriptive phrase as gloss
  after the title if it is doing work.

[MAJOR] chapters/14-graph-engineering.md:172 — Signal 3's "MET, retrospectively"
cell is sound, but one supporting quote is truncated into a false sentence.
  Every substantive element of the cell verifies against
  https://www.anthropic.com/engineering/multi-agent-research-system: "outperformed
  single-agent Claude Opus 4 by 90.2%" (verbatim); LLM-judge evaluation from "a
  set of about 20 queries representing real usage patterns" (verbatim) on factual
  accuracy / citation accuracy / completeness / source quality; "systems that can
  resume from where the agent was when the errors occurred" (verbatim); "about
  15x more tokens than chats"; a lead agent that "analyzes it, develops a
  strategy, and spawns subagents to explore different aspects simultaneously"
  (verbatim); CitationAgent; and the phrase "graph engineering" appears zero
  times on the page. The scorecard verdict is well-founded.
  The defect is at :71: 'releases use "rainbow deployments to avoid disrupting
  running agents, by gradually shifting traffic."' The source sentence continues:
  "... by gradually shifting traffic from old to new versions while keeping both
  running simultaneously." The chapter closes the quotation with a period at a
  mid-sentence cut, which presents a fragment as a complete quoted sentence.
  Minimal fix: '..., by gradually shifting traffic."' -> '..., by gradually
  shifting traffic from old to new versions while keeping both running
  simultaneously."'


================================================================================
MINOR
================================================================================

[MINOR] chapters/03-context-engineering.md:71 and :113 — "internal case study" is
a form the source does not use.
  Claim: "Anthropic reports that figure from an internal case study; it is not
  independently benchmarked." / ":113 (Anthropic's own internal case study, not
  independently benchmarked)"
  Source (verbatim): "We removed over 80% of Claude Code's system prompt for
  models like Claude Opus 5 and Claude Fable 5 with no measurable loss on our
  coding evaluations." Grep for "case study": zero hits.
  The substance ("Anthropic's own, not independent") is right; "case study" is
  invented framing.
  Minimal fix: "from an internal case study" -> "from its own coding evaluations".
  (Verified: title, author Thariq Shihipar, date July 24 2026, and the 80%+ figure
  all exact. Note the post scopes it to "models like Claude Opus 5 and Claude
  Fable 5", which the chapter generalises to "Claude 5 generation models" — the
  page title does the same, so this is fine.)

[MINOR] chapters/06-agent-memory.md:131 and chapters/11-timeline.md:410 — the two
StateMem comparators are conflated into one.
  Claim: "rising 1.8x on DeepSeek-V4-Flash (0.205 to 0.363) and 1.6x on
  Qwen-3.5-9B (0.149 to 0.233) against leading memory systems"
  Source (2608.19652 abstract, verbatim): "improves current-state accuracy over
  the strongest same-backbone baseline by 1.8x (0.205 -> 0.363) on
  DeepSeek-V4-Flash and over the strongest memory system by 1.6x (0.149 -> 0.233)
  on Qwen-3.5-9B".
  Different comparators: strongest same-backbone baseline vs strongest memory
  system. The numbers themselves are exact, as are 234 scenarios, closed-pool
  grading, +32 to +67 as a wrapper over six backends, and +15 to +32 surviving
  the length- and cost-matched control.
  Minimal fix: "against leading memory systems" -> "against the strongest
  same-backbone baseline and the strongest memory system respectively".

[MINOR] chapters/03-context-engineering.md:73 and :114 — one word dropped from the
fourth evaluation level.
  Claim: "four-level evaluation framework separating stored state, delivered
  context, management work, and task outcome"
  Source: "We organize these lessons into four levels: stored state, delivered
  context, management work, and task or process outcome."
  Minimal fix: "task outcome" -> "task or process outcome" in both places.

[MINOR] chapters/09-china-ecosystem.md:97 — inflection changed inside quotation
marks.
  Claim: Tencent says Hy4 "participated for the first time in the automated
  optimization of training methods, data strategies, evaluation frameworks, and
  low-level operators"
  Source (verbatim): "Hy4 preview also contributed to its own development process,
  participating for the first time in the automated optimization of training
  methods, data strategies, evaluation frameworks, and low-level operators."
  "participating" -> "participated". No meaning changes, so this does not block;
  it is flagged because the wave's contract requires quoted strings to be verbatim
  substrings.
  Minimal fix: "participated" -> "[p]articipating", or recast as "Tencent says Hy4
  contributed to its own development, 'participating for the first time in...'".
  (Everything else on this line verifies exactly: 770B / 49B active, context
  "exceeding 1M tokens", 31.8% end-to-end throughput gain from autonomous
  inference-bottleneck optimisation, blind evaluation with 163 experts and 203
  engineering tasks scoring 2.99/4.00 vs GLM-5.3 2.92 and Kimi K3 2.94, TokenHub
  and OpenRouter serving, August 28 2026.)

[MINOR] chapters/11-timeline.md:370 and chapters/06-agent-memory.md:183 — "four
capabilities" undercounts the five the blog names.
  Claim (11:370): "Google moved four Gemini Enterprise Agent Platform capabilities
  to general availability together."
  Source: the blog gives five separately headed bullets — Agent Memory Bank,
  Agent Runtime, Agent Identity, Agent Gateway, Agent Registry. The chapters fuse
  Gateway and Registry into "Agent Gateway / Registry" to reach four.
  Minimal fix: "four" -> "five", and split "Agent Gateway / Registry" into the two
  bullets the source uses.
  (Verified exactly: "agents capable of running continuously for up to 7 days";
  Memory Bank as "defining structured schemas that automatically extract and
  maintain critical conversation context"; Agent Identity; July 30 2026.)

[MINOR] chapters/14-graph-engineering.md:93 — quotation truncated at a period
without an ellipsis.
  Claim: 'the piece bounds itself, noting that "as of July 20, the cited posts and
  public materials do not provide a standard definition."'
  Source: "As of July 20, the cited posts and public materials do not provide a
  standard definition, a canonical reference architecture, peer-reviewed evidence
  of effectiveness, or a comparative benchmark against Loop Engineering."
  Cutting at "definition." makes the bound look narrower than it is — the source's
  list is stronger, not weaker, so the chapter under-claims.
  Minimal fix: end the quote with "...do not provide a standard definition, a
  canonical reference architecture, peer-reviewed evidence of effectiveness, or a
  comparative benchmark against Loop Engineering."

[MINOR] chapters/04-harness-engineering.md:291 and chapters/11-timeline.md:621 —
"page states Published 2026-09-03" is not what the page states.
  Source: the safety overview renders its date as "September 3, 2026" in the page
  body; there is no "Published 2026-09-03" string (the ISO form comes from fetch
  metadata). The date itself is correct.
  Minimal fix: "(Published 2026-09-03)" -> "(dated September 3, 2026 on the
  page)". Same for path-to-astra, which renders "September 1, 2026".

[MINOR] chapters/05-skill-systems.md:165 and :192 — "and skills" added to a figure
the source states for add-ons only.
  Claim: "more than 17,800 public AI add-ons and skills, representing roughly 6.7
  million installations"
  Source (SecurityWeek, verbatim): "more than 17,800 public AI add-ons
  (representing 6.7M installations) relying on untrusted external instruction
  sources."
  The same sentence separately reports "AI Skills in the wild impersonating
  companies like Anthropic and OpenAI" — so skills are discussed, but the 17,800
  count is stated for add-ons.
  Minimal fix: "17,800 public AI add-ons and skills" -> "17,800 public AI
  add-ons".
  (Verified exactly: $50M total, $10M first round led by Sequoia, $40M second led
  by Greenoaks, all from TechCrunch September 1; the impersonation finding and
  the "designed to bypass security reviews" framing from SecurityWeek September 3;
  the two-day spread is indeed publication lag on one announcement.)

[MINOR] chapters/14-graph-engineering.md:199 — "both pull requests" omits a third
credited PR.
  Claim: 'first released build carrying both pull requests'
  Source (release rust-v0.142.0 body, verbatim): "App-server clients can configure
  multi-agent delegation as disabled, explicit-request-only, or proactive at the
  thread and turn level. (#28685, #28792, #29324)"
  A third PR, #28685, is credited in the same line.
  Minimal fix: "carrying both pull requests" -> "carrying both pull requests (the
  release note credits #28685 alongside them)".


================================================================================
RE-SCAN LIST (could not be fetched or fetched only via fallback)
================================================================================

1. https://pro.stockalarm.io/blog/openrouter-llm-rankings-investor-analysis
   curl + browser UA -> HTTP 429, twice (2 attempts, ~3 min apart). 278 bytes of
   text returned. BLOCKS verification of the five September 1 top-five token
   figures in chapters/11-timeline.md:362 (see the MAJOR above). Highest-priority
   re-scan in this list.

2. https://openai.com/index/gpt-6-astra/
   curl + browser UA -> HTTP 403 (9,776 bytes challenge page). RECOVERED via
   mcp__exa__web_fetch_exa, full text. All claims against it were checked on the
   Exa copy.

3. https://openai.com/index/path-to-astra/
   curl + browser UA -> HTTP 403. RECOVERED via mcp__exa__web_fetch_exa, full
   text including the "Published: 2026-09-01" metadata.

4. arXiv API (export.arxiv.org/api/query)
   HTTP 429 "Rate exceeded" on 11 consecutive id_list calls. Worked around by
   fetching /abs/ pages with curl and /html/ full text, plus Exa. No claim was
   left unverified because of this.

Not re-scanned, judged non-load-bearing for any claim in the diff (each is cited
only as supplementary secondary coverage, and the claim it supports is already
carried by a fetched source): cryptobriefing.com, mindstudio.ai,
digitalapplied.com, flowtivity.ai (all four cited at 09:174 / 11:612 only for the
"fastest adoption curve" qualitative framing, which the chapters already mark as
"qualitatively"); unite.ai and siliconangle.com Salesforce pieces (Salesforce
primary fetched and complete); siliconangle.com and scworld.com CrowdStrike
pieces (CrowdStrike primary fetched and complete); technode.com Hy4 and
technode.global distillation pieces (both primaries fetched and complete);
dealroom.co, cnbc.com distillation pieces (primary now fetched in full, see M-09);
csoonline.com and cnbc.com Astra pieces; enterprisedna.co; techbriefly.com
(fetched, 200, consistent with Dataconomy); bloomberg.com (paywalled, and the
chapter already says so and cites TechPowerUp and TFTC instead);
openrouter.ai/rankings (live rolling view, as the chapters state);
docs.cloud.google.com memory-bank page; deepseek.com/harness/en/.

DeepSeek Bloomberg/Ascend paragraph (09:71, 09:178): NOT independently verified.
The chapter states outright that Bloomberg is paywalled and was not fetched, and
attributes the 160,000 / 950DT / 1GW / Ulanqab / late-2027 figures to TechPowerUp
and TFTC. That self-declaration is honest and the paragraph is hedged correctly
("stated intent, not deployed capacity"), so it was deprioritised against the
unhedged claims above rather than cleared.


================================================================================
VERIFIED LIST — every URL/endpoint fetched by this check
================================================================================

Format: URL | status | what was checked against it

GitHub API (14 calls, all 200)
  repos/deepseek-ai/deepseek-harness | 200 | 224,039 stars / 26,644 forks / MIT /
    created 2026-08-13 — chapter's "224,004 stars and 26,637 forks ... verified
    September 15, 2026" is consistent (35 stars, 7 forks of same-day drift); MIT
    licence and August 13 2026 creation date both confirmed
  repos/deepseek-ai/deepseek-harness/readme | 200 | "Cordis" present in README
  repos/deepseek-ai/deepseek-harness/contents/packages/subagent | 200 |
    subagent-claude-code and subagent-codex directories exist
  .../subagent-claude-code/package.json | 200 | name =
    "@deepseek-ai/dsh-subagent-claude-code" — chapter's package name EXACT
  .../subagent-codex/package.json | 200 | name = "@deepseek-ai/dsh-subagent-codex"
    — EXACT
  search/code?q=repo:deepseek-ai/deepseek-harness+dsh-subagent | 200 | 258 hits
  repos/cbrock84/headcount | 200 | created 2026-08-28, MIT, 1,393 stars;
    description field = "...15+ departments, 125+ skills..." — confirms the
    chapter's "stale at 15+ departments, 125+ skills"
  repos/cbrock84/headcount/readme | 200 | "a chief executive over 16 departments,
    172 skills in total" VERBATIM; "reviewer-class" on Security (CISO) and
    Legal & Risk (CLO/CCO); "Agents split by exclusive write surface, not by
    topic -- a topic split has no checkable boundary" VERBATIM; zero hits for
    "graph engineering". Ch14:73 and :200 fully verified.
  repos/openai/codex/pulls/28792 | 200 | merged 2026-06-19, title "Expose
    thread-level multi-agent mode" — both EXACT
  repos/openai/codex/pulls/29324 | 200 | merged 2026-06-22, title "Simplify
    multi-agent mode controls" — both EXACT; body carries all three mode
    descriptions VERBATIM ("Keep multi-agent tools available without adding mode
    instructions." / "Only delegate after an explicit user request." / "Delegate
    when parallel work materially improves speed or quality."); zero hits for
    "graph engineering"
  repos/openai/codex/releases/tags/rust-v0.142.0 | 200 | published 2026-06-22;
    body carries "App-server clients can configure multi-agent delegation as
    disabled, explicit-request-only, or proactive at the thread and turn level."
    VERBATIM
  repos/openai/codex/releases/tags/rust-v0.141.0 and rust-v0.143.0 | 200 | zero
    hits for "graph engineering" — confirms Ch14:69's three-version absence claim
  repos/ollama/ollama/releases/tags/v0.33.0 | 200 | published 2026-08-21; "Claude
    Desktop to seamlessly work with Ollama as a third-party gateway provider"
  repos/ollama/ollama/releases/tags/v0.34.0 | 200 | published 2026-09-05; ChatGPT
    Desktop integration, "Setup is available from the Ollama app on MacOS",
    "structured output performance on Apple Silicon, adds support for
    OpenAI-compatible client tool search and response compaction" — Ch12:102,
    :159, :160 fully verified

OpenAI
  https://openai.com/index/safety-overview-gpt-6-astra/ | 200 (curl) | "Astra is
    our first model to reach the Critical level of cybersecurity capability under
    our Preparedness Framework" VERBATIM; "GPT-6 Astra's monitorability has
    decreased relative to GPT-5.6 Sol." VERBATIM; "remain undetected when
    strategically underperforming in evaluations (sandbagging)" VERBATIM; "We have
    not seen evidence of steganographic CoT reasoning ... the evasion risk may
    largely be bounded to lower reasoning tasks"; "with the right tools and
    access, GPT-6 Astra can find previously unknown security flaws and develop new
    ways to exploit them across many well-protected systems without a person
    guiding each step" VERBATIM (the chapter's "new ways" is correct — it comes
    from this page, not from path-to-astra, which omits "new"); page dated
    September 3, 2026
  https://openai.com/index/gpt-6-astra/ | 403 curl / OK via Exa | ExploitBench
    100% vs 78.5%; ExploitGym 42.4% vs 30.3%; SRE-Bench 88.0% single attempt,
    99.2% within four, vs 55.9% and 68.7%; "rolling out today to a limited set of
    organizations and over the coming days will become available to all ChatGPT
    Plus, Pro, Business, and Enterprise users, as well as through the OpenAI API,
    Microsoft Azure, and AWS Bedrock" VERBATIM; "Astra will refuse to comply with
    more advanced cybersecurity tasks such as creating proof-of-concept exploits";
    "we take the decline seriously" VERBATIM; page title; API pricing; enterprise
    off-by-default (see BLOCKER 3)
  https://openai.com/index/path-to-astra/ | 403 curl / OK via Exa | "It is the
    first model we are designating at this level, and requires stronger safeguards
    during development and before release"; "ExploitBench - Internal Port
    (June-August 2026)" containing "20 high-severity V8 vulnerabilities";
    "discovered and used two zero-day vulnerabilities as part of an exploit chain"
    VERBATIM; "Access to Astra for advanced cybersecurity workflows will initially
    be available to a small group of alpha testers, with access through Daybreak
    Blue expanding afterward"; Published 2026-09-01

Anthropic
  https://www.anthropic.com/threat-intelligence-report-september-2026 | 200 |
    full distillation section returned (see M-09): 5,380 fraudulent accounts,
    almost 300,000 requests over ten days, over 23 million exchanges May-July
    2026, Singapore and Japan, mostly Opus, seven harm areas Dec 2025-Aug 2026,
    DeepSeek cross-session replay against Opus reasoning traces, Zhipu/Z.ai,
    Xiaomi, MiniMax, Alibaba (over 151 million exchanges), SenseTime
  https://www.anthropic.com/engineering/multi-agent-research-system | 200 | see
    the Signal 3 entry above — 90.2%, ~20 queries, rainbow deployments,
    resume-after-error, ~15x tokens, CitationAgent, zero "graph engineering"
  https://platform.claude.com/docs/en/managed-agents/permission-policies | 200 |
    "auto The server evaluates each call and runs it, denies it, or pauses for
    your approval"; "Each toolset kind has its own default: the agent toolset
    defaults to always_allow, and MCP toolsets default to always_ask" (confirms
    Ch07:210 exactly); "auto is not a human checkpoint. If the server determines
    that a call is safe, the call runs before anyone sees it, and its effects
    might not be reversible." (confirms Ch04:38); evaluation object,
    evaluated_permission, reason_code high_risk / indeterminate, agent.tool_use
    and agent.mcp_tool_use; "your client cannot override them"
  https://platform.claude.com/docs/en/release-notes/overview | 200 | September 10,
    2026 entry announcing the auto policy VERBATIM; September 3, 2026 entry
    "Version 1.30.0 of the ant CLI adds ant apply, which creates and updates
    agents, environments, skills, memory stores, and deployments from files in
    your repository" — both dates in Ch04/05/07 CONFIRMED
  https://platform.claude.com/docs/en/cli-sdks-libraries/cli/apply | 200 | "ant
    apply requires CLI version 1.30.0 or later" (confirms the v1.30.0 claim);
    "A skill is a directory with a SKILL.md at its root"; GitHub-URL skill
    references "pinned to the resolved commit until you run with --upgrade";
    "The two hashes fingerprint what was last sent and what the API returned";
    "Resources refer to each other by path ... write the relative path"; --dry-run;
    "Authenticate with Workload Identity Federation rather than a stored API key";
    CI x6, "pull request" x4. Ch05:132 and :193 fully verified.
  https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models
    | 200 | Thariq Shihipar, July 24 2026; "We removed over 80% of Claude Code's
    system prompt for models like Claude Opus 5 and Claude Fable 5 with no
    measurable loss on our coding evaluations"; zero hits for "case study"

arXiv
  https://arxiv.org/abs/2609.05339 | OK | title, Goyal + Ray, 4 Sep 2026, 48
    synthetic histories, +0.0004+/-0.0020, +9.91/-13.28, 4.96 vs 11.90, 80%
    construction-time, 34 of 48 "for one tested direction"
  https://arxiv.org/abs/2608.31057 | OK | title, nine authors, 31 Aug 2026, 55
    trajectories, four categories, four levels, both quoted strings VERBATIM
  https://arxiv.org/abs/2607.26637 | OK | title, 11 authors, 29 Jul 2026, three
    roles, "roughly halve retrieval cost", plus the omitted negative findings
  https://arxiv.org/abs/2607.27834 | OK | title, Hanshuai Cui + 5, 30 Jul 2026,
    60 accepted / 179 rejected, LongMemEval-S and LoCoMo, Ordered PatchTest,
    Temporal Resolver, snapshot journal
  https://arxiv.org/abs/2607.23929 | OK | title, 27 Jul 2026 (v1), eight authors
    with ZERO overlap with MemTxn's six — the chapter's "no author overlap" and
    "three days earlier" both CONFIRMED by name-by-name comparison
  https://arxiv.org/abs/2607.27919 | OK | title, Rubin Wei et al. incl. Qipeng
    Guo / Bowen Zhou / Zhouhan Lin, 30 Jul 2026, 6.9B on 300B tokens, distributed
    Faiss + sparse batch-wise kNN, 17 benchmarks, 29.86 -> 37.34 vs Pythia-12B
    37.24 at 39% fewer parameters — all EXACT
  https://arxiv.org/abs/2508.09874 | OK | "Memory Decoder: A Pretrained,
    Plug-and-Play Memory for Large Language Models", 13 Aug 2025 — the predecessor
    citation at 06:180 is correct
  https://arxiv.org/abs/2608.19652 | OK | real title (see MAJOR), five authors
    matching 11:410 exactly, 20 Aug 2026, 234 scenarios, closed-pool grading,
    1.8x/1.6x figures, +32/+67 and +15/+32
  https://arxiv.org/abs/2607.08124 | OK | title, Jun Nie first author, 9 Jul 2026,
    proposer/judge/solver around one frozen LLM, unlabeled traces, no gold labels
  https://arxiv.org/abs/2607.12227 | OK | title, Yike Wang first author, v1 14 Jul
    2026 / v2 27 Aug 2026 EXACT, matched-budget critique, overfitting risk, plus
    the omitted negative result
  https://arxiv.org/abs/2605.11887 | OK | Boyi Deng first author (the chapter's
    "Deng, Boyi, et al." is CORRECT — the HTML render credits only "Qwen Team",
    the abs page lists 18 named authors led by Boyi Deng), submitted 12 May 2026,
    14 SAE groups across 7 variants
  https://arxiv.org/html/2605.11887v1 | OK | full text, 127 KB — parameter range
    and feature-count checks (BLOCKERs 1 and 2), four directions (MAJOR)

Vendors and press
  https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise-agent-platform
    | 200 | July 30 2026; "agents capable of running continuously for up to 7
    days"; Agent Memory Bank schema extraction; Agent Identity; Agent Gateway;
    Agent Registry (five bullets, see MINOR)
  https://www.salesforce.com/uk/news/stories/agentforce-job-ready-ai-agents/ | 200
    | long-horizon runtime "enabling agents to pursue goals across days and weeks
    instead of completing only a task or interaction"; memory / durable execution
    / dynamic steering; "Hunter is the first agent to run on the long-horizon
    runtime"; Multi-Agent Orchestration "GA now". Agent roster enumerated by
    script: Casey (GA now), Paige (GA now), Carter (GA now), Hunter (Pilot now;
    GA November '26), Marshall (GA now), Piper (GA now), Fin (GA now) = SEVEN
    agents, SIX GA, Hunter the only one in pilot. Ch04:225 and Ch11:434 CONFIRMED
    exactly, including "GA planned November 2026".
  https://www.crowdstrike.com/en-us/press-releases/crowdstrike-unveils-falcon-guardian-ai-agent-security/
    | 200 | September 1 2026, Fal.Con; "discovers known and shadow AI agents
    across Windows and macOS, providing a live inventory of every running and
    dormant agent across the enterprise, who deployed it, and its security
    status"; "Runtime Detection and Response: Detects attacks on agents and
    malicious agent behavior, reconstructs the full execution chain"; no detection
    rate or install base present, as the chapters state
  https://techcrunch.com/2026/09/01/air-raises-50m-... | 200 | $50M; "the first
    round raising $10 million, and the second $40 million. Sequoia led the first
    round, while Greenoaks led the second"
  https://www.securityweek.com/ai-agent-firewall-startup-air-security-... | 200 |
    "more than 17,800 public AI add-ons (representing 6.7M installations) relying
    on untrusted external instruction sources"; skills "impersonating companies
    like Anthropic and OpenAI and designed to bypass security reviews"
  https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview/
    | 200 | every Hy4 figure (see MINOR entry)
  https://eu.36kr.com/en/p/3953230805876099 | 200 | reorg confirmed; "as soon as
    this week" launch line; zero hits for Tencent / WorkBuddy (see two MAJORs)
  https://www.cnbc.com/2026/09/11/chinese-ai-labs-moonshot-deepseek-alibaba-anthropic.html
    | 200 | secondary distillation coverage (superseded by the primary)
  https://dataconomy.com/2026/07/29/chinese-ai-models-openrouter-top-five/ | 200 |
    "Chinese LLMs take top five spots on OpenRouter"; order "Xiaomi's MiMo,
    DeepSeek, MiniMax, Alibaba's Qwen and Moonshot's Kimi" matches the chapters
    exactly; "OpenRouter processes more than 20 trillion tokens a week, and
    Chinese-origin models now account for more than 60% of all routed traffic";
    "V2.5" present, so "MiMo-V2.5" is supported
  https://techbriefly.com/2026/07/29/chinese-ai-models-lead-openrouter-for-first-time/
    | 200 | consistent with Dataconomy; "V2.5" present
  https://finance.yahoo.com/technology/ai/articles/chinese-ai-models-now-capture-020440715.html
    | 200 | "Chinese-origin models now account for 46.4% of routed tokens,
    compared to 35.7% for US-origin models" VERBATIM; does NOT carry the
    September 1 five-model token table
  https://www.kucoin.com/news/flash/chinese-models-dominate-openrouter-weekly-token-usage-ranking
    | 200 | August 5 2026 snapshot, eight of top ten, DeepSeek V4 Flash 0423 at
    692 billion tokens (see MAJOR)
  https://pro.stockalarm.io/blog/openrouter-llm-rankings-investor-analysis | 429 x2
    | RE-SCAN
  https://graphengineerings.com/ | 200 | $6.93 / $19.63, six modules, "not
    presented as formal faculty or endorsers" VERBATIM, footer with Justdoit.work
    + Newark CA address + phone, zero hits for "accredit", zero for "perez"
  https://graphengineerings.com/course/module-2.html | 200 | "Orchestration and
    Multi-Agent Topology"; LESSON 2.1-2.11 enumerated = eleven; "Build a
    support-ticket router: an agent classifies severity ... The branch condition
    must be a unit-testable pure function." (the chapter's ellipsis is a pure
    deletion, acceptable); Lesson 2.11 "Anchors -- and earning the scale"; zero
    hits for "perez"
  https://smartscope.blog/en/blog/graph-engineering-loop-engineering-logic-review/
    | 200 | "Graph Engineering is not the successor to Loop Engineering; it is a
    design lens for connecting multiple loops and agents through shared state,
    branches, permissions, and failure paths." VERBATIM; "As of July 20, the cited
    posts and public materials do not provide a standard definition, ..."; Husain
    title and the 00:34 UTC July 18 2026 Steinberger timestamp; September 1 2026;
    zero hits for "AI-research" / "fact.check"
  https://smartscope.blog/en/about/ | 200 | zero hits for "AI-research" /
    "fact.check"
  https://smartscope.blog/en/ | 200 | zero hits for "AI-research" / "fact.check"
  https://towardsdatascience.com/graph-engineering-for-ai-agents-from-prompts-and-loops-to-workflows/
    | 200 | Nhu Hoang, September 14 2026; "you define the nodes, routing logic,
    and checkpoints in advance" and "the graph decides what happens next" both
    VERBATIM; cites Steinberger and the Husain title; does NOT date the Husain
    essay (see MAJOR)
  https://agentengineering.world/london/ | 200 | "Friday 16 October 2026 Everyman
    Cinema, Crossrail Place, London E14 5AR"; "Talks cover disciplines such as
    context, harness, memory, evaluation, inference, protocols, and agentic
    coding"; "Confirmed names are announced on a rolling basis" with no names on
    the page, supporting "no published speaker list"; zero hits for "graph"


================================================================================
CROSS-FILE CONSISTENCY TABLE
================================================================================

Fact                          | Sites                                  | Verdict
------------------------------|----------------------------------------|--------
GPT-6 Astra date Sept 3 2026  | 04:63, 04:291, 11:420, 11:422, 11:621  | CONSISTENT, correct
Astra ExploitBench 100/78.5   | 04:63, 11:422, 11:621                  | CONSISTENT, correct
Astra ExploitGym 42.4/30.3    | 04:63 (42.4 only), 11:422, 11:621      | CONSISTENT, correct
Astra SRE-Bench 88.0/99.2     | 04:63, 11:422, 11:621                  | CONSISTENT, correct
Astra launch-page title       | 04:291, 11:621                         | INCONSISTENT w/ source (MAJOR)
Daybreak access framing       | 04:63 correct vs 11:422 present-tense   | INCONSISTENT (MAJOR)
dsh 224,004 / 26,637          | 09:75, 09:174, 11:398, 11:612          | CONSISTENT; live API 224,039/26,644 (same-day drift)
dsh 190,630 / 21,319 (Aug 24) | 09:75, 09:174, 11:398, 11:612          | CONSISTENT internally; historical snapshot not re-checkable
dsh MIT / Aug 13 2026         | 09:75, 09:174, 11:398, 11:612          | CONSISTENT, API-confirmed
dsh subagent package names    | 09:75, 09:174, 11:398, 11:612          | CONSISTENT, package.json-confirmed EXACT
Codex rust-v0.142.0 Jun 22    | 14:67, 14:199                          | CONSISTENT, API-confirmed
Codex PR merge dates 19/22 Jun| 14:67, 14:198                          | CONSISTENT, API-confirmed
Codex lead-in interval        | 14:67 "seven weeks" vs 14:67 body "a
                                month", 01:173 "a month", 14:179 "a
                                month"                                  | INCONSISTENT (MAJOR)
headcount 16 depts/172 skills | 14:73, 14:200                          | CONSISTENT, README-confirmed VERBATIM
headcount stale 15+/125+      | 14:73, 14:200                          | CONSISTENT, API description-confirmed
Memory Bank GA Jul 30 2026    | 04:225, 04:296, 06:137, 06:183, 11:368,
                                11:370, 11:618                          | CONSISTENT, correct
Agent Runtime 7 days          | 04:225, 06:137, 11:370, 11:618         | CONSISTENT, correct
GEAP capability count         | 11:370 "four" vs blog's five bullets    | INCONSISTENT w/ source (MINOR)
Goyal/Ray +0.0004+/-0.0020    | 02:101, 02:224, 06:117, 06:181, 11:426,
                                11:622                                  | CONSISTENT, correct
Goyal/Ray 34 of 48            | 06:117, 06:181, 11:426, 11:622         | CONSISTENT internally; all four drop "for one tested direction" (MAJOR)
Goyal/Ray paper title         | 02:224, 06:181, 11:622                 | CONSISTENT; all three use a paraphrase, not the title (MAJOR)
StateMem 1.8x / 1.6x          | 06:131, 06:182, 11:410, 11:619         | CONSISTENT, numbers correct; comparator conflated in all four (MINOR)
MemTxn 60 / 179               | 06:83, 06:179, 11:366, 11:617          | CONSISTENT, correct
MemTX Jul 27, no author overlap| 06:83, 06:179, 11:366, 11:617         | CONSISTENT, name-by-name confirmed
Memory Decoder 29.86->37.34   | 06:91, 06:180, 11:366, 11:617          | CONSISTENT, correct
Anthropic distillation 5,380 /
  ~300k / 23M                 | 09:135, 09:179, 11:430, 11:623         | CONSISTENT, primary-confirmed
"did not return on fetch"     | 09:137, 09:179, 11:430, 11:623         | CONSISTENT internally, WRONG vs source (MAJOR)
auto policy Sept 10 2026      | 04:38, 04:292, 07:154, 07:210          | CONSISTENT, release-notes-confirmed
auto reason codes / events    | 04:38, 04:292, 07:154, 07:210          | CONSISTENT, docs-confirmed
ant apply Sept 3 / v1.30.0    | 05:132, 05:193                         | CONSISTENT, docs+release-notes-confirmed
AIR $50M / 10 Sequoia / 40
  Greenoaks                   | 05:165, 05:192, 11:418, 11:620         | CONSISTENT, correct
AIR 17,800 / 6.7M             | 05:165, 05:192, 11:418, 11:620         | CONSISTENT; "and skills" added in 05 (MINOR)
Falcon Guardian Sept 1        | 05:165, 05:191, 11:418, 11:620         | CONSISTENT, correct
Salesforce 7 agents / Hunter
  pilot / GA Nov 2026         | 04:225, 04:295, 11:432, 11:434, 11:624 | CONSISTENT, roster-enumerated, correct
OpenRouter 60% (July)         | 09:131, 09:180, 11:362, 11:616         | CONSISTENT, Dataconomy-confirmed
OpenRouter 46.4% / 35.7%      | 09:131, 09:180, 11:362, 11:616         | CONSISTENT, Yahoo-confirmed
OpenRouter Sept 1 top five    | 09:131 (names only), 11:362 (names +
                                token figures)                          | INCONSISTENT in depth; token figures unverified (MAJOR)
SmartScope rebuttal thesis    | 14:93, 14:155, 14:202, 14:173          | CONSISTENT, VERBATIM-confirmed
SmartScope reversal reading   | 14:93, 14:177 ("the obituary under
                                dispute is loop engineering's")         | CONSISTENT, source-confirmed — the Ch14 correction is RIGHT
TDS Sept 14 / pre-committed
  control flow                | 14:131, 14:173, 14:203                 | CONSISTENT, VERBATIM-confirmed
Graph-engineering survival
  verdict                     | 01:173, 14:9, 14:179, glossary:75      | CONSISTENT across all four; wording matches
Signal 1 NOT-MET (no vendor
  product vocabulary)         | 01:173, 14:170, 14:179, 14:181,
                                glossary:75                             | CONSISTENT; zero-hit greps on Codex PRs, three Codex releases, headcount README and the Anthropic multi-agent post all support it


================================================================================
WHAT WAS CHECKED AND FOUND CLEAN (so the absence of a finding is legible)
================================================================================

- Chapter 14 section 14.7 scorecard, all four rows: every evidence string in
  every cell traced to a fetched source. Signal 3's "MET, retrospectively" is
  the strongest cell and it holds completely (90.2%, ~20 queries, rainbow
  deployments, resume-after-failure all VERBATIM from the June 2025 Anthropic
  post, which indeed never says "graph engineering"). Signal 2's course evidence
  holds apart from "Perez's" and "no company". Signal 4's two September pieces
  both fetched and both say what the chapter says they say. Signal 1's absence
  claims survived every grep run against them.
- The `auto` permission-policy material in Chapters 4 and 7 is the cleanest
  block in the wave: every identifier, reason code, event name, default and
  caveat matched the documentation, including the subtle one ("auto is not a
  human checkpoint").
- Salesforce: the "seven agents / six GA / Hunter only pilot" claim looked like a
  count error and is not — the page carries nine "GA now"/"Pilot now" markers, but
  two belong to non-agent capabilities. Enumerated rather than assumed.
- Ollama v0.33.0 / v0.34.0: dates and feature lists exact.
- Tencent Hy4: every one of nine figures exact.
- MemTX / MemTxn independence: verified by comparing all fourteen author names.
- "MiMo-V2.5": the version suffix is present in both July sources, so it is not
  the unverifiable-version-number error the last wave was caught on.
- Sources hygiene, verified by script rather than by eye:
    Chapter 6 numbered sources now run 1-29 with zero gaps and zero duplicates
    (master ended at 23; the wave adds 24-29 contiguously).
    Chapter 7 runs 1-24, zero gaps, zero duplicates (the wave adds 24).
    Chapter 11 and Chapter 14 use dash lists, format-consistent with their
    existing entries.
    Grep over all 179 added lines for internal-process vocabulary — VENDOR-CLAIM,
    PIN-DATE, SECONDARY-ONLY, UNFETCHED, "fact-sheet", "researcher", "Seat <n>",
    "W<n>", TODO, TBD — returns zero hits.
    Exactly one "..." appears in the added lines (14:91), and it is a legitimate
    elision inside the course quote, deleting text rather than substituting for
    it. No unfinished sentences.
