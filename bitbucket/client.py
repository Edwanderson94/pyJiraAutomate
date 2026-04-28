import os

import requests
from dotenv import load_dotenv

load_dotenv()

BITBUCKET_API_BASE_URL = "https://api.bitbucket.org/2.0"


def get_session():
    """
    Cria e retorna uma sessao autenticada com o Bitbucket.
    """
    username = os.getenv("BITBUCKET_USERNAME")
    token = os.getenv("BITBUCKET_APP_PASSWORD")

    if not username or not token:
        raise RuntimeError("Credenciais do Bitbucket nao encontradas no .env")

    session = requests.Session()
    session.auth = (username, token)
    session.headers.update({"Accept": "application/json"})

    return session


def bitbucket_get(url, params=None):
    """
    Executa um GET autenticado na API do Bitbucket e retorna o JSON.
    """
    session = get_session()
    response = session.get(url, params=params, timeout=30)
    response.raise_for_status()
    return response.json()


def bitbucket_paginated_get(url, params=None):
    """
    Percorre todos os resultados paginados da API do Bitbucket.
    """
    results = []
    next_url = url
    next_params = params.copy() if params else {}

    while next_url:
        payload = bitbucket_get(next_url, params=next_params)
        results.extend(payload.get("values", []))
        next_url = payload.get("next")
        next_params = None

    return results
