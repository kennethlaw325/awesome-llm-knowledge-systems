# Kenneth's review checklist — May mid-2026 update

**State as of 2026-05-15 HKT:** branch `update/may-mid-2026` created from master HEAD. Working tree has staged changes for Ch04/05/06/07/08/11 + glossary. Planning docs in `docs/may-mid-2026-update/` are untracked.

---

## Step 0 — Sanity check

```bash
cd C:/Users/Kenneth/Claude/llm-knowledge-engineering
git status        # should show ?? docs/may-mid-2026-update/ + 7 staged chapter/glossary files
git branch        # should show * update/may-mid-2026
git log -1        # should show master HEAD as the parent
```

If any of those is wrong, stop and investigate.

---

## Step 1 — Read the proposals

Read in this order:

1. `docs/may-mid-2026-update/timeline-additions.md` — the 3 proposed timeline entries + 1 augment with full text + sources
2. `docs/may-mid-2026-update/per-chapter-changes.md` — the per-chapter diff plan
3. `docs/may-mid-2026-update/PR-description.md` — what the PR will say

Decisions to make:

- Each Tier 1 timeline entry: **keep / soften / drop**
- For the Mythos augment (GPT-5.5-Cyber parallel): **keep / soften / drop**
- Glossary: **add all 3 / drop any**

---

## Step 2 — Review the actual diff

```bash
git diff --cached chapters/11-timeline.md
git diff --cached chapters/04-harness-engineering.md
git diff --cached chapters/05-skill-systems.md
git diff --cached chapters/06-agent-memory.md
git diff --cached chapters/07-mcp.md
git diff --cached chapters/08-tools-landscape.md
git diff --cached glossary.md
```

Eyeball:
- Chronology of `chapters/11-timeline.md` May 2026 section: should now be Apr 7-28 (existing) → May 6 AWS MCP GA → May 6 Code with Claude → May 7 AWS Payments. The April 7 Mythos entry should have the GPT-5.5-Cyber addendum.
- Source URLs in each chapter's Sources block are appended at the end (not interleaved).
- Glossary entries: D / O / X — D is new (Dreaming), O sits next to Obsidian (Outcomes), X is new.

---

## Step 3 — Commit (only when satisfied)

Recommend one commit for clean history (single bundled PR per locked scope):

```bash
git commit -m "$(cat <<'EOF'
Ch04/05/06/07/08/11 + glossary: May mid-2026 update (3 timeline entries + 1 augment)

Add three Tier 1 timeline entries and one augmentation:
- May 6, 2026 AWS MCP Server GA (first hyperscaler-managed remote MCP endpoint)
- May 6, 2026 Code with Claude — Dreaming + Outcomes + Multiagent Orchestration
- May 7, 2026 AWS AgentCore Payments preview (x402, Coinbase, Stripe)
- Augment Apr 7 Mythos entry: May 11 GPT-5.5-Cyber Trusted Access reproduces
  the Glasswing distribution pattern on OpenAI's side

Per-chapter expansions:
- Ch04 §4.6: Dreaming extends the self-healing memory lineage
- Ch04 §4.9: managed MCP edge as third cloud-native primitive
- Ch04 §4.1: deterministic infrastructure-enforced harness contract (x402)
- Ch05 §5.9: AWS as fourth Skills-adopting vendor (cross-vendor convergence)
- Ch06: trainable-vs-curated dichotomy for long-term agent memory
- Ch07: AWS MCP GA as scale milestone; x402 as cross-protocol value layer
- Ch08: managed substrate now learns and self-corrects (Velocity Paradox)

Glossary: Dreaming, Outcomes (Anthropic), x402.

All sources are primary or first-tier secondary. OpenAI GPT-5.5-Cyber URL may
return 403 to crawlers — flagged for user verification.
EOF
)"
```

---

## Step 4 — Push and PR

```bash
git push -u origin update/may-mid-2026

gh pr create --title "May mid-2026 update: 3 timeline entries + 1 augment + 6 chapter expansions" \
             --body-file docs/may-mid-2026-update/PR-description.md
```

---

## Caveats to surface in PR

- OpenAI primary URL (`openai.com/index/gpt-5-5-with-trusted-access-for-cyber/`) may 403 against crawlers; CNBC secondary is the load-bearing source for the Mythos augment.
- AWS AgentCore Payments URL slug contains `/04/` but the launch is May 7, 2026 — preserved as user-supplied.
- No translation propagation in this wave (English-only first wave per locked scope).
