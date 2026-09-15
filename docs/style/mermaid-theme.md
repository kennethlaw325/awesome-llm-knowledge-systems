# Chapter figure style

Every chapter carries one structural figure at the top, a reading-time line in the header blockquote, and a three-bullet take-away box before Sources. This file is the single source for the theme and the placement rules so the figures stay consistent across waves. Approved on the `visual-poc` branch, September 15, 2026.

## Theme

Paste this as the first line of every `mermaid` fence, verbatim:

```
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#eef1f4','primaryTextColor':'#1f2328','primaryBorderColor':'#8c959f','lineColor':'#6b7280','tertiaryColor':'#f6f8fa','clusterBkg':'#f9fafb','clusterBorder':'#8c959f','edgeLabelBackground':'#ffffff'}}}%%
```

And these four class definitions as the last lines of every `flowchart` fence, verbatim:

```
classDef stable fill:#eef1f4,stroke:#8c959f,stroke-width:1.5px,color:#1f2328
classDef accent fill:#dbeafe,stroke:#2563eb,stroke-width:1.5px,color:#0b3a8f
classDef muted fill:#f6f8fa,stroke:#adb5bd,stroke-width:1.5px,color:#57606a
classDef gate fill:#ffffff,stroke:#2563eb,stroke-width:1.5px,color:#0b3a8f
```

One accent colour (blue), everything else greyscale. Meaning of the classes:

- `stable` -- settled components, the things the chapter treats as given.
- `accent` -- the one or two nodes the chapter's argument turns on. Use sparingly; a figure with five accent nodes has no accent.
- `muted` -- ephemeral, per-job, or contested items.
- `gate` -- a decision or check point (usually a `{{hexagon}}` node).

Assign classes with `class A,B stable` lines placed before the `classDef` block. Use `direction LR` inside a subgraph when it keeps the figure short. Edge labels carry the argument (`-->|read before deciding|`), not decoration. Dotted edges (`-.->`) mean ephemeral or optional. Prefer `flowchart TB` or `flowchart LR`. Keep a figure at or under about 2:1 wide, so its type stays readable in GitHub's roughly 900px column; a wide `LR` layout usually wants `TB` instead. The Chapter 11 `timeline` is exempt: it is horizontal by construction and readers zoom it.

Chapter 11 uses `timeline`, which takes no `classDef` and no `title` line (a title renders in the default text colour and vanishes in dark mode; the caption already names the figure). Its init line is this variant, verbatim, which maps the section colours onto the same greys and the one blue:

```
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#eef1f4','primaryTextColor':'#1f2328','primaryBorderColor':'#8c959f','lineColor':'#6b7280','tertiaryColor':'#f6f8fa','clusterBkg':'#f9fafb','clusterBorder':'#8c959f','edgeLabelBackground':'#ffffff','cScale0':'#eef1f4','cScale1':'#f6f8fa','cScale2':'#eef1f4','cScale3':'#f6f8fa','cScale4':'#dbeafe','cScaleLabel0':'#1f2328','cScaleLabel1':'#1f2328','cScaleLabel2':'#1f2328','cScaleLabel3':'#1f2328','cScaleLabel4':'#0b3a8f','cScalePeer0':'#f6f8fa','cScalePeer1':'#eef1f4','cScalePeer2':'#f6f8fa','cScalePeer3':'#eef1f4','cScalePeer4':'#dbeafe','cScaleInv0':'#8c959f','cScaleInv1':'#8c959f','cScaleInv2':'#8c959f','cScaleInv3':'#8c959f','cScaleInv4':'#8c959f'}}}%%
```

## Placement and format

**Figure** goes at the top of the chapter: after the header blockquote (the `In one sentence` / `Why it matters` / `Reading time` block), before the first `##` heading. A one-paragraph italic caption comes first, then a blank line, then the fence:

````
*Figure: What the figure shows, which section it comes from, and the one relationship the reader should notice. Two to four sentences.*

```mermaid
...
```
````

The caption names the section the figure is drawn from and states the argument the edges carry. It is not a title.

**Reading time** is the last line of the header blockquote, separated from `Why it matters` by a bare `>` line:

```
>
> **Reading time:** ~18 min (3,951 words / 230 wpm)
```

Words are counted on the whole file with `str.split()` before these two lines are inserted; minutes are rounded up. Recount when the chapter changes.

**Three things to take away** sits immediately before `## Sources` (or before the `*Next:*` footer when a chapter has no Sources). Exactly three bullets, each a bold claim followed by one sentence, each grounded in the chapter text. Separators on both sides:

```
---

## Three things to take away

- **Claim one.** One sentence of consequence.
- **Claim two.** One sentence of consequence.
- **Claim three.** One sentence of consequence.

---

## Sources
```

## Rules that keep the diff reviewable

- Existing sentences are never edited or moved: nothing that exists on `master` is deleted or changed. Figures, captions, the reading-time lines, and take-away boxes are pure insertions, and only those inserted elements may be revised.
- ASCII dashes only (`--`, `---`), matching the chapters. No U+2014 or U+2013 in inserted text.
- CRLF line endings, matching the repository.
- Every fence must parse in Mermaid 11 (GitHub's renderer). Render it headless before committing.
