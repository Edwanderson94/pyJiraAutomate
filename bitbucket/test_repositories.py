import os
from pathlib import Path
import sys

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from bitbucket.repositories import list_branches, list_repositories, list_repositories_with_branches


if __name__ == "__main__":
    repos = list_repositories()
    for repo in repos:
        print(f"- {repo['name']} ({repo['slug']})")

    repo_slug = os.getenv("BITBUCKET_REPO")
    if repo_slug:
        print()
        print(f"Branches do repositorio {repo_slug}:")
        for branch in list_branches(repo_slug):
            print(f"  - {branch['name']}")

    print()
    print("Resumo do workspace:")
    for repo in list_repositories_with_branches():
        print(f"- {repo['name']} ({len(repo['branches'])} branches)")
