import os
from jira import JIRA
from dotenv import load_dotenv

load_dotenv()

jira = JIRA(
    server=os.getenv("JIRA_URL"),
    basic_auth=(
        os.getenv("JIRA_EMAIL"),
        os.getenv("JIRA_TOKEN")
    )
)

print("Conectado com sucesso!")