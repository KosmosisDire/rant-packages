# rant-packages

The GitHub repos `rant install` looks in for a package it knows by name, and `rant add` for a
library.

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

A `library` block in its `package.rant` makes a repo a library: `cmake`, `python`, `csharp` and
`rust` name the target to link, the Python project, the NuGet id and the crate. Its wheels and
`<id>.<version>.nupkg` come with each release, and its crate from the tag `crate-v<version>`.
