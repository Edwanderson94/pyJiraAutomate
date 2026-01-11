
# pyJiraAutomate
Automatizações e utilitários para integração com Jira (Python).

## Descrição 🔧
Coleção de scripts e bibliotecas para automatizar criação/atualização de issues no Jira, geração de relatórios e integrações com pipelines.

## Principais funcionalidades ✨
- Criar e atualizar issues automaticamente
- Buscar e filtrar issues por JQL
- Exportar relatórios (CSV/JSON)
- Integração com CI/CD para automações

## Pré-requisitos ✅
- Python 3.8+
- Acesso à API do Jira (URL, usuário/token)
- Recomenda-se usar um virtual environment

## Instalação 🔧
```bash
# clonar repo
git clone <repo-url>
cd pyJiraAutomate

# criar venv (opcional, recomendado)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

# instalar dependências
pip install -r requirements.txt
# ou instalar dependências individuais
pip install python-dotenv requests jira
```

## Configuração (.env) 💡
Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis (exemplo):

```env
JIRA_URL=https://seu-jira.atlassian.net
JIRA_USER=seu-email@exemplo.com
JIRA_TOKEN=seu-token-api
DEFAULT_PROJECT=PROJ
```

> Observação: o projeto usa `python-dotenv` para carregar variáveis de ambiente.

## Uso — Exemplos 🔍
Como usar scripts CLI:

```bash
# Buscar issues por JQL
python scripts/search_issues.py --jql "project = PROJ AND status = 'To Do'"

# Criar issue
python scripts/create_issue.py --project PROJ --summary "Bug report" --description "Detalhes..."
```

Como usar como módulo:

```python
from pyjira import JiraClient

client = JiraClient.from_env()
issues = client.search("project=PROJ AND assignee=currentUser()")
```

## Estrutura do projeto 📁
- `scripts/` — scripts executáveis (CLI)
- `pyjira/` — código principal (clientes, utilitários)
- `tests/` — testes automatizados
- `docs/` — documentação adicional

## Testes 🧪
```bash
# rodar testes
pytest
# verificar cobertura (se configurado)
coverage run -m pytest && coverage report
```

## Contribuição 🤝
- Abra Issues para bugs/feature requests
- Faça branch a partir de `main`: `feature/nova-funcionalidade`
- Envie PR com descrição clara e testes

## Troubleshooting / FAQ ❓
- Erro de autenticação: verifique `JIRA_USER` e `JIRA_TOKEN`
- Timeout: ajustar variáveis de timeout nas configurações do cliente

## Licença 📜
Defina a licença do projeto (ex.: MIT). Consulte o arquivo `LICENSE` na raiz do repositório.

## Contato ✉️
Nome / e-mail do maintainer ou link para perfil no GitHub/GitLab
