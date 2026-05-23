# PR — May mid-2026 update — 3 timeline entries + 1 augment + 6 chapter expansions

**Status:** Draft. Branch `update/may-mid-2026`. NOT pushed, NOT opened as PR.
**Generated:** 2026-05-15 HKT.

---

## Title (under 70 chars)

`May mid-2026 update: 3 timeline entries, 1 augment, 6 chapter expansions`

---

## Summary

- **Timeline:** 3 new entries — AWS MCP Server GA (May 6), Code with Claude (Dreaming + Outcomes + Multiagent Orchestration, May 6), AWS AgentCore Payments preview / x402 (May 7). Plus 1 augment of the existing April 7 Mythos entry with the May 11 GPT-5.5-Cyber Trusted Access parallel (Glasswing pattern reproducing on OpenAI's side).
- **Chapter 04 (Harness Engineering):** 3 insertions — Dreaming extending self-healing memory lineage in §4.6; managed MCP edge as third cloud-native primitive in §4.9; deterministic infrastructure-enforced harness contract (x402) in §4.1.
- **Chapter 05 (Skill Systems):** 1 paragraph in §5.9 noting AWS as the fourth Skills-adopting vendor (cross-vendor convergence widens).
- **Chapter 06 (Agent Memory):** 1 paragraph under "Trainable Memory Modules" naming the trainable-vs-curated dichotomy (Titans+MIRAS vs Dreaming).
- **Chapter 07 (MCP):** AWS MCP GA added as the scale-milestone post-97M-downloads; x402 added as cross-protocol value layer ("MCP for tools, x402 for value").
- **Chapter 08 (Tools Landscape):** 1 paragraph appended to the AI Velocity Paradox section noting that the managed substrate now learns and self-corrects.
- **Glossary:** 3 new terms — Dreaming, Outcomes (Anthropic), x402.

## Per-chapter change summary

| Chapter | File | Change |
|---------|------|--------|
| 04 Harness Engineering | `chapters/04-harness-engineering.md` | §4.1 deterministic-infrastructure contract paragraph, §4.6 Dreaming paragraph, §4.9 managed MCP edge paragraph, 2 sources added |
| 05 Skill Systems | `chapters/05-skill-systems.md` | §5.9 fourth-vendor (AWS) paragraph + 2 sources |
| 06 Agent Memory | `chapters/06-agent-memory.md` | "Trainable Memory Modules" trainable-vs-curated paragraph + 2 sources |
| 07 MCP | `chapters/07-mcp.md` | "Timeline: From Launch to Linux Foundation" AWS MCP GA addition; "MCP for tools, x402 for value" cross-protocol paragraph; 3 sources added |
| 08 Tools Landscape | `chapters/08-tools-landscape.md` | Velocity Paradox section managed-substrate-learns-and-self-corrects paragraph + 2 sources |
| 11 Timeline | `chapters/11-timeline.md` | 3 new entries + 1 augmentation; ~14 new source URLs |
| Glossary | `glossary.md` | 3 new terms added |

**No changes to:** README, Ch01, Ch02, Ch03, Ch09, Ch10, Ch12, diagrams, translations, CHANGELOG.

## Diff size estimate

- ~+130-160 lines added across content
- ~14 new source URLs in Ch11 Sources; additional sources in other chapter Sources blocks
- All sources are primary or first-tier secondary

## Test plan

- [ ] Markdown link check on changed files
- [ ] Table-of-contents validity in `chapters/11-timeline.md` (April → May 6 AWS MCP → May 6 Code with Claude → May 7 AWS Payments — chronologically ordered)
- [ ] `## Sources` blocks in Ch04, Ch05, Ch06, Ch07, Ch08, Ch11 — each new entry has a primary URL
- [ ] Glossary entries land in correct alphabetical sections (new D and X sections added)
- [ ] CONTRIBUTING.md inclusion criteria still consistent with the new Tier 1 entries

## Sources index

See `docs/may-mid-2026-update/timeline-additions.md` for the full source URL table.

## What this PR does NOT do

- No diagram update (timeline.png stays as-is)
- No translation file changes (English-only first wave per locked scope)
- No README change
- No CHANGELOG update

## Caveats

- OpenAI primary URL (`openai.com/index/gpt-5-5-with-trusted-access-for-cyber/`) may 403 against crawlers; CNBC secondary is the load-bearing source for the Mythos augment.
- AWS AgentCore Payments URL slug contains `/04/` but the launch is May 7, 2026 — preserved as user-supplied.

## Reviewer focus areas

1. **Same-day ordering for May 6** — AWS MCP GA placed before Code with Claude (narrative-flow choice: infra/substrate consolidation first, then primitives sitting on top). Reverse order would also be defensible.
2. **Cross-chapter framing** — Ch04 §4.1 deterministic-infrastructure-contract paragraph references Ch11 May 7 entry; verify the forward-reference reads well.
3. **Glossary section headers** — New `### D` (between C and E) and `### X` (between W and end) sections required.
