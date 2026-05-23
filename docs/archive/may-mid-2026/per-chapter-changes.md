# May mid-2026 update — Per-Chapter Change Proposals

**Status:** Draft proposals only. Branch: `update/may-mid-2026`.
**Generated:** 2026-05-15 HKT.

---

## Summary table

| Chapter | File | Change type | Lines added (approx) | Source URL count |
|---------|------|-------------|----------------------|-------------------|
| 04 | `chapters/04-harness-engineering.md` | 3 insertions | ~25 | 2 |
| 05 | `chapters/05-skill-systems.md` | 1 insertion in §5.9 | ~10 | 2 |
| 06 | `chapters/06-agent-memory.md` | 1 insertion in "Trainable Memory Modules" | ~12 | 2 |
| 07 | `chapters/07-mcp.md` | 2 insertions (timeline + adopters) | ~15 | 3 |
| 08 | `chapters/08-tools-landscape.md` | 1 paragraph + 1 sentence | ~10 | 2 |
| 11 | `chapters/11-timeline.md` | 3 new entries + augment Apr 7 | ~45 | ~14 |
| Glossary | `glossary.md` | 3 new terms | ~12 | 0 |

**Total:** approx +130 lines, ~25 sources cited (all primary or first-tier secondary).

---

## Chapter 04: Harness Engineering

### Change 4-A: Augment §4.6 with Dreaming (cloud-managed memory curator)

**Where:** End of §4.6 ("The Claude Code Leak: An Empirical Look (March 31, 2026)"), after the existing paragraph about Routines moving the orchestrator off the laptop (around line 147).

**Why:** §4.6 already establishes the self-healing memory lineage from the March 31 leak (three-layer self-healing memory) and traces it forward through April Routines and April 23 Memory for Managed Agents. Dreaming is the next step in that exact arc — the first cloud-managed background memory *curator*, productizing the consolidation pattern the leak showed running inside Claude Code.

**Proposed insertion (new paragraph appended to end of §4.6):**

> On **May 6, 2026**, Anthropic took the self-healing memory lineage one step further with **Dreaming** (research preview), a scheduled between-session job that reads recent sessions, identifies recurring errors and converged workflows, and rewrites the agent's persistent memory. Where the March 31 leak revealed self-healing memory as a runtime architecture inside Claude Code, Dreaming productizes the *consolidation* pass as managed infrastructure: the curation that happens when the agent is not actively answering a request. Combined with April 23's Memory for Managed Agents (durable cross-session state) and the two other primitives shipped the same day — **Outcomes** (separate-grader self-correction) and **Multiagent Orchestration** (lead-agent fan-out with shared filesystem) — the trajectory is from "memory is data the harness reads" to "memory is a maintained store the substrate keeps in good repair on the agent's behalf." Early pilot data from Harvey reports a ~6x task-completion improvement with Dreaming enabled.

**Source to add:**
- Anthropic. "New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration." May 6, 2026. https://claude.com/blog/new-in-claude-managed-agents

---

### Change 4-B: Augment §4.9 (Cloud-Native Harness Primitives) with managed MCP edge

**Where:** End of §4.9 — append a short paragraph after the existing Memory-for-Managed-Agents / AWS-OpenAI Bedrock paragraph (around line 193).

**Why:** §4.9 frames cloud-native harness primitives. AWS MCP Server GA (May 6, 2026) adds the *managed MCP edge* to the substrate — the boundary at which the harness reaches external tools is now also a vendor-operated primitive.

**Proposed insertion:**

> A third managed primitive landed on the **substrate's outer edge** the same week. On **May 6, 2026**, AWS shipped the **AWS MCP Server** at general availability — the first hyperscaler-managed remote MCP endpoint, exposing 15,000+ AWS API operations through one authenticated server with IAM context keys for fine-grained access and a sandboxed `run_script` tool for server-side Python. For harness engineers, the managed-MCP-edge is the third side of the cloud-native triangle: Managed Agents (where the loop runs) + Memory for Managed Agents (what the loop remembers) + a managed MCP edge (how the loop reaches external tools). Self-hosted MCP servers do not go away, but the centre of gravity for "where do my agents connect to the cloud's APIs" shifts from "one MCP server per service" toward "one managed endpoint at the cloud boundary."

**Source to add:**
- AWS. "The AWS MCP Server is now generally available." May 6, 2026. https://aws.amazon.com/blogs/aws/the-aws-mcp-server-is-now-generally-available/ — 15,000+ API operations through one authenticated server; IAM context keys; sandboxed `run_script` tool.

---

### Change 4-C: Add sentence on x402 / payment harness contract to §4.1 (Defining the Harness)

**Where:** End of §4.1's list of harness components (after the existing bullet list ending "Context assembly pipelines (Chapter 3)" around line 30) — add the new contract as a one-paragraph note rather than as a bullet, since the list is for steady-state components and this is a 2026 development.

**Why:** AWS AgentCore Payments (May 7) introduces a new harness contract: spending budget enforced outside the model, deterministically by infrastructure rather than LLM-judged. This belongs in the chapter that defines what the harness is.

**Proposed insertion (new paragraph after the bullet list):**

> A new class of harness contract appeared in May 2026 with AWS AgentCore Payments (Chapter 11): **deterministic infrastructure-enforced limits on agent action.** Where evaluator-style components soft-enforce by asking another LLM "did this go too far," AgentCore Payments' session-level spending limit is a hard cap at the substrate boundary — the agent simply cannot exceed it, no LLM judgement involved. The pattern generalizes: as substrate primitives like Managed Agents, Memory, and Payments accumulate, the harness contract increasingly includes hard limits that the model cannot reason around, sitting alongside the soft inferential controls that filter what the model says.

**No new source required** (cross-references Ch11 May 7 entry).

---

## Chapter 05: Skill Systems

### Change 5-A: Augment §5.9 (Industry Convergence) with AWS as fourth Skills vendor

**Where:** §5.9 "Industry Convergence: The Google Agent Skills Spec (April 2026)" — append a paragraph after the existing closing line ("'how many tokens does your baseline agent context consume' has become a first-class metric that vendors compete on," around line 137).

**Why:** §5.9's headline is cross-vendor convergence: Anthropic (Oct 2025) → Google (April 2026). AWS MCP Server GA on May 6, 2026 adopts "Skills over SOPs" as the canonical agent entry point — making AWS the first **hyperscaler** to ship Skills as production agent guidance. Four vendors now == industry convention.

**Proposed insertion:**

> The convergence widened again on **May 6, 2026** when AWS shipped its general-availability **AWS MCP Server** and adopted **"Skills over SOPs"** as the canonical agent entry point — the first hyperscaler to ship Skills (the Anthropic / OpenAI / Google open standard from December 2025) as production agent guidance. With four vendors now aligned — Anthropic, OpenAI, Google, and AWS — Skills crosses the threshold from "the convention three frontier labs use" to "the way agent capabilities are described across the cloud stack." For practitioners, the practical effect is that a skill authored against the agentskills.io spec is now portable across the platforms where the majority of production agents run.

**Sources to add:**
- AWS. "AWS MCP Server now generally available." May 6, 2026. https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/
- AWS News Blog. "The AWS MCP Server is now generally available." May 6, 2026. https://aws.amazon.com/blogs/aws/the-aws-mcp-server-is-now-generally-available/

---

## Chapter 06: Agent Memory

### Change 6-A: Augment "Trainable Memory Modules" with trainable-vs-curated dichotomy

**Where:** End of the "Trainable Memory Modules" paragraph under "Architectural Patterns" (around line 83), after the existing Titans / MIRAS framing.

**Why:** The section currently presents Titans+MIRAS as the new pattern alongside data-store memories. Dreaming (May 6, 2026) introduces the *contrasting* commercial direction: instead of writing facts into weight updates via gradient descent at inference (Titans), Dreaming rewrites a plaintext memory store via a scheduled LLM curation pass. These are now the two contrasting commercial directions for long-term agent memory and the chapter should name the dichotomy.

**Proposed insertion (new paragraph after the existing Titans+MIRAS paragraph):**

> A second commercial direction emerged on **May 6, 2026** with Anthropic's **Dreaming** (research preview): instead of training memory into weights at inference time, Dreaming runs a scheduled between-session job that reads recent sessions, identifies recurring errors and converged workflows, and **rewrites the agent's persistent memory in plaintext**. Where Titans makes memory a part of the model itself (updated by gradient descent), Dreaming keeps memory as data the harness reads (updated by an LLM curation pass). The two are now the contrasting commercial templates for long-term agent memory: **trainable memory** (gradient updates at inference, model-internal) versus **curated memory** (LLM-rewritten plaintext, substrate-external). For knowledge engineers the design question sharpens — when is the memory worth burning into weights (Titans), when is it worth keeping queryable as a store the model can read (Mem0, A-MEM, ByteRover, MemPalace), and when is it worth keeping editable as plaintext a curator pass can revise (Dreaming)?

**Sources to add:**
- Anthropic. "New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration." May 6, 2026. https://claude.com/blog/new-in-claude-managed-agents
- Simon Willison. Live blog of Code w/ Claude 2026 SF (May 6, 2026). https://simonwillison.net/2026/May/6/code-w-claude-2026/

---

## Chapter 07: MCP

### Change 7-A: Add AWS MCP Server entry to 2026 (present) section under "Timeline: From Launch to Linux Foundation"

**Where:** End of the "2026 (present)" paragraph in "Timeline: From Launch to Linux Foundation" (around line 21), after the existing "the protocol has become the default integration layer..." sentence.

**Why:** This is the scale-milestone slot. Post-97M-downloads (Q1 2026), the next consolidation moment is AWS shipping the first hyperscaler-managed remote MCP endpoint at GA — the S3-like consolidation moment for the interop layer.

**Proposed insertion (append to existing 2026 paragraph):**

> The protocol's consolidation moment arrived on **May 6, 2026** when AWS shipped the **AWS MCP Server** at general availability — the first hyperscaler-managed remote MCP endpoint, exposing 15,000+ AWS API operations through one authenticated server, with IAM context keys for fine-grained access and a sandboxed `run_script` tool for server-side Python. The Linux Foundation donation (Dec 2025) and 97M downloads (Q1 2026) established MCP as the standard; AWS GA marks the moment the standard becomes infrastructure. The pattern echoes S3's consolidation of object storage: many self-hosted servers do not disappear, but the centre of gravity shifts to "one managed endpoint at the cloud boundary."

### Change 7-B: Add x402 cross-protocol stack note to Adopters / Synthesis-Dimension section

**Where:** After the existing "MCP as a synthesis dimension" paragraph (around line 48), before "Connection to Knowledge Engineering."

**Why:** The Adopters section already lists who speaks MCP. x402 (May 7, 2026) is the first cross-protocol agent stack — "MCP for tools, x402 for value" — and belongs adjacent to the adopters discussion as a protocol-landscape framing rather than an adopter.

**Proposed insertion:**

> **MCP for tools, x402 for value.** On **May 7, 2026**, AWS announced **AgentCore Payments** in preview — the first managed payment primitive for autonomous agents — built with Coinbase and Stripe and built around the **x402** open protocol, which revives HTTP status code 402 ("Payment Required") for in-band stablecoin payment between machines. Coinbase's prior x402 traction — 69,000 active agents, 165M transactions, ~$50M cumulative volume by late April 2026 — meant the protocol had reached scale before the hyperscaler endorsement. With MCP carrying the tool-call layer and x402 carrying the value-transfer layer, agents now have a cross-protocol stack: MCP standardizes how an agent reaches an API, x402 standardizes how it pays the API. The pairing is significant for knowledge engineering because paid resources (premium data, licensed content, gated APIs) become first-class citizens of the agent's action space, with budget enforcement handled deterministically at the protocol layer rather than via LLM-judged rules.

**Sources to add (numbered):**
- AWS. "AWS MCP Server now generally available." May 6, 2026. https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/ and https://aws.amazon.com/blogs/aws/the-aws-mcp-server-is-now-generally-available/
- AWS. "Agents that transact: Amazon Bedrock AgentCore now includes Payments (preview)." May 7, 2026. https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-bedrock-agentcore-payments-preview/ and https://aws.amazon.com/blogs/machine-learning/agents-that-transact-introducing-amazon-bedrock-agentcore-payments-built-with-coinbase-and-stripe/
- x402 specification. https://www.x402.org/ and https://github.com/coinbase/x402

---

## Chapter 08: Tools Landscape

### Change 8-A: Augment the "AI Velocity Paradox" section with managed-substrate raise-the-bar note

**Where:** End of the "And the substrate itself is now portable" paragraph (around line 95), before `## Sources`.

**Why:** The Velocity Paradox section already ends with portable-substrate. The May 6 Code with Claude release adds a second substrate change: managed substrates now bundle a *learning loop* (Dreaming) and a *self-correction loop* (Outcomes). This raises the bar for self-hosted alternatives — generation speed wasn't the bottleneck, evaluation and governance was, and that's exactly where the new managed primitives now compete.

**Proposed insertion (new paragraph appended):**

> **And the managed substrate now learns and self-corrects.** On **May 6, 2026**, Anthropic added three primitives to its Managed Agents substrate — **Dreaming** (scheduled between-session memory curation), **Outcomes** (separate-grader iterate-against-a-rubric loops), and **Multiagent Orchestration** (lead-agent fan-out with shared filesystem) — and on the same day AWS shipped its **MCP Server** at general availability with the first hyperscaler-blessed **Skills** deployment. Read alongside the Velocity Paradox framing, the implication is direct: the bottleneck the report named — evaluation and governance, not generation — is exactly the surface the new managed primitives now compete on. Self-hosted harnesses that scaled generation in 2025 now face managed competitors that scale *learning and grading* in 2026. The Velocity Paradox does not get solved by faster code generation; it gets solved by infrastructure that learns where its own errors recur. That is the substrate Anthropic and AWS just shipped.

**Sources to add:**
- Anthropic. "New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration." May 6, 2026. https://claude.com/blog/new-in-claude-managed-agents
- AWS. "The AWS MCP Server is now generally available." May 6, 2026. https://aws.amazon.com/blogs/aws/the-aws-mcp-server-is-now-generally-available/

---

## Chapter 11: Timeline

See `timeline-additions.md` for full entry text. Summary:

| Operation | Where | Approx lines |
|-----------|-------|--------------|
| Augment existing April 7 Mythos entry with GPT-5.5-Cyber parallel (May 11) | In-place addendum | +4 |
| Insert new entry — May 6, 2026 — AWS MCP Server GA | After Apr 28 / late-Apr cluster | +6 |
| Insert new entry — May 6, 2026 — Code with Claude: Dreaming + Outcomes + Multiagent Orchestration | Immediately after the AWS MCP Server entry | +6 |
| Insert new entry — May 7, 2026 — AWS AgentCore Payments (x402) | Immediately after Code with Claude | +6 |
| Append source URLs to Ch11 Sources block (~14 URLs) | After existing April sources | +14 |

**Ordering rationale (May 6 same-day):** AWS MCP Server GA placed first (infra/substrate consolidation), then Code with Claude (substrate primitives sitting on top of the same managed-substrate posture). This is a narrative-flow judgement; reverse order would also be defensible.

---

## Glossary additions

`glossary.md` should gain three terms.

### Term 1: Dreaming (alphabetical slot — after "Embeddings" before "Emotion Vectors" — section D, or insert new D section)

Actually `glossary.md` has no D section currently. New section header needed:

```
### D

**Dreaming**
A scheduled between-session memory-curation job that rewrites an agent's persistent memory based on recent session patterns. First commercialized by Anthropic Managed Agents (May 6, 2026, research preview): the curator reads recent sessions, identifies recurring errors and converged workflows, and rewrites the agent's persistent memory in plaintext. Contrasts with trainable memory (Titans + MIRAS, April 2026) which adapts at inference via gradient updates: Dreaming keeps memory as data the harness reads, Titans makes memory a part of the model itself.
```

### Term 2: Outcomes (Anthropic) — section O

Currently §O has only "Obsidian." Add:

```
**Outcomes (Anthropic)**
A public-beta managed-agent primitive (Anthropic, May 6, 2026) where the agent iterates against a separate grader running in its own context window until a rubric is satisfied. Productizes the Ralph-loop / CATTS uncertainty-steered iteration pattern as an API contract: the caller writes a rubric, the substrate runs the iterate-and-grade loop on the agent's behalf, and only converged results return to the caller.
```

### Term 3: x402 — section X (new)

Currently no §X. New section header needed (will sit between W and the existing end of file):

```
### X

**x402**
An open protocol reviving HTTP status code 402 ("Payment Required") for in-band stablecoin payment between machines, used for agent-to-resource transactions. Originated by Coinbase; first hyperscaler-managed implementation in AWS AgentCore Payments (May 7, 2026). The "value-layer" analogue of MCP for the tool layer — where MCP standardizes how an agent reaches an API, x402 standardizes how it pays the API. Prior traction before AWS endorsement: 69,000 active agents and ~$50M cumulative volume by late April 2026.
```

---

## What this update does NOT change

For transparency:

- README.md — no change required.
- Chapters 01, 02, 03, 09, 10, 12 — no change required. The proposed additions either land in chapters that already cover the relevant arc, or in the timeline.
- Diagrams — no update proposed.
- Translations — no propagation in this wave (English-only first wave, per locked scope).
- CHANGELOG.md — exists in repo; will be left untouched in this wave (April pattern: separate update).
