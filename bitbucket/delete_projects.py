from requests import HTTPError

from bitbucket.projects import delete_project


def main():
    for project_key in ["AUT", "TER"]:
        try:
            delete_project(project_key)
            print(f"Projeto removido: {project_key}")
        except HTTPError as exc:
            response = exc.response
            details = response.text if response is not None else str(exc)
            print(f"Falha ao remover {project_key}: {details}")


if __name__ == "__main__":
    main()
