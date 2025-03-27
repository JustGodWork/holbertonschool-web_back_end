#!/usr/bin/env python3
"""
Unit tests for client.GithubOrgClient class.
"""

import unittest
from unittest.mock import PropertyMock, patch
from parameterized import parameterized
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
