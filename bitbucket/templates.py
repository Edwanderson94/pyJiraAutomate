from bitbucket.branches import create_branch
from bitbucket.repositories import create_repository, initialize_repository, list_branches


def create_template_repository(repo_slug, project_key, description=""):
    create_repository(
        repo_slug=repo_slug,
        project_key=project_key,
        is_private=True,
        description=description or f"Repositorio template do projeto {project_key}",
    )

    initialize_repository(
        repo_slug=repo_slug,
        readme_content=f"# {repo_slug}\n\nRepositorio inicializado automaticamente pelo pyJiraAutomate.\n",
        branch_name="master",
        commit_message="Initialize repository with README",
    )

    branches = [branch["name"] for branch in list_branches(repo_slug)]
    if "develop" not in branches:
        create_branch(repo_slug, "develop", "master")
    if "homolog" not in branches:
        create_branch(repo_slug, "homolog", "master")

    return {
        "repo_slug": repo_slug,
        "project_key": project_key,
        "branches": [branch["name"] for branch in list_branches(repo_slug)],
    }


def create_default_template_repositories():
    repositories = [
        ("template-qa", "QA"),
        ("template-sre", "SRE"),
        ("template-devops", "DEVOPS"),
    ]

    return [
        create_template_repository(repo_slug, project_key)
        for repo_slug, project_key in repositories
    ]
