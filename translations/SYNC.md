# Translation synchronization

The synchronization pass covers the English README, all 14 chapters and glossary in Traditional Chinese, Simplified Chinese, Japanese, Korean and Spanish.

Synchronized on **November 1, 2026**, against the October 31 English content snapshot: **80 documents and 21,200 aligned source lines**. Every language includes its README, 14 chapters and glossary. The [manifest](sync-manifest.json) records the exact source and translated text hashes.

| Language | README | Chapters | Glossary |
|---|---|---|---|
| 繁體中文 | [Read](README-zh.md) | 14 / 14 | [Terms](glossary_zh.md) |
| 简体中文 | [Read](README_zh-CN.md) | 14 / 14 | [Terms](glossary_zh-CN.md) |
| 日本語 | [Read](README_ja.md) | 14 / 14 | [Terms](glossary_ja.md) |
| 한국어 | [Read](README_ko.md) | 14 / 14 | [Terms](glossary_ko.md) |
| Español | [Read](README_es.md) | 14 / 14 | [Terms](glossary_es.md) |

The translations combine existing translations of unchanged source passages, machine-assisted drafts and native-language AI revision. They are not presented as professional human copy editing. Code blocks, diagram labels, technical identifiers, verbatim quotations and original reference titles retain their source form. Reading-time estimates refer to the English source.

Acceptance checks compare source and translation line structure, heading levels, table rows, numeric literals, inline/fenced code, HTML and citation targets. Stable original-heading anchors preserve section links after headings are translated. A source/content hash manifest identifies the exact edition checked; hashes establish byte identity, not semantic accuracy.

The English edition remains the reference for resolving translation questions. Future English changes require a new synchronization pass; a dated translation does not silently become current with them.

Run `python scripts/check_translation_sync.py --require-current` from the repository root to verify the current snapshot. The default mode checks translated-file integrity and reports changed English sources as warnings, preserving the option to publish English updates before a later translation pass. Hashes normalize UTF-8 text to LF line endings.
