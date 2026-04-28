import argparse
import json

from bitbucket.branches import create_branch, get_branch
from bitbucket.projects import create_project, delete_project, list_projects, update_project
from bitbucket.repositories import (
    create_repository,
    delete_repository,
    initialize_repository,
    list_branches,
    list_repositories,
)
from bitbucket.templates import create_default_template_repositories, create_template_repository


def _print_json(payload):
    print(json.dumps(payload, indent=2, ensure_ascii=True))


def handle_list_projects(_args):
    _print_json(list_projects())


def handle_create_project(args):
    result = create_project(
        project_key=args.project_key,
        project_name=args.project_name,
        description=args.description,
        is_private=not args.public,
    )
    _print_json(result)


def handle_update_project(args):
    result = update_project(
        project_key=args.project_key,
        project_name=args.project_name,
        description=args.description,
        is_private=not args.public,
        new_project_key=args.new_project_key,
    )
    _print_json(result)


def handle_delete_project(args):
    delete_project(args.project_key)
    print(f"Projeto removido: {args.project_key}")


def handle_list_repositories(_args):
    _print_json(list_repositories())


def handle_create_repository(args):
    result = create_repository(
        repo_slug=args.repo_slug,
        project_key=args.project_key,
        is_private=not args.public,
        description=args.description,
    )
    _print_json(result)


def handle_initialize_repository(args):
    result = initialize_repository(
        repo_slug=args.repo_slug,
        readme_content=args.readme_content,
        branch_name=args.branch_name,
        commit_message=args.commit_message,
    )
    _print_json(result)


def handle_delete_repository(args):
    delete_repository(args.repo_slug)
    print(f"Repositorio removido: {args.repo_slug}")


def handle_list_branches(args):
    _print_json(list_branches(args.repo_slug))


def handle_get_branch(args):
    _print_json(get_branch(args.repo_slug, args.branch_name))


def handle_create_branch(args):
    result = create_branch(
        repo_slug=args.repo_slug,
        branch_name=args.branch_name,
        target_hash=args.target_hash,
    )
    _print_json(result)


def handle_create_template_repository(args):
    result = create_template_repository(
        repo_slug=args.repo_slug,
        project_key=args.project_key,
        description=args.description,
    )
    _print_json(result)


def handle_create_default_templates(_args):
    _print_json(create_default_template_repositories())


def build_parser():
    parser = argparse.ArgumentParser(
        description="CLI do pyJiraAutomate para operacoes com Bitbucket Cloud."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_projects_parser = subparsers.add_parser("list-projects", help="Lista projetos do workspace.")
    list_projects_parser.set_defaults(func=handle_list_projects)

    create_project_parser = subparsers.add_parser("create-project", help="Cria um projeto.")
    create_project_parser.add_argument("project_key")
    create_project_parser.add_argument("project_name")
    create_project_parser.add_argument("--description", default="")
    create_project_parser.add_argument("--public", action="store_true")
    create_project_parser.set_defaults(func=handle_create_project)

    update_project_parser = subparsers.add_parser("update-project", help="Atualiza um projeto.")
    update_project_parser.add_argument("project_key")
    update_project_parser.add_argument("project_name")
    update_project_parser.add_argument("--new-project-key")
    update_project_parser.add_argument("--description", default="")
    update_project_parser.add_argument("--public", action="store_true")
    update_project_parser.set_defaults(func=handle_update_project)

    delete_project_parser = subparsers.add_parser("delete-project", help="Exclui um projeto vazio.")
    delete_project_parser.add_argument("project_key")
    delete_project_parser.set_defaults(func=handle_delete_project)

    list_repositories_parser = subparsers.add_parser("list-repositories", help="Lista repositorios do workspace.")
    list_repositories_parser.set_defaults(func=handle_list_repositories)

    create_repository_parser = subparsers.add_parser("create-repository", help="Cria um repositorio.")
    create_repository_parser.add_argument("repo_slug")
    create_repository_parser.add_argument("--project-key")
    create_repository_parser.add_argument("--description", default="")
    create_repository_parser.add_argument("--public", action="store_true")
    create_repository_parser.set_defaults(func=handle_create_repository)

    initialize_repository_parser = subparsers.add_parser("initialize-repository", help="Cria o primeiro commit com README.")
    initialize_repository_parser.add_argument("repo_slug")
    initialize_repository_parser.add_argument("--readme-content", default="# Repository\n\nInitialized by pyJiraAutomate.\n")
    initialize_repository_parser.add_argument("--branch-name", default="master")
    initialize_repository_parser.add_argument("--commit-message", default="Initial commit")
    initialize_repository_parser.set_defaults(func=handle_initialize_repository)

    delete_repository_parser = subparsers.add_parser("delete-repository", help="Exclui um repositorio.")
    delete_repository_parser.add_argument("repo_slug")
    delete_repository_parser.set_defaults(func=handle_delete_repository)

    list_branches_parser = subparsers.add_parser("list-branches", help="Lista branches de um repositorio.")
    list_branches_parser.add_argument("repo_slug")
    list_branches_parser.set_defaults(func=handle_list_branches)

    get_branch_parser = subparsers.add_parser("get-branch", help="Busca uma branch especifica.")
    get_branch_parser.add_argument("repo_slug")
    get_branch_parser.add_argument("branch_name")
    get_branch_parser.set_defaults(func=handle_get_branch)

    create_branch_parser = subparsers.add_parser("create-branch", help="Cria uma branch.")
    create_branch_parser.add_argument("repo_slug")
    create_branch_parser.add_argument("branch_name")
    create_branch_parser.add_argument("--target-hash", default="master")
    create_branch_parser.set_defaults(func=handle_create_branch)

    create_template_parser = subparsers.add_parser(
        "create-template-repository",
        help="Cria, inicializa e configura um repositorio template com master, develop e homolog.",
    )
    create_template_parser.add_argument("repo_slug")
    create_template_parser.add_argument("project_key")
    create_template_parser.add_argument("--description", default="")
    create_template_parser.set_defaults(func=handle_create_template_repository)

    create_default_templates_parser = subparsers.add_parser(
        "create-default-templates",
        help="Cria template-qa, template-sre e template-devops com branches padrao.",
    )
    create_default_templates_parser.set_defaults(func=handle_create_default_templates)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
