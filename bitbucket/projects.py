import os

from bitbucket.client import (
    BITBUCKET_API_BASE_URL,
    bitbucket_delete,
    bitbucket_paginated_get,
    bitbucket_post,
    bitbucket_put,
)


def list_projects():
    workspace = os.getenv("BITBUCKET_WORKSPACE")

    if not workspace:
        raise RuntimeError("BITBUCKET_WORKSPACE nao definido no .env")

    url = f"{BITBUCKET_API_BASE_URL}/workspaces/{workspace}/projects"
    return bitbucket_paginated_get(url, params={"pagelen": 100})


def create_project(project_key, project_name, description="", is_private=True):
    workspace = os.getenv("BITBUCKET_WORKSPACE")

    if not workspace:
        raise RuntimeError("BITBUCKET_WORKSPACE nao definido no .env")

    if not project_key:
        raise ValueError("project_key deve ser informado")

    if not project_name:
        raise ValueError("project_name deve ser informado")

    url = f"{BITBUCKET_API_BASE_URL}/workspaces/{workspace}/projects"
    payload = {
        "key": project_key,
        "name": project_name,
        "description": description,
        "is_private": is_private,
    }
    return bitbucket_post(url, payload=payload)


def update_project(project_key, project_name, description="", is_private=True, new_project_key=None):
    workspace = os.getenv("BITBUCKET_WORKSPACE")

    if not workspace:
        raise RuntimeError("BITBUCKET_WORKSPACE nao definido no .env")

    if not project_key:
        raise ValueError("project_key deve ser informado")

    if not project_name:
        raise ValueError("project_name deve ser informado")

    url = f"{BITBUCKET_API_BASE_URL}/workspaces/{workspace}/projects/{project_key}"
    payload = {
        "key": new_project_key or project_key,
        "name": project_name,
        "description": description,
        "is_private": is_private,
    }
    return bitbucket_put(url, payload=payload)


def delete_project(project_key):
    workspace = os.getenv("BITBUCKET_WORKSPACE")

    if not workspace:
        raise RuntimeError("BITBUCKET_WORKSPACE nao definido no .env")

    if not project_key:
        raise ValueError("project_key deve ser informado")

    url = f"{BITBUCKET_API_BASE_URL}/workspaces/{workspace}/projects/{project_key}"
    return bitbucket_delete(url)
