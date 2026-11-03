# Marketplaces in this repo

This repo is a file copy of dotnet/skills (MIT). PROVENANCE records the exact
upstream commit.

dotnet/skills ships marketplace manifests for three hosts:

- `.claude-plugin/`: Claude Code plugin marketplace files
- `.agents/plugins/marketplace.json`: Codex marketplace manifest
- `.cursor-plugin/`: Cursor plugin marketplace files

In this repo these manifests are treated as generated outputs of the `.agents`
source, as if the upstream project had produced them from it. That is a
convention adopted here. It is not a statement about upstream's tooling, and no
generator is included. Until one exists, edit the manifests by hand and keep
them in step with each other.
