import os

from bitbucket.client import BITBUCKET_API_BASE_URL, bitbucket_paginated_get


def list_repositories():
    workspace = os.getenv("BITBUCKET_WORKSPACE")

    if not workspace:
        raise RuntimeError("BITBUCKET_WORKSPACE nao definido no .env")

    url = f"{BITBUCKET_API_BASE_URL}/repositories/{workspace}"
    return bitbucket_paginated_get(url, params={"pagelen": 100})


def list_branches(repo_slug):
    workspace = os.getenv("BITBUCKET_WORKSPACE")

    if not workspace:
        raise RuntimeError("BITBUCKET_WORKSPACE nao definido no .env")

    if not repo_slug:
        raise ValueError("repo_slug deve ser informado")

    url = f"{BITBUCKET_API_BASE_URL}/repositories/{workspace}/{repo_slug}/refs/branches"
    return bitbucket_paginated_get(url, params={"pagelen": 100})


def list_repositories_with_branches():
    repositories_with_branches = []

    for repo in list_repositories():
        repo_slug = repo["slug"]
        repositories_with_branches.append(
            {
                "name": repo["name"],
                "slug": repo_slug,
                "project": repo.get("project", {}).get("name"),
                "is_private": repo.get("is_private"),
                "branches": list_branches(repo_slug),
            }
        )

    return repositories_with_branches
