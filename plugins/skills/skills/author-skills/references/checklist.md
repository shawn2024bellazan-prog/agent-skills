# checklist.md

> Supporting file bundled with the skill

**Scope:** project  (.agents/skills/security-review/checklist.md)

**When it loads:** The agent reads it on demand while running the skill.

Skills can bundle any supporting files: reference docs, templates, scripts. The skill directory path is prepended to SKILL.md, so the agent can read bundled files by name. For scripts in bash injection commands, use the ${CLAUDE_SKILL_DIR} placeholder.

## Example

```markdown
# Security Review Checklist

## Input Validation
- [ ] All user input sanitized before DB queries
- [ ] File upload MIME types validated
- [ ] Path traversal prevented on file operations

## Authentication
- [ ] JWT tokens expire after 24 hours
- [ ] API keys stored in environment variables
- [ ] Passwords hashed with bcrypt or argon2
```

_Source: Claude Code docs, Explore the .claude directory (captures in G:\ProjectName\docs\claude-directory-screenshots)._
