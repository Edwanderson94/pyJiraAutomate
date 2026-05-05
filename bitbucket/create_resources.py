from bitbucket.branches import create_branch
from bitbucket.projects import create_project
from bitbucket.repositories import create_repository


def main():
    print("Exemplos de uso:")
    print("create_project('QAUTO', 'Automacoes QA', 'Projeto de testes')")  # noqa: T201
    print("create_repository('novo-repo-exemplo', project_key='QAUTO')")  # noqa: T201
    print("create_branch('python-automate', 'feature/exemplo-api', 'master')")  # noqa: T201


if __name__ == "__main__":
    main()
