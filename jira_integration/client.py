import os
import sys
from importlib import import_module
from pathlib import Path

from core.secrets import EnvSecretsProvider


def _load_jira_class():
    project_root = Path(__file__).resolve().parent.parent
    original_sys_path = sys.path[:]
    original_jira_module = sys.modules.get("jira")

    try:
        sys.path = [
            path for path in sys.path
            if Path(path or ".").resolve() != project_root
        ]

        if "jira" in sys.modules:
            del sys.modules["jira"]

        jira_module = import_module("jira")
        return jira_module.JIRA
    finally:
        sys.path = original_sys_path
        if original_jira_module is not None:
            sys.modules["jira"] = original_jira_module


def get_jira_client():
    secrets = EnvSecretsProvider()
    jira_url = secrets.get("JIRA_URL")
    jira_email = secrets.get("JIRA_EMAIL")
    jira_token = secrets.get("JIRA_TOKEN")

    jira_class = _load_jira_class()

    return jira_class(
        server=jira_url,
        basic_auth=(jira_email, jira_token),
    )
