import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_session():
    """
    Cria e retorna uma sessão autenticada com o Bitbucket
    """
    username = os.getenv("BITBUCKET_USERNAME")
    token = os.getenv("BITBUCKET_APP_PASSWORD")

    if not username or not token:
        raise RuntimeError("Credenciais do Bitbucket não encontradas no .env")

    session = requests.Session()
    session.auth = (username, token)

    return session