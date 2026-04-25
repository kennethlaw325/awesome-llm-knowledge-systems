# Contributing

This guide is **not an awesome list.** It is an opinionated, structured synthesis of how LLM knowledge engineering evolved between 2022 and 2026. The goal is not breadth of links — it is a coherent map. Contributions that strengthen the map are welcome; contributions that just add entries are not.

If you want to add an item, read the inclusion criteria below before opening a PR.

---

## What the guide tracks

The repo is organized around ten axes the framework treats as load-bearing:

1. **Layered evolution** — prompt → context → harness (Ch01)
2. **Knowledge layer** — RAG, long context, knowledge graphs (Ch02)
3. **Context engineering** — what surrounds the call (Ch03)
4. **Harness engineering** — orchestration as the OS layer (Ch04)
5. **Skill systems** — discovery, composition, progressive disclosure (Ch05)
6. **Agent memory** — short-term, long-term, graph, learned (Ch06)
7. **MCP and interop** — protocols and standards (Ch07)
8. **Tools landscape** — production frameworks (Ch08)
9. **China ecosystem** — open-weight inflection, sovereign silicon, Chinese-language frontier (Ch09)
10. **Local models** — small or local deployment patterns (Ch12)

Plus **interpretability** and **test-time compute**, treated as cross-cutting concerns that surface in Ch04 (harness) and Ch11 (timeline).

If a proposed addition does not move along one of these axes, it does not belong here. There is no "miscellaneous" lane.

---

## The inclusion test

A single question decides whether something gets added:

> **Does this event introduce, validate, or operationalize a primitive, pattern, or narrative beat that the framework tracks?**

If the answer is yes, propose it. If the answer is "it's notable" or "people are talking about it," that is not the bar. The repo's value is editorial selection; entries that pass only on news-worthiness dilute it.

---

## By event type

Different kinds of events face different bars. The implicit pattern from existing entries:

### Model releases

**In:** First-of-a-kind capability (ChatGPT, Gemini 1.0 multimodal), new economic point (DeepSeek R1's $6M training), new context-window class (Gemini 1.5's 1M, Kimi's 2M Chinese), new distribution model (Mythos's Glasswing coalition), new modality-fusion architecture (ERNIE 5.0).

**Out:** Version bumps. The repo does not include Claude 3.5 / 3.7 / 4 / 4.5 / 4.6, GPT-5.x base, Gemini 2.x, the Llama series, etc., even when individually impressive — they extend rather than redefine.

A version bump qualifies *only* when it ships a new primitive (e.g., Claude Opus 4.7's task budgets are a new harness contract, not a model improvement).

### Protocols and standards

**In:** New primitive (SEP-1686 Tasks, AgentCore bidirectional MCP), cross-vendor convergence (agentskills.io adopted by Anthropic, OpenAI, Google), scale milestones that shift the interop story (MCP 8M, MCP 97M downloads).

**Out:** Routine spec revisions, maintainer churn, governance procedural changes.

### Primary research papers

**In:** New result, new architecture, new measurement axis, or first operational case (Meta-Harness's 6x harness gap, CATTS's vote-derived uncertainty, Titans+MIRAS as trainable memory, OpenAI's first CoT-monitoring catch).

**Out:** Incremental benchmarks on existing axes, replications, ablations.

### Survey and synthesis papers

A tighter bar — see the Academic Policy section below. Most do not get in.

### Products and harness primitives

**In:** Productizes a research idea (the Advisor Tool exposing the Stanford / MIT / KRAFTON harness gap as a tool call), exposes new architecture (the Claude Code source leak revealing self-healing memory), or makes the framework empirically visible (Notion 3.0 as evidence of mainstream convergence).

**Out:** Vertical applications that don't introduce a primitive (a design assistant or vertical agent product is not, by itself, a knowledge-engineering primitive).

### Market events

**In:** Narrative shift (the AI Velocity Paradox report reframing eval, not generation, as the bottleneck), structural acquisitions that signal infrastructure becoming strategic (Meta's $2B Manus acquisition).

**Out:** Funding rounds, valuation news, partnership announcements absent a structural shift. Investment headlines without a structural argument do not qualify, regardless of dollar amount.

---

## Academic policy

The README opens with: *"I analyzed 50+ awesome lists, surveys, and guides — none of them connected the dots."* The repo's existence claim is that surveys missed the synthesis. This creates a deliberate tension with how academic synthesis is treated.

Two lanes apply to academic work:

| Lane | Bar | Where it goes |
|---|---|---|
| **Primary research** | New result, architecture, or first operational case. | Ch11 timeline entry **and** chapter body where the framework is affected. |
| **Synthesis / framing** | (i) flagship-level visibility (large author group, top venue, or strong community signal), **and** (ii) introduces, contests, or independently arrives at a framing the repo uses. | Chapter body framing context only. **Not added to the timeline.** Cited as evidence the practitioner thesis converged with academic literature, or as a foil where the academic frame misses something. |

Surveys that summarize the field without doing either of (i) or (ii) are declined. Surveys that name a primitive the field will adopt, or that frame the conversation in a way readers will encounter, get cited in the relevant chapter — without timeline entries.

---

## Where content goes

| Content type | Location |
|---|---|
| Event with a date | Ch11 timeline. Absolute dates where known; quarter or month otherwise. |
| Concept, framework, or pattern | The relevant chapter body. Add to multiple chapters only when it cuts across (e.g., interpretability touches Ch04 and Ch11). |
| New term | `glossary.md`. Define on first appearance; cross-link from the chapter body. |
| External reference | The chapter's `Sources` section. Prefer primary sources (vendor blog, arXiv, official spec) over secondary commentary. |
| Translation | `translations/` folder. Translations follow the English version, they do not lead it. |

---

## Sourcing standards

- **Dates:** absolute when available (e.g., "April 16, 2026"), otherwise month or quarter. No relative dates ("last week", "recently").
- **Sources:** primary first. Vendor blog → official spec → reputable secondary outlet, in that order. Secondary-only sources are flagged for verification.
- **Numbers:** cited with source. Performance claims, download counts, valuations all need a verifiable link.
- **Speculation:** marked clearly. The repo prefers under-claiming over over-claiming.

---

## How to propose

For substantive additions (new timeline entry, new chapter section, new glossary term):

1. Open an **issue** first describing the proposed addition and which inclusion criteria it meets.
2. After alignment, open a PR.

For editorial fixes (typos, broken links, formatting, source updates):

1. Open a PR directly.

PRs that add entries without engaging with the inclusion criteria may be closed with a pointer to this document.

---

## Code of Conduct

Be direct. Disagreement on inclusion is welcome — argue from the criteria, not from "but this is interesting." Keep discussions about the work, not about people.
