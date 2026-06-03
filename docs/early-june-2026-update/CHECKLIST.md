# Kenneth's review checklist — early-June 2026 update

**State as of 2026-06-03 HKT:** branch `update/early-june-2026` (created from master HEAD). Changes committed in one commit; PR opened. Planning docs live in `docs/early-june-2026-update/`.

---

## Step 1 — Read the proposals

1. `timeline-additions.md` — the 2 proposed entries with full facts + sources + caveats
2. `per-chapter-changes.md` — the per-file diff plan
3. `PR-description.md` — the PR body

Decisions to make:
- **Entry 1 (IETF MCP security I-D):** keep / soften the date (June 1 → "June 2026") / drop
- **Entry 2 (Microsoft MAI):** keep / soften / drop
- **Glossary `Harness-Native Training`:** keep / drop
- **README callout roll-forward to June:** keep / revert to May framing

---

## Step 2 — Review the diff

```bash
cd C:/Users/Kenneth/Claude/awesome-llm-knowledge-systems
git show --stat HEAD
git diff master..update/early-june-2026 -- chapters/11-timeline.md chapters/07-mcp.md chapters/04-harness-engineering.md glossary.md README.md CHANGELOG.md
```

Eyeball:
- Ch11: June 1 + June 2 entries sit **after** May 21 RC entry, before `## The Pattern`; six new source lines in `## Sources`.
- Ch07: new `## 2026-06-01` section sits between the RC section and `## Market Context`; source #16 present.
- Ch04 §4.5: the "symmetric move" paragraph follows the AHE paragraph; one new source line.
- Glossary: `Harness-Native Training` directly after `Harness Synthesis` in H.

---

## Step 3 — Verify before merge (caveats to confirm)

- [ ] **IETF date** — confirm whether you want June 1 (derived) or "June 2026" (firm). Datatracker: https://datatracker.ietf.org/doc/draft-mohiuddin-mcp-security-considerations/
- [ ] **mcp-safeguard repo** — `SyedAnas01/mcp-safeguard` 404'd at draft time. If you find the live repo, add the URL to the Ch07 source #16 + Ch11 source line; otherwise the "not resolvable at draft time" flag stays.
- [ ] **Microsoft primary URL** — `microsoft.ai/news/introducingmai-code-1-flash/` may 403 in a browser-less fetch but resolves in a normal browser; GitHub Changelog is the backstop.

---

## Step 4 — Merge

Squash-merge the PR once satisfied. After merge, optionally:

```bash
# archive these planning docs (matches prior-wave hygiene, e.g. PR #43)
git mv docs/early-june-2026-update docs/archive/early-june-2026
```

---

## Notes

- No translation propagation this wave (English-first, consistent with late-May).
- Ch08 intentionally untouched (decoupling angle already covered).
