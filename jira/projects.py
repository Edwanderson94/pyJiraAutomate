from jira.client import get_jira_client


def list_projects():
    client = get_jira_client()
    projects = client.projects()

    return [
        {
            "key": project.key,
            "name": project.name,
            "id": project.id,
        }
        for project in projects
    ]
