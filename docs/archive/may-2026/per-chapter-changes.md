# May 2026 Update — Per-Chapter Change Proposals

**Status:** Draft proposals only. Not committed.
**Generated:** 2026-04-30 HKT.

---

## Summary table

| Chapter | File | Change type | Lines added (approx) | Source URL count |
|---------|------|-------------|----------------------|-------------------|
| 04 | `chapters/04-harness-engineering.md` | Insert + extend | ~25 | 4 |
| 07 | `chapters/07-mcp.md` | Cross-reference only | ~5 | 1 |
| 08 | `chapters/08-tools-landscape.md` | Insert paragraph | ~10 | 2 |
| 11 | `chapters/11-timeline.md` | Insert 4 entries + augment 1 | ~80 | 14 |
| Glossary | `glossary.md` | Add 3 terms | ~6 | 0 |
| README | `README.md` | No change required | 0 | 0 |

**Total:** approx +130 lines, ~21 sources cited (all primary or first-tier secondary).

---

## Chapter 04: Harness Engineering

### Change 4-A: Add subsection to "4.9 Cloud-Native Harness Primitives"

**Where:** After current paragraph ending "...the discipline this chapter has been building toward: knowing which assumption each component encodes, and noticing when the substrate underneath it changes." (line ~185).

**Why:** Section 4.9 currently treats Routines (April 14) as the cloud-native primitive. But Anthropic also shipped **Managed Agents (April 8)** — the *substrate* on which Routines and other harness loops can run. Distinguishing them sharpens the section.

**Proposed insertion:**

> **Routines vs. Managed Agents.** It is worth being precise about what Anthropic actually shipped in April 2026, because the two pieces are sometimes conflated. **Claude Managed Agents** (public beta, April 8, 2026) is the *substrate*: a hosted runtime that exposes sessions (durable context state outside the model's context window), Anthropic-operated sandboxes, scoped tool execution, and tracing. Pricing is **standard token rates plus $0.08 per session-hour** — the first frontier-vendor primitive that meters the orchestrator seat itself, separately from inference. **Claude Code Routines** (research preview, April 14, 2026) is a *triggering surface* that runs on top of that substrate (or compatible alternatives): schedule, API call, GitHub event, with quotas of 5 / 15 / 25 invocations per day for Pro / Max / Team-Enterprise tiers. The two answer different questions. Managed Agents answers "where does the agent loop physically run, and how is its state durably maintained between turns?" Routines answers "what makes the loop start in the first place?" A self-hosted harness that adopts Routines but not Managed Agents keeps owning its state and execution environment; one that adopts Managed Agents but builds its own triggering layer keeps owning when work begins. In practice, most cloud-native harness designs in mid-2026 will adopt both — but the unbundling is the architectural point. Anthropic is no longer selling "the harness" as one thing; it is selling its constituent primitives.

**Sources to add to chapter Sources block:**
- Anthropic. "Claude Managed Agents overview." API documentation. https://platform.claude.com/docs/en/managed-agents/overview
- Anthropic. "Scaling Managed Agents: Decoupling the brain from the body." Engineering blog, April 2026. https://www.anthropic.com/engineering/managed-agents

---

### Change 4-B: Augment Section 4.4 "Harness as Optimization Problem (Meta-Harness)"

**Where:** End of the section that currently closes with the Meta-Harness March 2026 finding.

**Why:** Meta-Harness opened the door; AHE (April 28, 2026) shows the field walked through it. The section as written ends in March; readers in May 2026 will notice the time stamp.

**Proposed insertion:**

> The Meta-Harness paper is now one data point in a fast-moving line. In April 2026, the **AHE paper** ("Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses," arXiv 2604.25850, Fudan / Peking / Shanghai Qiji Zhifeng) reframed the problem from search to *observability*: instead of treating harness configurations as a search space and running an optimizer over it, AHE instruments three observability pillars — component (an explicit, revertible action space), experience (condensed trajectory evidence), and decision (falsifiable edit predictions made before execution) — and lets the harness evolve itself by reading its own runtime signals. After 10 AHE iterations, a Codex-CLI-style baseline at 69.7% pass@1 on Terminal-Bench 2 reaches 77.0%, surpassing the human-designed baseline (71.9%) with **+5.1 to +10.1 pp cross-family gains** when transferred to model families the harness was not optimized on. The cross-family transfer is the structural news: an evolved harness is not over-fit to one model's quirks, it carries forward as the substrate underneath turns over. The Meta-Harness finding ("harness engineering is an optimization problem with a large search space") and the AHE finding ("…and the search can run as a continuous observability loop, not a one-shot optimization") together describe an engineering practice that is rapidly leaving manual tuning behind.

**Source to add:**
- Lin et al. "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses." arXiv 2604.25850, April 2026. https://arxiv.org/abs/2604.25850

---

### Change 4-C: One-line addition to Section 4.8 "Harness Maintenance: The Stress-Testing Imperative"

**Where:** End of section, after the existing CATTS paragraph (line ~173).

**Proposed insertion:**

> The April 2026 AHE result (Section 4.4) makes the same point structurally: stress-testing is not a one-time review activity but a continuous observability loop. Manual stress-testing remains valuable as a discipline practitioners can run today; AHE shows it is also automatable.

**No new source required** (cross-references the source added in Change 4-B).

---

## Chapter 07: MCP

### Change 7-A: Add cross-reference in "MCP Adoption Landscape"

**Where:** After the existing bullet list of adopters (line ~46).

**Why:** AgentFlow (April 2026) demonstrates MCP-style tool integration as one of five harness-synthesis dimensions. MCP is being treated as a search variable, not a fixed substrate. This is a one-paragraph addition, not a new section.

**Proposed insertion:**

> **MCP as a synthesis dimension.** A subtler 2026 development: MCP tool selection is starting to appear as one of the *variables* in automated harness-synthesis systems rather than as a fixed substrate. The AgentFlow paper (arXiv 2604.20801, April 2026) treats agent roles, prompts, *tools*, communication topology, and coordination protocol as five dimensions of a typed-graph DSL its synthesis loop searches over. For an MCP-aware harness designer this is two-edged. MCP's standardization makes the tool dimension genuinely searchable — a synthesis loop can swap one MCP server for another without rewriting the integration layer. But the same standardization makes MCP servers themselves selection candidates: the question is no longer "which servers do I install" but "which servers does my harness *evolve into using* under observability pressure."

**Source to add (numbered list at end of Ch07 Sources):**
- AgentFlow / "Synthesizing Multi-Agent Harnesses for Vulnerability Discovery." arXiv 2604.20801, April 2026. https://arxiv.org/abs/2604.20801

---

## Chapter 08: Tools Landscape

### Change 8-A: Add paragraph to AI Velocity Paradox section

**Where:** End of the Velocity Paradox section (around line ~93), before the `## Sources` heading.

**Why:** The Velocity Paradox is "evaluation and governance is the new bottleneck." The Microsoft–OpenAI restructure (April 27) changes the *commercial* substrate underneath that bottleneck: OpenAI can now serve from any cloud, AGI clauses no longer hold commercial agreements, exclusivity is gone. For a tools-landscape chapter that is partly about which substrate practitioners are building on, this is a one-paragraph addition.

**Proposed insertion:**

> **And the substrate itself is now portable.** On April 27, 2026, Microsoft and OpenAI announced an amended partnership agreement that ended OpenAI's cloud exclusivity to Azure (OpenAI can now serve API access via AWS, Google Cloud, or any provider), capped revenue-share payments asymmetrically, and removed the long-disputed AGI clause that would have let OpenAI exit financial obligations on a unilateral declaration of AGI. For knowledge-engineering teams this matters not as business news but as a substrate change: the largest closed-weight frontier model is no longer locked behind one cloud. "Which cloud do you run on" stops being a constraint on "which models do you have access to" — for the GPT family, at least, on the same terms the open-weight ecosystem already enjoys. Combined with DeepSeek V4's day-one Ascend-NPU support (Chapter 11, April 24), the second half of 2026 begins with portable substrate as the default expectation rather than the exception.

**Sources to add:**
- Microsoft. "The next phase of the Microsoft-OpenAI partnership." April 27, 2026. https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/
- OpenAI. "The next phase of the Microsoft partnership." April 27, 2026. https://openai.com/index/next-phase-of-microsoft-partnership/

---

## Chapter 11: Timeline

See `timeline-additions.md` for full proposed text. Summary:

| New entry | Insertion point | Approx lines |
|-----------|-----------------|--------------|
| Mythos breach (augment existing April 7 entry) | In-place addendum | +6 |
| April 8 — Managed Agents | Between April 7 Mythos and April 14 Routines | +18 |
| April 27 — Microsoft / OpenAI Restructure | Between April 24 DeepSeek V4 and "## The Pattern" | +20 |
| April 28 — AHE paper | Between CATTS and Titans+MIRAS April entries | +18 |
| Late April — AgentFlow | After AHE entry | +18 |

**Plus:** ~14 source URLs added to the timeline's Sources block.

---

## Glossary additions

`glossary.md` should gain three terms.

### Term 1: Managed Agents

> **Managed Agents.** A hosted-runtime model in which the agent harness's substrate — sandboxes, durable session state, scoped tool execution, tracing — is operated by the model vendor rather than the developer. Anthropic shipped the first commercial example in public beta on April 8, 2026 (`platform.claude.com/docs/en/managed-agents/overview`), pricing it at standard API token rates plus a per-session-hour fee for the substrate. Distinct from cloud-native triggering surfaces (e.g. Claude Code Routines), which sit on top of a Managed Agents-style substrate but answer a different question ("what makes the loop start").

### Term 2: Harness Synthesis

> **Harness synthesis.** The class of techniques in which an outer-loop optimizer (search-based, observability-based, or otherwise) automatically modifies a harness — its tools, prompts, role decomposition, communication topology, and coordination protocol — based on runtime signals from the target task. See **AHE** (arXiv 2604.25850) and **AgentFlow** (arXiv 2604.20801) for the two reference April 2026 implementations. Distinct from *meta-harness* (a 2025 / early 2026 framing that treated the harness as a one-shot optimization target rather than a continuously evolving artifact).

### Term 3: Session-hour pricing

> **Session-hour pricing.** A billing model that meters the orchestrator seat — the substrate on which an agent loop runs — separately from inference. First introduced commercially by Anthropic Managed Agents (April 8, 2026) at $0.08 per session-hour on top of standard token rates. Notable because it is the first vendor primitive to put a number on the cost of "where the loop runs," distinct from the cost of "what the loop thinks."

---

## What this update does NOT change

For transparency:

- README.md — no change required. The existing content covers the framework holistically; the updates land in chapter-level depth.
- Chapters 01, 02, 03, 05, 06, 09, 10, 12 — no change required. The proposed additions either land in chapters that already cover the relevant arc, or in the timeline. None of the proposed entries open a new arc that requires fresh chapter-level treatment.
- Diagrams — no update proposed for May. The April timeline.png already covers through April 24. A diagram refresh can wait until at least 2-3 more months of data are in.
