import os
from jira import JIRA
from dotenv import load_dotenv

load_dotenv()

jira_url = os.getenv("JIRA_URL")
jira_email = os.getenv("JIRA_EMAIL")
jira_token = os.getenv("JIRA_TOKEN")

if not all([jira_url, jira_email, jira_token]):
    raise ValueError("Variáveis de ambiente do Jira não foram configuradas corretamente.")

jira = JIRA(
    server=jira_url,
    basic_auth=(jira_email, jira_token)
)

print("Conectado com sucesso!")
