import os
from bitbucket.client import get_session


def list_repositories():
    session = get_session()
    workspace = os.getenv("BITBUCKET_WORKSPACE")

    if not workspace:
        raise RuntimeError("BITBUCKET_WORKSPACE não definido no .env")

    url = f"https://api.bitbucket.org/2.0/repositories/{workspace}"
    response = session.get(url)
    response.raise_for_status()

    return response.json()["values"]