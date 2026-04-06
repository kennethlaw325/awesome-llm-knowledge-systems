# Chapter 5: Skill Systems -- Skills, Skill Graphs, and Progressive Disclosure

> **In one sentence:** Skills are reusable instruction sets that tell AI how to do specific tasks, and skill graphs connect them into a navigable knowledge network.
>
> **Why it matters:** Instead of explaining the same thing to AI every time, skills let you teach it once and reuse that knowledge forever.

Skills are pre-packaged instruction sets -- self-contained bundles of prompts, tool configurations, and behavioral rules -- injected into an agent's context window when a specific capability is needed. They are the mechanism by which agent systems scale from a handful of built-in behaviors to hundreds or thousands of specialized capabilities without drowning the model in irrelevant instructions.

This chapter covers the architecture of skill systems, the combinatorial problem they create, and the progressive disclosure patterns that solve it.

---

## 5.1 The Skill Concept

A skill, in its simplest form, is a markdown file (or structured text block) containing instructions for a specific task. When a user request matches the skill's trigger conditions, the skill's content is loaded into the context window. When no match occurs, the skill contributes zero tokens.

This is fundamentally different from a monolithic system prompt that tries to cover every capability. A system prompt that describes 90 tools and 50 behavioral modes might consume 50,000 or more tokens before the user even types a message. A skill-based system loads only what is relevant, keeping the baseline context lean and reserving window capacity for the actual task.

The design pattern is borrowed from software engineering: skills are to agents what plugins are to applications. They provide extensibility without bloat.

## 5.2 The Anthropic Skills Ecosystem

Anthropic launched skills for Claude Code in October 2025, initially as a project-specific feature -- markdown files in a `.claude/` directory that Claude could invoke when relevant. The format was intentionally simple: a markdown file with a description, trigger conditions, and instructions.

By December 2025, Anthropic published skills as an open standard through agentskills.io, defining a portable format that any agent system could adopt. The specification covered:

- Skill metadata (name, description, version, author)
- Trigger definitions (keyword matches, intent classifiers, regex patterns)
- Content structure (instructions, examples, tool configurations)
- Dependency declarations (other skills this skill builds on)

The ecosystem response was rapid. By early 2026, the official repository had accumulated over 87,000 GitHub stars, and community-contributed skills exceeded 700,000. Collections like awesome-llm-skills, awesome-agent-skills (featuring 1,000+ skills from official platform teams), and awesome-claude-code became primary discovery channels.

This growth created the very problem skills were designed to solve: too many capabilities competing for limited context space.

## 5.3 The Scaling Problem

OpenAI's agent documentation includes a practical guideline: **keep agents under 20 tools, and expect accuracy degradation past 10.** Empirical testing across multiple model families confirms this threshold. Each additional tool definition adds tokens to the context and decision branches to the model's selection space. At 90 tools, the schema overhead alone can exceed 50,000 tokens -- before any conversation, memory, or retrieved documents enter the window.

The degradation is not just about token count. It is about decision complexity. When a model must choose among 90 tools, the probability mass spreads thin. The model spends more reasoning capacity on tool selection and less on task execution. Error rates on tool parameter construction increase. The model begins selecting plausible-but-wrong tools more frequently.

Skills face the same scaling pressure. A system with 500 available skills cannot load all 500 descriptions into the context. Even loading just the trigger descriptions for 500 skills could consume thousands of tokens and degrade the model's ability to process the actual request.

The solution is progressive disclosure.

## 5.4 Progressive Disclosure Architecture

Progressive disclosure is a multi-level information architecture where each level provides just enough detail for the next routing decision:

**Level 0: Routing Index.** A compact table mapping categories to skill groups. Might consume 200-500 tokens total for an entire skill library. This is what sits in the system prompt at rest.

**Level 1: Category Descriptions.** When the routing index identifies a relevant category, load the one-paragraph descriptions for skills in that category. Each description is optimized for scanning -- enough to determine relevance, not enough to execute.

**Level 2: Skill Links and Dependencies.** For the selected skill, load its dependency graph -- what other skills or tools it requires, what context it expects.

**Level 3: Sections and Summaries.** Load the structural outline of the skill -- section headers, key decision points, parameter lists -- without the full instructional content.

**Level 4: Full Content.** Load the complete skill instructions into the context window. This happens only for the one or two skills actually being invoked.

The key insight, formalized by Heinrich and the arscontexta team, is that **most decisions happen before reading a single full file.** The routing index eliminates 95% of skills. Category descriptions eliminate most of the remainder. Full content loading is the exception, not the rule.

Measured across production systems, progressive disclosure reduces token overhead by **85-95%** compared to loading all skill definitions upfront. Anthropic's own agent skills implementation demonstrates this: 17 production skills consume approximately 1,700 tokens at rest (Level 0 + Level 1), expanding to full content only on invocation.

## 5.5 Skill Graphs

Heinrich's Skill Graph architecture (arscontexta, 2025-2026) extends progressive disclosure into a network structure. Rather than a flat list of skills organized by category, a skill graph is a **network of interconnected markdown files linked by wikilinks**, where each node carries:

- A YAML frontmatter block with a concise description (for scanning at Level 1)
- Wikilinks to related skills, prerequisite skills, and sub-skills
- Structured sections that can be loaded independently

The graph structure enables several capabilities that flat skill lists cannot support:

**Contextual navigation.** When one skill is invoked, its linked skills become candidates for co-loading. A "deploy" skill links to "test," "rollback," and "monitor" skills -- not because they are in the same category but because they are operationally adjacent.

**Dependency resolution.** Skills can declare prerequisites. Invoking a complex skill automatically pulls in foundational skills it depends on, similar to package dependency resolution.

**Partial loading.** Because skills are structured with clear sections, the system can load specific sections (e.g., just the "error handling" section of a deployment skill) without loading the full document.

The graph topology itself becomes a form of knowledge representation. Densely connected skill clusters indicate capability areas with high internal coherence. Isolated skills may indicate gaps in the system's coverage or opportunities for integration.

## 5.6 The SkillReducer Paper

A study published in March 2026 examined 55,315 skills across multiple agent platforms and produced findings that challenge naive assumptions about skill quality:

- **26.4% of skills lacked routing descriptions entirely.** They had full instructional content but no metadata to help a routing system identify when to invoke them. These skills could only be triggered by exact name -- invisible to any intelligent routing layer.

- **Over 60% of skill body content was non-actionable.** It consisted of background context, motivation, caveats, and explanatory text rather than concrete instructions the model could execute. This content consumed tokens without contributing to task performance.

- **Compressed skills improved output quality by 2.8% over originals.** When researchers stripped non-actionable content and tightened the instructional language, model performance actually improved. Less was more -- the reduced noise in the context allowed the model to focus on the actionable instructions.

The implications for skill authoring are direct:

1. **Every skill needs a routing description.** Without it, the skill is effectively invisible to progressive disclosure systems.
2. **Instructional content should be dense and actionable.** Background context belongs in documentation, not in the skill body that gets injected into the context window.
3. **Skill quality measurement should include token efficiency** -- not just "does it work" but "does it work per token consumed."

## 5.7 The Meta-Tool Pattern for MCP

The Model Context Protocol (MCP) introduced a standardized way for agents to discover and invoke tools across providers. But MCP's original design loaded all available tool schemas at connection time, creating the same scaling problem skills face.

The meta-tool pattern solves this with two components:

- **Discovery Tool:** A single tool that accepts a natural language description and returns relevant tool schemas from the full registry. This is the only tool loaded at baseline.
- **Execution Tool:** A generic tool invocation wrapper that can call any tool by name once its schema has been retrieved via discovery.

The system loads two tool schemas instead of hundreds. When the model determines it needs a capability, it calls the discovery tool, receives the relevant schema, and then invokes the specific tool. The pattern trades one extra inference round-trip for massive context savings.

This is progressive disclosure applied to tool management: the model gets a phonebook, not the contents of every contact's file.

## 5.8 Authoring Guidelines

Drawing from the SkillReducer findings and production experience, a set of skill authoring best practices has emerged:

- **Lead with the routing description.** The YAML frontmatter description is the most important line in the file. It determines whether the skill is ever invoked. Write it for a classifier, not a human reader.
- **Front-load actionable instructions.** The first 200 tokens of the skill body should contain the core behavioral instructions. Background and context follow.
- **Use structured sections.** Headers, lists, and clear delineation enable partial loading and section-level retrieval.
- **Declare dependencies explicitly.** If the skill assumes another skill or tool is available, state it in metadata.
- **Include trigger examples.** Provide 3-5 example user messages that should activate the skill. These serve as both documentation and test cases for the routing layer.
- **Measure token cost.** Track the token count of each skill and set a budget. If a skill exceeds 2,000 tokens, consider whether it can be split or compressed.

---

## Sources

- **Anthropic.** "Claude Code Skills." Documentation and open standard specification, October 2025 (launch), December 2025 (open standard via agentskills.io). 87K+ GitHub stars by early 2026.
- **OpenAI.** "Agent Design Best Practices." OpenAI documentation, 2025. Recommendation of fewer than 20 tools per agent, accuracy degradation past 10.
- **Heinrich / arscontexta.** "Skill Graphs: Progressive Disclosure for Agent Capabilities." Blog series and implementation, 2025-2026. Wikilink-based skill networks, YAML scanning, partial loading architecture.
- **SkillReducer Paper.** "Less Is More: Compressing Agent Skills for Improved Performance." March 2026. 55,315 skills analyzed, 26.4% lacking routing descriptions, 60%+ non-actionable content, 2.8% quality improvement from compression.
- **Model Context Protocol (MCP).** Anthropic specification, 2024-2025. Standardized tool discovery and invocation protocol.
- **awesome-llm-skills.** Community collection on GitHub. Curated skill libraries across platforms.
- **awesome-agent-skills.** GitHub collection, 1,000+ skills from official platform teams.
- **awesome-claude-code.** GitHub collection. Claude Code-specific skills and configurations.
- **OpenAI.** "Function Calling Best Practices." 2025. Empirical data on tool count vs. accuracy tradeoffs.
- **Griciunas, Aurimas.** "Tool and Capability Management." In "5 Dominant Patterns in Context Engineering," 2025. Meta-tool pattern description.
