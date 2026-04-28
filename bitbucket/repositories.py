import os

from bitbucket.client import (
    BITBUCKET_API_BASE_URL,
    bitbucket_delete,
    bitbucket_form_post,
    bitbucket_paginated_get,
    bitbucket_post,
)


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


def create_repository(repo_slug, project_key=None, is_private=True, scm="git", description=""):
    workspace = os.getenv("BITBUCKET_WORKSPACE")

    if not workspace:
        raise RuntimeError("BITBUCKET_WORKSPACE nao definido no .env")

    if not repo_slug:
        raise ValueError("repo_slug deve ser informado")

    url = f"{BITBUCKET_API_BASE_URL}/repositories/{workspace}/{repo_slug}"
    payload = {
        "scm": scm,
        "is_private": is_private,
        "description": description,
    }

    if project_key:
        payload["project"] = {"key": project_key}

    return bitbucket_post(url, payload=payload)


def delete_repository(repo_slug):
    workspace = os.getenv("BITBUCKET_WORKSPACE")

    if not workspace:
        raise RuntimeError("BITBUCKET_WORKSPACE nao definido no .env")

    if not repo_slug:
        raise ValueError("repo_slug deve ser informado")

    url = f"{BITBUCKET_API_BASE_URL}/repositories/{workspace}/{repo_slug}"
    return bitbucket_delete(url)


def initialize_repository(repo_slug, readme_content, branch_name="master", commit_message="Initial commit"):
    workspace = os.getenv("BITBUCKET_WORKSPACE")

    if not workspace:
        raise RuntimeError("BITBUCKET_WORKSPACE nao definido no .env")

    if not repo_slug:
        raise ValueError("repo_slug deve ser informado")

    if not readme_content:
        raise ValueError("readme_content deve ser informado")

    url = f"{BITBUCKET_API_BASE_URL}/repositories/{workspace}/{repo_slug}/src"
    data = {
        "message": commit_message,
        "branch": branch_name,
        "/README.md": readme_content,
    }
    return bitbucket_form_post(url, data=data)
