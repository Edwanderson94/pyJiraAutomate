from pathlib import Path
import sys

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from bitbucket.repositories import list_repositories_with_branches


def main():
    repositories = list_repositories_with_branches()

    for repo in repositories:
        print(f"Repositorio: {repo['name']} | slug: {repo['slug']}")
        if repo.get("project"):
            print(f"Projeto: {repo['project']}")
        print(f"Privado: {repo['is_private']}")

        if not repo["branches"]:
            print("Branches: nenhuma branch encontrada")
        else:
            print("Branches:")
            for branch in repo["branches"]:
                print(f"  - {branch['name']}")

        print("-" * 60)


if __name__ == "__main__":
    main()
