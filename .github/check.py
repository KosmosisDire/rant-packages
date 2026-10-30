"""Fails when a repo that packages.rant lists names no package, or when two name the same one."""

import re
import sys
import urllib.error
import urllib.request

NAME = re.compile(r"^[a-z][a-z0-9_]*$")
REPO = re.compile(r"^[\w.-]+/[\w.-]+$")


def fetch(url):
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            return r.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def main():
    text = open("packages.rant", encoding="utf-8").read()
    text = re.sub(r"#[^\n]*", "", text)
    listed = re.fullmatch(r"\s*repos\s*=\s*\[([^\]]*)\]\s*", text)
    if not listed:
        return "packages.rant must hold only repos = [...]"
    repos = re.findall(r'"([^"]*)"', listed.group(1))
    problems, named = [], {}
    for repo in repos:
        if not REPO.match(repo):
            problems.append(f"{repo} is no GitHub repo as owner/name")
            continue
        if repo.lower() in (r.lower() for r in named.values()):
            problems.append(f"{repo} is listed twice")
            continue
        package = fetch(f"https://raw.githubusercontent.com/{repo}/HEAD/package.rant")
        found = package and re.search(r'^name\s*=\s*"([^"]*)"', package, re.M)
        if not found:
            problems.append(f"{repo} gives no name in a package.rant at its root")
        elif not NAME.match(found.group(1)):
            problems.append(f"{repo} names its package {found.group(1)}, which is no package name")
        elif found.group(1) in named:
            problems.append(f"{repo} names the package {found.group(1)}, as {named[found.group(1)]} does")
        else:
            named[found.group(1)] = repo
            print(f"{found.group(1)}: {repo}")
    return "\n".join(problems) or None


if __name__ == "__main__":
    sys.exit(main())
