# Secrets Validation Checklist

- Confirm `.env` is present only locally and is not tracked by Git.
- Confirm `.env.example` is present and contains placeholder values only.
- Run `git check-ignore -v .env` and verify `.env` is ignored by `.gitignore`.
- Validate that `EnvSecretsProvider` returns values for configured keys.
- Validate that `EnvSecretsProvider` raises an error when a required key is missing.
- Validate that Jira integration reads `JIRA_URL`, `JIRA_EMAIL`, and `JIRA_TOKEN` through the provider.
- Validate that Bitbucket integration reads `BITBUCKET_USERNAME` and `BITBUCKET_APP_PASSWORD` through the provider.
- Run automated tests for `core/secrets.py`, `jira_integration/client.py`, and `bitbucket/client.py`.
- Record the branch and date of the validation in `QA/after/`.
- Never store real secrets in committed QA evidence files.
