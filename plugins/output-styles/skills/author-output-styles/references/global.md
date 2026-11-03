# output-styles/ (global)

> Custom instruction sets that adjust how the agent works

**Scope:** global  (C:\Users\pmcro\.claude\output-styles\)

**When it loads:** Files read at startup; the style you select with outputStyle applies to every response.

Each markdown file defines an output style: a set of instructions that, by default, also replaces the built-in software-engineering task instructions. Use this to adapt the tool for uses beyond coding, or to add teaching or review modes. Select a built-in or custom style with /output-style, /config, or the outputStyle key in settings. Styles here are available in every project; project-level styles with the same name take precedence.

## Tips

- Built-in styles Default, Proactive, Concise, Explanatory, and Learning are included; custom styles go here
- Set keep-coding-instructions: true in frontmatter to keep the default task instructions alongside your additions
- Switching styles mid-session applies from your next message; in the terminal, a style file you create or edit mid-session is picked up after a restart

_Source: AGENTS docs, Explore the .claude directory (captures in G:\ProjectName\docs\claude-directory-screenshots)._
