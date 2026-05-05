import os

from dotenv import load_dotenv

load_dotenv()


class EnvSecretsProvider:
    def get(self, key):
        value = os.getenv(key)
        if not value:
            raise ValueError(f"Secret '{key}' nao encontrada no ambiente.")
        return value
