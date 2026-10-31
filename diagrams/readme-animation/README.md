# README animation source

The shared English animation is a 30-second introduction to the guide. The five translated READMEs embed the same diagram; the guide's text remains available in each language.

Outputs: [GIF](../knowledge-map.gif), [MP4](../knowledge-map.mp4), [static map](../evolution-stack.png).

The diagram connects knowledge to context to the model, with tools, permissions and checks in the harness, then shows reading paths. It makes no new model-performance claim or settled-generation claim.

## Reproduce

Requires Node.js, FFmpeg and the HyperFrames browser runtime. The package scripts pin HyperFrames 0.8.223; its compiler resolves GSAP and bundled fonts.

```sh
cd diagrams/readme-animation
npm run check
npm run render -- --quality delivery --workers 2 --output ../knowledge-map.mp4
ffmpeg -i ../knowledge-map.mp4 -filter_complex "fps=10,scale=960:-1:flags=lanczos,split[s0][s1];[s0]palettegen=stats_mode=diff[p];[s1][p]paletteuse=dither=bayer:bayer_scale=3" -loop 0 -y ../knowledge-map.gif
```

Use the HyperFrames preview to edit the HTML scene. There is no audio; the expandable README block and static alternative let readers choose whether to view motion. The final render was inspected at multiple timestamps and at phone width, and its full MP4 decode and 30-second GIF duration were checked.
