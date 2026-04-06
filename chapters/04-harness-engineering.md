# Chapter 4: Harness Engineering -- Building the OS Around the Model

> **In one sentence:** A harness is everything around the AI model -- the rules, tools, safety checks, and workflows that make it actually useful.
>
> **Why it matters:** The AI model is like a powerful engine. Without a chassis, steering wheel, and brakes, it's useless. The harness is what turns raw AI into a product.

> "Every component in a harness encodes an assumption about what the model can't do on its own, and those assumptions are worth stress testing."
> -- Anthropic, "Building Effective Agents," 2025

An agent is not a model. An agent is a **model plus a harness** -- the surrounding system of prompts, tools, memory, control flow, evaluation logic, and orchestration code that turns raw inference into reliable behavior. The model is the engine; the harness is the vehicle. This chapter examines how practitioners design, evaluate, and evolve that vehicle.

---

## 4.1 Defining the Harness

The harness is everything that is not the model weights. It includes:

- System prompts and instruction templates
- Tool definitions and execution sandboxes
- Memory systems (short-term, long-term, episodic)
- Planning and decomposition logic
- Control flow (loops, conditionals, retry policies)
- Evaluation and self-correction mechanisms
- Safety guardrails and output validation
- Context assembly pipelines (Chapter 3)

A bare model API call with a user message is a trivial harness. A production agent with planning, multi-step tool use, self-evaluation, and persistent memory is a complex one. The discipline of harness engineering is about making principled decisions across this spectrum.

## 4.2 The Fowler-Bockeler Taxonomy

Martin Fowler and Birgitta Bockeler (ThoughtWorks, 2025) proposed a two-axis taxonomy for harness components that has become a standard reference:

**Axis 1: Direction**
- **Guides (Feedforward):** Components that shape behavior *before* the model acts. System prompts, few-shot examples, tool schemas, planning templates. These set the rails.
- **Sensors (Feedback):** Components that evaluate behavior *after* the model acts and feed results back. Output validators, test runners, human review, self-evaluation prompts. These correct the course.

**Axis 2: Mechanism**
- **Computational Controls:** Deterministic code -- regex validators, type checkers, schema enforcement, permission checks. These are hard constraints that never hallucinate.
- **Inferential Controls:** Another LLM call used to judge, route, or refine. Evaluator models, classifiers, summarizers. These are soft constraints that trade precision for flexibility.

The taxonomy reveals a design space. Most production harnesses use all four quadrants:

|  | Feedforward (Guides) | Feedback (Sensors) |
|--|---------------------|--------------------|
| **Computational** | Schema validation on tool inputs, permission allow-lists | Output format checks, test suite execution |
| **Inferential** | Planning prompts, few-shot routing | Self-evaluation, LLM-as-judge, critique chains |

The insight is that computational controls are cheaper and more reliable but less flexible, while inferential controls handle ambiguity but introduce their own failure modes. Good harness design uses computational controls wherever possible and reserves inferential controls for genuinely ambiguous decisions.

## 4.3 OpenAI Codex: Scale Through Harness

The OpenAI Codex blog post (2025) offered a striking data point: **three engineers plus the Codex agent system produced approximately one million lines of code across roughly 1,500 pull requests.** The productivity multiplier was not primarily about model quality -- it was about harness design.

The Codex harness included:
- Automated PR decomposition (breaking large tasks into reviewable units)
- Sandboxed execution environments for each task
- Automated test generation and validation
- Human review integration at PR boundaries
- Persistent context about repository structure and conventions

The lesson: at sufficient harness maturity, the model becomes a component in a larger production system rather than a standalone tool. The harness handles orchestration, quality control, and integration -- concerns that no amount of prompt engineering can address.

## 4.4 The IMPACT Framework

swyx (Shawn Wang) proposed the IMPACT framework as a systematic way to think about harness design dimensions:

- **Intent:** How does the system understand what the user actually wants? Includes intent classification, clarification dialogues, and goal decomposition.
- **Memory:** What does the system remember across turns and sessions? Includes conversation buffers, vector stores, structured knowledge bases, and user preference systems.
- **Planning:** How does the system break complex tasks into steps? Includes chain-of-thought prompting, explicit plan generation, and tree-search over action spaces.
- **Authority:** What is the system allowed to do? Includes permission systems, human-in-the-loop gates, and capability boundaries.
- **Control Flow:** How does execution proceed? Includes sequential chains, parallel fan-out, conditional branching, loops with exit conditions, and retry policies.
- **Tools:** What external capabilities does the system have access to? Includes function definitions, API integrations, code execution environments, and browser access.

IMPACT is useful as a design checklist. When building or reviewing a harness, walking through each dimension surfaces gaps. A system with strong Tools but weak Authority has a security problem. A system with strong Planning but no Memory cannot learn from its mistakes. The framework makes these imbalances visible.

## 4.5 The Meta-Harness Paper: Automating Harness Design

A joint paper from Stanford, MIT, and KRAFTON (March 2026) introduced the concept of the **meta-harness** -- a system that automatically optimizes harness configurations.

Their key finding: on the same benchmark, with the same base model, different harness configurations produced a **6x performance gap**. The best harness configuration for a given task was rarely obvious and often counterintuitive. Manual harness tuning was leaving enormous performance on the table.

The meta-harness approach treated harness parameters (number of retries, planning depth, tool selection strategy, memory window size, evaluation stringency) as a search space and used automated optimization to find high-performing configurations. The system could adapt the harness to different task types, different models, and different cost constraints.

This result has a profound implication: **harness engineering is not a solved design problem with known best practices -- it is an optimization problem with a large and poorly understood search space.** Teams that treat harness design as a one-time architecture decision are likely operating far below the frontier.

## 4.6 Anthropic's Three-Agent Architecture

Anthropic's research on multi-agent systems (2025-2026) converged on a recurring three-role architecture:

- **Planner:** Decomposes the task into subtasks, maintains the overall plan, and decides when to revise.
- **Generator:** Executes individual subtasks -- writing code, drafting text, calling tools.
- **Evaluator:** Assesses Generator output against task requirements and provides structured feedback.

This separation of concerns directly addresses two failure modes Anthropic identified:

**Context Anxiety.** When a single agent handles planning, execution, and evaluation, it tends to hedge. It qualifies its outputs, adds unnecessary caveats, and spends tokens on meta-commentary rather than task execution. Separating the roles lets each agent focus without carrying the cognitive load of the others.

**Self-Evaluation Bias.** Models are systematically poor at evaluating their own output. They exhibit a well-documented leniency bias -- rating their own work higher than an independent judge would. The three-agent architecture mitigates this by using a separate evaluator (potentially a different model or a differently prompted instance) that has no investment in the generated output.

A subtlety Anthropic emphasized: **evaluator calibration is itself a harness engineering problem.** An overly strict evaluator causes infinite revision loops. An overly lenient one passes low-quality work. The evaluator's threshold and criteria need tuning as carefully as the generator's instructions.

## 4.7 The Harness as Moat

In early 2026, Meta acquired Manus for approximately $2 billion. Manus had no proprietary model. Its entire value was in the harness -- the orchestration logic, context engineering pipeline, tool integration layer, and operational infrastructure that turned commodity model APIs into a reliable agent product.

This acquisition crystallized what the industry had been discovering: **the harness is the moat.** Models are increasingly commoditized. The differentiator is how you wrap them -- what tools you provide, how you manage context, how you handle failure, how you orchestrate multi-step workflows, and how you evaluate quality.

The implication for practitioners is that harness engineering is not plumbing to get through on the way to the "real work" of model development. It *is* the real work for most production AI teams.

## 4.8 Harness Maintenance: The Stress-Testing Imperative

Anthropic's most actionable insight may be the simplest: every harness component encodes an assumption about model limitations, and **those assumptions expire.**

When a harness was built around GPT-4-level capabilities, it might include:
- Explicit chain-of-thought prompting (because the model needed it)
- Aggressive output parsing (because the model was inconsistent with formats)
- Multi-step verification (because single-pass accuracy was insufficient)
- Detailed few-shot examples (because zero-shot performance was poor)

As newer models arrive with improved reasoning, instruction following, and output consistency, these components become **load-bearing walls that may no longer need to bear load.** They add latency, cost, and complexity without contributing to quality.

The discipline is periodic stress-testing: systematically disabling harness components to determine which ones are still necessary. If removing a planning step does not degrade performance, remove it. If the model now follows a format reliably without few-shot examples, drop them. If self-evaluation adds cost but not quality, eliminate it.

This is counterintuitive. Engineers naturally add safety mechanisms and resist removing them. But in harness engineering, unnecessary components are not free -- they consume context window space, add latency, increase cost, and create maintenance burden. A lean harness that matches the current model's capabilities outperforms an over-engineered one built for a weaker model.

The practical recommendation: when onboarding a new model, start by running your existing harness, then methodically strip components while measuring task performance. What remains is your true harness. What you removed was technical debt from a previous capability era.

---

## Sources

- **Fowler, Martin and Bockeler, Birgitta.** "Harness Architecture for LLM Agents." ThoughtWorks Technology Radar / blog, 2025. Guides vs. Sensors, Computational vs. Inferential taxonomy.
- **OpenAI.** "Codex: From Research to Production." OpenAI blog, 2025. Three-engineer, ~1M lines, ~1,500 PRs case study.
- **swyx (Shawn Wang).** "The IMPACT Framework for Agent Design." Blog / conference talk, 2025. Six-dimension harness design checklist.
- **Stanford / MIT / KRAFTON.** "Meta-Harness: Automated Optimization of LLM Agent Harnesses." arXiv preprint, March 2026. 6x performance gap finding, automated harness tuning.
- **Anthropic.** "Building Effective Agents." Anthropic engineering guide, 2025. Three-agent architecture, context anxiety, self-evaluation bias, stress-testing imperative.
- **Anthropic.** "Multi-Agent Systems: Planner-Generator-Evaluator Architectures." Research report, 2025-2026. Evaluator calibration findings.
- **Meta / Manus Acquisition.** Various reporting, early 2026. ~$2B acquisition validating harness-as-moat thesis.
- **Karpathy, Andrej.** "Software 3.0." Talk / essay, 2025. Framing of models as components within larger software systems.
- **LangChain.** "Agent Architecture Patterns." LangChain documentation, 2025. Practical patterns for control flow and tool orchestration.
- **Harrison Chase.** "The Rise of the Agent Engineer." Blog post, 2025. Role definition for harness-focused engineering.
