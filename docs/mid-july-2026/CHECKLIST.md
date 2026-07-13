# Kenneth's review checklist — mid-July 2026 update

**State as of 2026-07-14 HKT:** branch `mid-july-2026-wave` (created from master HEAD). Changes committed in four logical chunks; PR not yet opened (orchestrator handles push/PR). Planning docs live in `docs/mid-july-2026/`.

Wave window: 2026-06-03 → 2026-07-14. Every fact below was fact-checked against primary sources during drafting; the two "verify before printing" figures were re-fetched at implementation time (see Verification, bottom).

---

## Step 1 — Read the proposals

1. `timeline-additions.md` — the 10 new entries + the June 2 extension, with facts, sources, and caveats
2. `per-chapter-changes.md` — the per-file diff plan
3. `PR-description.md` — the PR body

---

## Step 2 — Review the commits (4 chunks)

```bash
cd C:/Users/Kenneth/Claude/awesome-llm-knowledge-systems
git log --oneline master..mid-july-2026-wave
git diff --stat master..mid-july-2026-wave
```

Expected commits (oldest first):
1. Ch11 — 10 timeline entries + June 2 extension + sixth Pattern thread + Sources
2. Chapters — Ch02/03/04/06/07/08/09/12 integrations
3. Glossary + README + CHANGELOG
4. Planning docs (`docs/mid-july-2026/`)

`translations/` and `docs/archive/` must be untouched.

---

## Step 3 — Timeline entries (Ch11), checked off as done

- [x] June 8 — Apple opens Foundation Models to any LLM provider (WWDC26)
- [x] June 9 — Claude Fable 5 + Mythos 5 (first public GA of a Mythos-class model)
- [x] June 12 — Export-control suspension + staged restoration + jailbreak-severity framework
- [x] June 17 — AWS AgentCore harness GA
- [x] June 18 — MCP Enterprise-Managed Authorization
- [x] June 18 — Terminal-Bench Challenges
- [x] June 26 — OpenAI GPT-5.6 Sol/Terra/Luna (EO-gated preview, METR CoT catch, priced ultra mode)
- [x] June 29 — DeepSeek V4 peak/off-peak pricing
- [x] July 6 — Tencent Hy3 (Hunyuan 3.0) under Apache 2.0
- [x] July 6 — Anthropic J-space ("A global workspace in language models")
- [x] June 2 Microsoft Build entry EXTENDED (Agent Harness + Foundry Hosted Agents)
- [x] `## The Pattern` — sixth thread ("government enters the distribution loop")
- [x] `## Sources` — new primary sources appended

## Step 4 — Chapter integrations, checked off as done

- [x] Ch04 — AWS/Microsoft harness-as-product (§4.9); metered-credit walk-back + Cowork (§4.9); refusal-as-`stop_reason` (§4.10); Terminal-Bench Challenges + UK AISI (§4.8); J-space + METR CoT feature-level sensor (§4.2)
- [x] Ch07 — new EMA section; SDK betas + SEP-2322 (RC section); 97M stat date-qualified (STALE FIX)
- [x] Ch06 — new "Evaluation Grows Governance Axes" section (GateMem, MemSyco-Bench, Decision-Aware Memory Cards, agent-native memory survey; optional control-plane-placement note)
- [x] Ch03 — Still + TokenPilot KV-cache compaction (§3.3)
- [x] Ch02 — Bedrock Managed KB (GA); contested SubQ 12M-token claim; Agents-K1
- [x] Ch09 — DeepSeek V4 peak pricing; Huawei + China Mobile carrier-scale validation; GLM-5.2; Hy3
- [x] Ch08 — Notion 3.6 External Agents; Tana → Tana Outliner correction; Heptabase/Capacities
- [x] Ch12 — Apple `LanguageModel` protocol; Gemma 4 QAT
- [x] Ch05 — SKIPPED (no `wave-skills-addendum.md` present at implementation time)

## Step 5 — Glossary / README / CHANGELOG

- [x] Glossary — **Safety-Tiered Distribution** (S), **Enterprise-Managed Authorization (EMA)** (E)
- [x] README — What's-new block → July 2026; June entries demoted; late-May list dropped; Ch07 ToC row date-qualified; footer May → July (STALE FIX)
- [x] CHANGELOG — new `## July 2026` section with mid-July wave bullet + caveats

---

## Verification (the two "verify before printing" figures)

- [x] **Hy3 hallucination second figure** — fetched `huggingface.co/tencent/Hy3`: confirmed **12.5% → 5.4%** (printed the exact figure, not the "roughly halved" fallback). Blind eval 2.67/4 vs GLM-4's 2.51/4 also confirmed.
- [x] **MemSyco-Bench Qwen3-8B pair** — fetched `arxiv.org/html/2607.01071v1`: confirmed **27.43% → 44.67%** (≈27.4% → 44.7%; kept). DeepSeek-V4-Flash 18.67% → 32.67% confirmed; factual-accuracy drop 11-23 pts confirmed.

## Editorial exclusions (recorded in `PR-description.md` and `per-chapter-changes.md`)

Tree Ring Memory (issue #48), Remio (issue #47), Qwen3.7-Plus, Claude Cowork web/mobile (folded into Ch04), KV-cache marketplace proposal (arXiv 2606.13361), Anthropic SDK metering pause (chapter-level). Neutral reasons only.

---

## Step 6 — Merge (orchestrator)

No push / PR from this session. After review, squash-merge; then, matching prior-wave hygiene (PRs #43, #46), archive these planning docs in a follow-up:

```bash
git mv docs/mid-july-2026 docs/archive/mid-july-2026
```

## Notes

- No translation propagation this wave (English-first, consistent with the last three waves).
- `docs/` path is `docs/mid-july-2026/` per the work order (prior waves used a `-update` suffix, e.g. `docs/early-june-2026-update/`); the follow-up archive PR normalizes to `docs/archive/mid-july-2026/`.
