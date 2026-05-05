# pyJiraAutomate

Automacoes em Python para Jira e Bitbucket Cloud. O projeto nasceu como apoio operacional e hoje ja oferece uma camada reutilizavel para administrar projetos, repositorios e branches no Bitbucket, com uma estrutura simples de QA para validar mudancas antes e depois da execucao.

## O que a aplicacao faz hoje

### Jira

- abre uma conexao com Jira usando variaveis de ambiente
- lista projetos do Jira

### Bitbucket Cloud

- lista projetos do workspace
- cria projetos
- atualiza nome e key de projetos
- exclui projetos vazios
- lista repositorios
- cria repositorios
- inicializa repositorios vazios com um primeiro commit
- exclui repositorios
- lista branches
- consulta uma branch especifica
- cria branches
- cria repositorios template com `master`, `develop` e `homolog`

### QA

- organiza validacoes em `before/` e `after/`
- mantem checklists e planos de teste

## Estrutura do projeto

```text
pyJiraAutomate/
|-- jira/
|   |-- __init__.py
|   |-- client.py
|   `-- projects.py
|-- jira_integration/
|   |-- __init__.py
|   |-- client.py
|   `-- projects.py
|-- bitbucket/
|   |-- __init__.py
|   |-- client.py
|   |-- projects.py
|   |-- repositories.py
|   |-- branches.py
|   |-- templates.py
|   |-- list_workspace_inventory.py
|   |-- create_resources.py
|   `-- delete_projects.py
|-- QA/
|   |-- before/
|   |-- after/
|   `-- checklists/
|-- cli.py
|-- requirements.txt
`-- README.md
```

## Requisitos

- Python 3.10+
- acesso ao Jira
- acesso ao Bitbucket Cloud
- `App Password` do Bitbucket com permissao compativel com leitura e escrita

## Instalacao

```powershell
git clone <repo-url>
cd pyJiraAutomate
python -m venv desenvolvimento
.\desenvolvimento\Scripts\activate
pip install -r requirements.txt
```

## Configuracao

Crie um arquivo `.env` na raiz do projeto:

```env
# Jira
JIRA_URL=https://seu-jira.atlassian.net
JIRA_EMAIL=seu-email@dominio.com
JIRA_TOKEN=seu-token-jira

# Bitbucket Cloud
BITBUCKET_WORKSPACE=seu-workspace
BITBUCKET_REPO=seu-repositorio
BITBUCKET_USERNAME=seu-email@dominio.com
BITBUCKET_APP_PASSWORD=seu-app-password
```

## Como a aplicacao funciona

O fluxo principal do Bitbucket esta dividido em camadas:

1. [bitbucket/client.py](/c:/Users/usuario/Documents/repo/pyJiraAutomate/bitbucket/client.py) autentica e encapsula `GET`, `POST`, `PUT`, `DELETE` e paginacao.
2. [bitbucket/projects.py](/c:/Users/usuario/Documents/repo/pyJiraAutomate/bitbucket/projects.py) cuida dos projetos.
3. [bitbucket/repositories.py](/c:/Users/usuario/Documents/repo/pyJiraAutomate/bitbucket/repositories.py) cuida dos repositorios e da inicializacao.
4. [bitbucket/branches.py](/c:/Users/usuario/Documents/repo/pyJiraAutomate/bitbucket/branches.py) cuida da criacao e consulta de branches.
5. [bitbucket/templates.py](/c:/Users/usuario/Documents/repo/pyJiraAutomate/bitbucket/templates.py) agrupa fluxos prontos para repositorios template.

Quando a aplicacao consulta listas da API, a paginacao e tratada automaticamente.

No Jira, a primeira camada reutilizavel foi isolada em um pacote proprio para evitar conflito com a biblioteca `jira` instalada:

1. [jira_integration/client.py](/c:/Users/usuario/Documents/repo/pyJiraAutomate/jira_integration/client.py) para conexao autenticada
2. [jira_integration/projects.py](/c:/Users/usuario/Documents/repo/pyJiraAutomate/jira_integration/projects.py) para listagem de projetos

## CLI para o consumidor

Agora o projeto possui um ponto de entrada unico em [cli.py](/c:/Users/usuario/Documents/repo/pyJiraAutomate/cli.py). Isso deixa a aplicacao mais amigavel para quem consome sem precisar montar scripts Python toda vez.

Formato geral:

```powershell
.\desenvolvimento\Scripts\python.exe cli.py <comando> [argumentos]
```

### Comandos de projeto

Listar projetos:

```powershell
.\desenvolvimento\Scripts\python.exe cli.py list-projects
```

Listar projetos do Jira:

```powershell
.\desenvolvimento\Scripts\python.exe cli.py jira-list-projects
```

Criar projeto:

```powershell
.\desenvolvimento\Scripts\python.exe cli.py create-project QA QA --description "Projeto de qualidade"
```

Atualizar projeto:

```powershell
.\desenvolvimento\Scripts\python.exe cli.py update-project PROJETO1 QA --new-project-key QA --description "Projeto QA"
```

Excluir projeto vazio:

```powershell
.\desenvolvimento\Scripts\python.exe cli.py delete-project QA
```

### Comandos de repositorio

Listar repositorios:

```powershell
.\desenvolvimento\Scripts\python.exe cli.py list-repositories
```

Criar repositorio:

```powershell
.\desenvolvimento\Scripts\python.exe cli.py create-repository meu-novo-repo --project-key QA --description "Repositorio de exemplo"
```

Inicializar repositorio vazio com README:

```powershell
.\desenvolvimento\Scripts\python.exe cli.py initialize-repository meu-novo-repo --branch-name master --commit-message "Initial commit"
```

Excluir repositorio:

```powershell
.\desenvolvimento\Scripts\python.exe cli.py delete-repository meu-novo-repo
```

### Comandos de branch

Listar branches:

```powershell
.\desenvolvimento\Scripts\python.exe cli.py list-branches meu-novo-repo
```

Buscar branch:

```powershell
.\desenvolvimento\Scripts\python.exe cli.py get-branch meu-novo-repo master
```

Criar branch:

```powershell
.\desenvolvimento\Scripts\python.exe cli.py create-branch meu-novo-repo develop --target-hash master
```

### Comandos de template

Criar um repositorio template individual:

```powershell
.\desenvolvimento\Scripts\python.exe cli.py create-template-repository template-qa QA
```

Criar o conjunto padrao:

```powershell
.\desenvolvimento\Scripts\python.exe cli.py create-default-templates
```

Esse fluxo:

- cria o repositorio
- faz o primeiro commit com `README.md`
- garante `master`
- cria `develop`
- cria `homolog`

## Uso como biblioteca

Se preferir usar direto no Python, as funcoes continuam disponiveis.

Criar repositorio:

```python
from bitbucket.repositories import create_repository

create_repository(
    repo_slug="meu-novo-repo",
    project_key="QA",
    is_private=True,
    description="Repositorio criado via automacao",
)
```

Inicializar repositorio:

```python
from bitbucket.repositories import initialize_repository

initialize_repository(
    repo_slug="meu-novo-repo",
    readme_content="# meu-novo-repo\n\nRepositorio inicializado.\n",
    branch_name="master",
    commit_message="Initial commit",
)
```

Criar branch:

```python
from bitbucket.branches import create_branch

create_branch(
    repo_slug="meu-novo-repo",
    branch_name="develop",
    target_hash="master",
)
```

Criar projeto:

```python
from bitbucket.projects import create_project

create_project(
    project_key="QA",
    project_name="QA",
    description="Projeto de qualidade",
    is_private=True,
)
```

Listar projetos do Jira:

```python
from jira_integration.projects import list_projects

for project in list_projects():
    print(project["key"], project["name"])
```

## Scripts auxiliares

[list_workspace_inventory.py](/c:/Users/usuario/Documents/repo/pyJiraAutomate/bitbucket/list_workspace_inventory.py) imprime um inventario do workspace com repositorios e branches.

```powershell
.\desenvolvimento\Scripts\python.exe bitbucket\list_workspace_inventory.py
```

[create_resources.py](/c:/Users/usuario/Documents/repo/pyJiraAutomate/bitbucket/create_resources.py) mostra exemplos simples de uso.

[delete_projects.py](/c:/Users/usuario/Documents/repo/pyJiraAutomate/bitbucket/delete_projects.py) mostra um exemplo de exclusao de projetos.

## QA e validacao

A pasta [QA](/c:/Users/usuario/Documents/repo/pyJiraAutomate/QA) ajuda a registrar baselines, resultados e checklists.

Arquivos principais:

- [QA/README.md](/c:/Users/usuario/Documents/repo/pyJiraAutomate/QA/README.md)
- [baseline-checklist.md](/c:/Users/usuario/Documents/repo/pyJiraAutomate/QA/checklists/baseline-checklist.md)
- [bitbucket-resource-creation-plan.md](/c:/Users/usuario/Documents/repo/pyJiraAutomate/QA/before/bitbucket-resource-creation-plan.md)

Uso sugerido:

1. registrar o estado atual em `QA/before`
2. executar a mudanca
3. validar o resultado em `QA/after`

## Limitacoes importantes

- branch pertence a repositorio, nao a projeto
- projeto nao pode ser excluido se contiver repositorios
- repositorio vazio precisa de um commit base antes da criacao normal de novas branches
- nomes de repositorio precisam ser unicos no workspace do Bitbucket Cloud

## Proximos passos recomendados

- adicionar testes automatizados para os modulos do Bitbucket
- padronizar logs e mensagens de erro
- expandir a parte de Jira alem da conexao basica
- evoluir Jira com listagem de issue types, criacao de issue e busca por JQL
- empacotar a aplicacao para distribuicao mais formal
