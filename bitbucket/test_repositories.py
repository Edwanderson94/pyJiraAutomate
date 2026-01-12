from bitbucket.repositories import list_repositories


if __name__ == "__main__":
    repos = list_repositories()
    for repo in repos:
        print("-", repo["name"])
