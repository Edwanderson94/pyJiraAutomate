import os

from bitbucket.client import BITBUCKET_API_BASE_URL, bitbucket_get, bitbucket_post


def get_branch(repo_slug, branch_name):
    workspace = os.getenv("BITBUCKET_WORKSPACE")

    if not workspace:
        raise RuntimeError("BITBUCKET_WORKSPACE nao definido no .env")

    if not repo_slug:
        raise ValueError("repo_slug deve ser informado")

    if not branch_name:
        raise ValueError("branch_name deve ser informado")

    url = f"{BITBUCKET_API_BASE_URL}/repositories/{workspace}/{repo_slug}/refs/branches/{branch_name}"
    return bitbucket_get(url)


def create_branch(repo_slug, branch_name, target_hash="master"):
    workspace = os.getenv("BITBUCKET_WORKSPACE")

    if not workspace:
        raise RuntimeError("BITBUCKET_WORKSPACE nao definido no .env")

    if not repo_slug:
        raise ValueError("repo_slug deve ser informado")

    if not branch_name:
        raise ValueError("branch_name deve ser informado")

    url = f"{BITBUCKET_API_BASE_URL}/repositories/{workspace}/{repo_slug}/refs/branches"
    payload = {
        "name": branch_name,
        "target": {"hash": target_hash},
    }
    return bitbucket_post(url, payload=payload)
