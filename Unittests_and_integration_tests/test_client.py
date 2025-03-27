#!/usr/bin/env python3
"""
Unit tests for client.GithubOrgClient class.
"""

import unittest
from unittest.mock import PropertyMock, patch
from parameterized import parameterized, parameterized_class
from unittest import TestCase
from unittest.mock import patch
from fixtures import TEST_PAYLOAD
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test case for the GithubOrgClient class.
    """

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, expected, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.
        """
        mock_get_json.return_value = expected
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):
        """
        Test that GithubOrgClient._public_repos_url returns the expected value.
        """
        payload = {
            "repos_url": "https://api.github.com/orgs/test_org/repos"
        }
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock:
            mock.return_value = payload
            client = GithubOrgClient("test_org")
            result = client._public_repos_url

            mock.assert_called_once()
            self.assertEqual(result, payload["repos_url"])

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """
            Test that GithubOrgClient.public_repos
            returns the expected list of repos.
        """
        url = "https://api.github.com/orgs/test_org/repos"
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        with patch.object(GithubOrgClient, "_public_repos_url",
                          new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = url
            client = GithubOrgClient("test_org")
            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2", "repo3"])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({"license": None}, "my_license", False),
        ({}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test that GithubOrgClient.has_license returns the correct value.
        """
        client = GithubOrgClient("test_org")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(TestCase):
    """
    Integration test case for GithubOrgClient.public_repos.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the class by patching requests.get and mocking its behavior.
        """
        cls.get_patcher = patch(
            "requests.get",
            **{"return_value.json.side_effect": [
                cls.org_payload, cls.repos_payload,
                cls.org_payload, cls.repos_payload
            ]}
        )

        # Start the patcher
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """
        Tear down the class by stopping the patcher.
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
            Test that GithubOrgClient.public_repos
            returns the expected list of repos.
        """
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test that GithubOrgClient.public_repos filters repos by license.
        """
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(license="apache-2.0"),
                         self.apache2_repos)
