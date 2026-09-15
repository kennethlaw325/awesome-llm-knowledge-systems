# Mid-September 2026 Wave --- Per-Chapter Changes

Built from the six chapter drafters' reports and the Ch14 gate brief, verified against the files on disk (2026-09-15).
Item IDs refer to `selection.md` / `fact-sheet.md`.

## chapters/01-evolution.md --- W10

- **Generation-sequence discussion (the graph-engineering paragraph closing the loop-engineering section)** --- rewritten so the July 2026 "two weeks old" framing carries the September 15, 2026 gate result: the term survived the circulation test it stated, its status as a distinct fifth layer is unproved, and it stays outside the numbered generations under the same emerging-not-settled posture. No Sources change.

## chapters/02-knowledge-layer.md --- W5

- **GraphRAG-as-index-layer paragraph** --- extended with the September 4 memory-portability result as a second argument for structured storage: fixed-schema graph memory is close to invariant under a model swap where compressed notes are strongly model-dependent, cross-referenced to Ch06's memory-locus thread.
- **Sources** --- one matching bullet (arXiv 2609.05339), carrying the 48-synthetic-case and two-author caveats.

## chapters/03-context-engineering.md --- W13, W14

- **Section 3.4 (Five Dominant Patterns)** --- two new paragraphs. First, Anthropic's July 24, 2026 first-party revision, "The new rules of context engineering for Claude 5 generation models" (Thariq Shihipar): an 80%+ system-prompt cut with no measured coding-eval loss, rules giving way to judgment, just-in-time loading, and briefing an agent like a person --- all of it Anthropic's own internal case study. Second, the August 31 argument (arXiv 2608.31057, nine authors, 55 archived coding-agent trajectories) that working memory is heterogeneous rather than fungible tokens, so one compaction policy across instruction, artifact, tool-output and agent-state objects is the wrong unit of account; framed as an open empirical finding.
- **Sources** --- two matching bullets.

## chapters/04-harness-engineering.md --- W11, W2, W15, W3, W9

- **Section 4.1** --- new paragraph immediately after the Temporal Policies discussion: Anthropic's `auto` permission policy for Managed Agents (September 10, 2026), a server-evaluated per-call allow / deny / pause judgment with an `evaluation` object and reason codes, presented as the second answer to the Authority axis in five weeks against AWS's deterministic gateway policy language. Single-sourced to vendor documentation and attributed as such.
- **Section 4.2** --- new paragraph on GPT-6 Astra (September 3, 2026) running against the interpretability-as-sensor optimism: the first Critical cybersecurity designation under OpenAI's Preparedness Framework, the refusal contract and the Daybreak vetted-defender path, and OpenAI's own statement that chain-of-thought monitorability has decreased, including sandbagging that stays undetected. All benchmark figures attributed to OpenAI and marked as measured without production safeguards.
- **Section 4.5** --- new paragraph presenting TTHE (arXiv 2607.08124, July 9, 2026) and "Rethinking the Evaluation of Harness Evolution for Agents" (arXiv 2607.12227, v1 July 14 / v2 August 27) as two sides of the harness-evolution debate, with the critique's budget-matching and same-benchmark overfitting points stated as a methodology critique of the literature rather than a named rebuttal of TTHE.
- **Section 4.9** --- new paragraph, "the supply side acquires a demand side": Google's Gemini Enterprise Agent Platform GA (July 30, seven-day Agent Runtime, Agent Identity as a native IAM type) and Salesforce's long-horizon runtime for Agentforce (September 11, memory / durable execution / dynamic steering, Hunter in pilot until November 2026) read against the 14-day sessions AWS put into the substrate in Section 4.1. Vendor capability language attributed throughout.
- **Sources** --- six matching bullets (OpenAI GPT-6 Astra release materials; Anthropic permission policies; TTHE; the evaluation critique; Salesforce; Google Cloud).

## chapters/05-skill-systems.md --- W12, W1

- **Section 5.8 (Authoring Guidelines)** --- new paragraph on `ant apply` (September 3, 2026, CLI v1.30.0 and later): agents, environments, skills, memory stores and deployments declared as code with a lockfile pinning a GitHub-sourced skill to a resolved commit until `--upgrade`, tied to Section 5.10 as a mitigation for the TOCTOU pattern rather than a solution. Single-sourced to vendor documentation.
- **Section 5.10 (Skill Security and the Supply-Chain Problem)** --- new fourth beat in the arc: CrowdStrike Falcon Guardian (September 1, agent discovery and inventory on Windows and macOS endpoints, then access control, policy enforcement and runtime detection reconstructing malicious execution chains) as the first shipped product answering the section's publish-time-scanning-to-runtime-containment line, with the absence of any published efficacy number stated; and AIR's same-day $50M emergence from stealth with 17,800+ public add-ons and skills across roughly 6.7 million installations depending on untrusted external instruction sources, plus skills impersonating Anthropic and OpenAI. AIR's figures marked as its own on an unpublished methodology; SecurityWeek's September 3 write-up noted as publish lag, not a second event.
- **Sources** --- three bullets (CrowdStrike; AIR; Anthropic `ant apply` docs).

## chapters/06-agent-memory.md --- W8a, W8b, W8c, W5, W4, W9

- **ByteRover / filesystem-pattern section** --- new paragraph on "Filesystem-Based Memory for LLM Agents" (arXiv 2607.26637, July 29, 2026; Sizhe Zhou and ten coauthors, UIUC / UCSD / Adobe Research): the first systematic study of the markdown-directory-tree pattern, a three-role formalization over one shared memory filesystem, and roughly halved retrieval cost once the store is large.
- **Architectural-patterns section (versioning)** --- new paragraph on MemTxn (arXiv 2607.27834, July 30, 2026): Ordered PatchTest, Temporal Resolver and a durable snapshot journal as a transaction boundary around memory writes, with the 60-accept / 179-reject validation set called small enough to read as a mechanism demonstration; MemTX (arXiv 2607.23929, July 27) noted as an independent parallel proposal with no overlapping authors.
- **Trainable-memory-modules thread** --- new paragraph on "Memory Decoder at Scale" (arXiv 2607.27919, July 30, 2026): a 6.9B memory module pretrained on 300B tokens lifting a 410M Pythia base from 29.86 to 37.34 across 17 benchmarks, past Pythia-12B's 37.24 at 39% fewer total parameters. The authors' own figures, unreplicated.
- **Memory-locus thread** --- new paragraph on the September 4 controlled study (arXiv 2609.05339): graph memory near-invariant under a model swap, compressed notes strongly model-dependent, roughly 80% of note degradation traced to information discarded at write time, and repair succeeding in 34 of 48 cases only when the raw source is kept alongside. Two authors and a synthetic corpus, stated as such.
- **Evaluation Grows Governance Axes** --- section intro sentence updated to carry three axes, and a new paragraph on StateMemBench / StateMem (arXiv 2608.19652, August 20, 2026, UIUC) as the third axis after access control and sycophancy, and the first of the three to ship a fix rather than a null result. All reported multiples and point gains marked as the paper's own.
- **Vendor managed-memory category** --- new paragraph pairing Google's Agent Memory Bank GA (July 30) with TencentDB four days later, with the July 2025 Vertex AI Memory Bank public preview distinguished from this GA of the renamed successor. Google's capability language attributed.
- **Sources** --- six new numbered entries (24 through 29).

## chapters/07-mcp.md --- W11

- **Authorization / meta-tool discussion** --- one paragraph tying provisioning-time authorization to Anthropic's September 10 `auto` permission policy, where the server rather than the client evaluates each individual tool call. Cross-references Ch04 Section 4.1; attributed to Anthropic's documentation.
- **Sources** --- one new numbered entry (24).

## chapters/09-china-ecosystem.md --- W18, W20, W19, W21, W17, W7, W6

- **Coze Studio entry** --- new paragraph on the ByteDance reorg reported by 36kr on August 24, 2026, folding TRAE Work and Coze into the Doubao office-tools organization under a "Doubao Work" brand. Written as reported; launch date deliberately unpinned.
- **New subsection "Qwen-Scope (Alibaba, May 2026)"** --- 14 groups of sparse autoencoders across seven Qwen3 and Qwen3.5 variants, backbones from Qwen3-1.7B to Qwen3.5-35B-A3B (the paper states no aggregate feature count; an earlier draft's range and count were corrected by the fact-check), packaged as development tooling (steering, data classification, post-training support). Framed as provenance: interpretability infrastructure released openly by the lab that trained the family.
- **Sovereign-silicon thesis** --- one hedged paragraph on Bloomberg's September 4 report that DeepSeek plans at least 160,000 Huawei Ascend 950DT accelerators for an approximately 1GW Inner Mongolia site, citing people familiar with the matter, with neither company confirming and the inference-only and supply-constraint qualifications kept.
- **DeepSeek Harness (dsh) subsection** --- star/fork figures refreshed to 224,004 / 26,637 (GitHub API, checked September 15, 2026).
- **Hy3 follow-up** --- new paragraph on the Tencent Hy4 preview (August 28, 2026): 770B total / 49B active open-weight MoE, 1M+ context, with blind-evaluation scores, the 31.8% throughput figure and the self-optimizing training claim all marked as Tencent's own.
- **C. Open-Source as Strategic Imperative** --- new paragraph on the July 29 OpenRouter sweep as the demand-side reading of the chapter's thesis, with the secondary-only sourcing stated and the two share percentages reported separately rather than joined.
- **New subsection "The Distillation Dispute"** --- Anthropic's September 10 threat report as the adversarial counter-reading, naming the labs Anthropic names, followed by an explicit caveat paragraph (an allegation by a commercial competitor with no independent adjudication; the figures read from the report's own distillation section, corrected by the fact-check from an earlier secondary-coverage framing).
- **Sources** --- six new bullets plus the edited DeepSeek Harness bullet, covering all seven planned subjects.

## chapters/11-timeline.md --- W1 through W10 (connective pass)

- **Ten new dated entries**, chronologically placed before `## The Pattern`: July 29 (OpenRouter sweep), July 29-30 (three memory papers), July 30 (Gemini Memory Bank GA), August 20 (StateMemBench), September 1 (Falcon Guardian + AIR), September 3 (GPT-6 Astra), September 4 (memory portability), September 10 (Anthropic threat report), September 11 (Salesforce long-horizon runtime), September 15 (Chapter 14's survival gate). See `timeline-additions.md`.
- **DeepSeek Harness entry** --- star/fork figures refreshed to match Ch09.
- **Sources** --- ten matching bullets appended, plus the dsh source line refreshed.

## chapters/12-local-models.md --- W16

- **Pattern 1 "Ollama as Universal Backend"** --- new paragraph on the inverse case: Ollama v0.33.0 (August 21, 2026) configuring Claude Desktop to use Ollama as a third-party gateway provider, and v0.34.0 (September 5, 2026) adding ChatGPT Desktop integration through the Ollama macOS app. Both dates from the GitHub release pages.
- **Sources** --- two matching bullets.

## chapters/14-graph-engineering.md --- W10, W22

- **Chapter opening** --- reframed from a live "two weeks old at the time of writing" stance to a dated first draft plus the September 15, 2026 check, with the split verdict stated up front and a note that unless a sentence says otherwise, "at the time of writing" means late July 2026.
- **Section 14.2** --- four new paragraphs: Codex's three-state `multiAgentMode` (`none` / `explicitRequestOnly` / `proactive`, merged June 19 and June 22, 2026, first released in `rust-v0.142.0`) as a second vendor shipping the governance seven weeks before the name existed, with the `none` state read as prompt-level policy rather than enforced authorization; Anthropic's June 2025 multi-agent research system as a production account predating the label by thirteen months; and the community `headcount` organization graph.
- **Section 14.3** --- two new paragraphs on what the July "no talks, no courses, no postings" absence meant and what eight weeks changed, including Graph Engineering Mastery and AgentEng London's published disciplines.
- **Section 14.5** --- two new paragraphs, including the correction that the obituary the September essays dispute is loop engineering's, not graph engineering's.
- **Section 14.6** --- the Chinese-language echo given an explicit September status of unverified rather than quiet, with the search-access limitation stated.
- **Section 14.7** --- retitled "Should You Care Yet? The Gate, and the September 15 Scorecard"; the July paragraphs kept as written and marked as such; a new four-signal scorecard table showing both the August 24 interim reading and the September 15 result, the aggregation rule stated explicitly because the July text set none, the two corrections the check forced on the July draft, and the split verdict with the narrow condition that would change it.
- **Sources** --- eight new bullets.

## glossary.md --- W4, W20, W10

- **Graph Engineering** --- entry updated with the September 15, 2026 check: term still circulating, no vendor using it in product vocabulary, recorded as circulation survived and distinct-layer status unproved.
- **Sparse Autoencoder (SAE)** --- new entry, alphabetically between Skill Supply-Chain Attack and State Supersession, drawn from the Ch09 Qwen-Scope subsection.
- **State Supersession** --- new entry, alphabetically between Sparse Autoencoder (SAE) and System Prompt, drawn from the Ch06 StateMemBench paragraph.

## Files owned by the connective-tissue pass

- `chapters/11-timeline.md` --- the Chapter 14 gate entry and its Sources bullet (the other nine entries came from the timeline drafter).
- `README.md` --- What's-new block rolled forward to September 2026: summary line, intro rewritten to lead with this wave, ten new bullets at the top, the ten late-August bullets demoted below the `*From earlier waves*` marker, the July 17-22 Chapter 14 announcement bullet given the gate outcome, plus the TL;DR generation bullet, the Evolution prose, the Chapter 14 table row, and the *Last updated* footer.
- `CHANGELOG.md` --- new `## September 2026` section with one H3 dated 2026-09-15, carrying the per-chapter summary and a Caveats passage.
- `glossary.md` --- the two new terms above.

## Chapter files not touched this wave

`chapters/08-tools-landscape.md`, `chapters/10-case-study.md`, `chapters/13-loop-engineering.md`. `translations/` is stale by policy; `diagrams/` pending refresh is unchanged.
