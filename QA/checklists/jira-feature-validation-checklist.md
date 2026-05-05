# Jira Feature Validation Checklist

- Confirm `JIRA_URL`, `JIRA_EMAIL`, and `JIRA_TOKEN` are present in `.env`.
- Confirm `.env` is ignored by Git and `.env.example` is versioned.
- Confirm the Jira client reads credentials through `EnvSecretsProvider`.
- Confirm the Jira site is reachable in the browser before running the feature.
- Run `python cli.py jira-list-projects --help` and verify the command is exposed.
- Run `python cli.py jira-list-projects` and capture the output in `QA/after/`.
- Validate that the response is structured JSON when the environment is healthy.
- If the call fails, record HTTP status code, endpoint, and error message.
- Check whether the failure comes from credentials, permissions, site availability, or local import issues.
- Run automated tests for the secrets flow before changing Jira authentication code.
- Record the exact branch used for the validation.
- Update `QA/after/` with a short report describing pass, fail, or blocked status.
- Before developing the next Jira capability, rerun this checklist to confirm the baseline remains healthy.
