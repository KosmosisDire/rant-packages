# rant-packages

The packages `rant install` knows by name, each with the GitHub repo it comes from.

```hcl
package "bridge" {
  repo = "KosmosisDire/rant-bridge"
}
```

The repo holds a `package.rant` at its root with a `description` and the files its releases
carry: an `archive` unpacked into `~/.rant/packages/<name>`, or a `vsix` for editors. Releases
are tagged `v<version>`.
