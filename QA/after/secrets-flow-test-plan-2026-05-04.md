# Secrets Flow Test Plan

Date: 2026-05-04
Scope: `EnvSecretsProvider`, Jira integration, Bitbucket integration

## Objective

Validate the first secure configuration flow introduced in the application:

- secrets are loaded through `EnvSecretsProvider`
- `.env` remains local and ignored by Git
- `.env.example` is the safe committed reference
- Jira and Bitbucket clients consume secrets through the provider

## Planned automated checks

1. `EnvSecretsProvider` returns values when keys exist
2. `EnvSecretsProvider` raises an error for missing required keys
3. Jira client consumes `JIRA_URL`, `JIRA_EMAIL`, and `JIRA_TOKEN`
4. Bitbucket client consumes `BITBUCKET_USERNAME` and `BITBUCKET_APP_PASSWORD`

## Planned manual checks

1. Verify `.env` is ignored by Git
2. Verify `.env.example` contains placeholders only
3. Re-run Jira and Bitbucket CLI smoke tests after secrets changes

## Expected result

The configuration layer should be reusable, deterministic, and safe to evolve without exposing real credentials in version control.
