import unittest
from unittest.mock import patch

from core.secrets import EnvSecretsProvider
from jira_integration.client import get_jira_client
from bitbucket.client import get_session


class EnvSecretsProviderTests(unittest.TestCase):
    @patch.dict(
        "os.environ",
        {
            "JIRA_TOKEN": "token-value",
        },
        clear=True,
    )
    def test_returns_secret_when_present(self):
        provider = EnvSecretsProvider()
        self.assertEqual(provider.get("JIRA_TOKEN"), "token-value")

    @patch.dict("os.environ", {}, clear=True)
    def test_raises_when_secret_is_missing(self):
        provider = EnvSecretsProvider()

        with self.assertRaises(ValueError) as context:
            provider.get("JIRA_TOKEN")

        self.assertIn("JIRA_TOKEN", str(context.exception))


class JiraIntegrationSecretsTests(unittest.TestCase):
    @patch("jira_integration.client._load_jira_class")
    @patch.dict(
        "os.environ",
        {
            "JIRA_URL": "https://example.atlassian.net",
            "JIRA_EMAIL": "user@example.com",
            "JIRA_TOKEN": "jira-token",
        },
        clear=True,
    )
    def test_get_jira_client_reads_secrets_from_provider(self, jira_class_loader):
        jira_class = jira_class_loader.return_value

        get_jira_client()

        jira_class.assert_called_once_with(
            server="https://example.atlassian.net",
            basic_auth=("user@example.com", "jira-token"),
        )


class BitbucketSecretsTests(unittest.TestCase):
    @patch.dict(
        "os.environ",
        {
            "BITBUCKET_USERNAME": "user@example.com",
            "BITBUCKET_APP_PASSWORD": "bitbucket-token",
        },
        clear=True,
    )
    def test_get_session_reads_secrets_from_provider(self):
        session = get_session()

        self.assertEqual(session.auth, ("user@example.com", "bitbucket-token"))
        self.assertEqual(session.headers.get("Accept"), "application/json")


if __name__ == "__main__":
    unittest.main()
