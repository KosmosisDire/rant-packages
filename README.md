# rant-packages

The GitHub repos `rant install` looks in for a package it knows by name.

```hcl
repos = [
  "KosmosisDire/rant-bridge",
]
```

The `name` in the `package.rant` at the root of each repo names its package, and no two repos
may name the same one. Releases are tagged `v<version>` and carry their files by name:

- `<name>-<version>-<platform>.tar.gz`, unpacked into `~/.rant/packages/<name>`
- `<name>-<version>.vsix`, installed into an editor
- `<name>-<version>-skill.zip`, a skill for AI coding agents
