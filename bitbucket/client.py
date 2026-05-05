import requests
from core.secrets import EnvSecretsProvider

BITBUCKET_API_BASE_URL = "https://api.bitbucket.org/2.0"


def get_session():
    """
    Cria e retorna uma sessao autenticada com o Bitbucket.
    """
    secrets = EnvSecretsProvider()
    username = secrets.get("BITBUCKET_USERNAME")
    token = secrets.get("BITBUCKET_APP_PASSWORD")

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


def bitbucket_post(url, payload=None, params=None):
    """
    Executa um POST autenticado na API do Bitbucket e retorna o JSON.
    """
    session = get_session()
    response = session.post(url, params=params, json=payload, timeout=30)
    response.raise_for_status()
    return response.json()


def bitbucket_put(url, payload=None, params=None):
    """
    Executa um PUT autenticado na API do Bitbucket e retorna o JSON.
    """
    session = get_session()
    response = session.put(url, params=params, json=payload, timeout=30)
    response.raise_for_status()
    return response.json()


def bitbucket_delete(url, params=None):
    """
    Executa um DELETE autenticado na API do Bitbucket.
    """
    session = get_session()
    response = session.delete(url, params=params, timeout=30)
    response.raise_for_status()
    return response


def bitbucket_form_post(url, data=None, files=None, params=None):
    """
    Executa um POST autenticado usando form data ou multipart.
    """
    session = get_session()
    response = session.post(url, params=params, data=data, files=files, timeout=30)
    response.raise_for_status()
    if not response.text.strip():
        return {}

    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        return {"raw_response": response.text}


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
