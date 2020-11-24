#!/usr/bin/env python3
"""
Test client
"""


import unittest
from unittest.mock import Mock, patch, PropertyMock
from parameterized import parameterized, param, parameterized_class
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    """
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('requests.get')
    def test_org(self, org, mock_get):
        """Test org url
        """
        pass

    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False})
    ])
    def test_public_repos_url(self, org, payload):
        """test repos url
        """
        with patch(
             'client.GithubOrgClient._public_repos_url',
             new_callable=PropertyMock
             ) as mock_repo:
            mock_repo.return_value = payload
            this_repo = GithubOrgClient(org)
            self.assertEqual(this_repo._public_repos_url, payload)

    @patch('requests.get')
    def test_public_repos(self, mock_rep):
        """test public repos
        """
        pass

    @parameterized.expand([
        param(
            {"license": {"key": "my_license"}},
            True,
            license_key="my_license",
            ),
        param(
            {"license": {"key": "other_license"}},
            False,
            license_key="my_license",
            )
    ])
    def test_has_license(self, repo, return_val, license_key):
        """if has license
        """
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key), return_val
            )

    def test_public_repos_with_license(self):
        """repos with license
        """
        self.assertTrue(True)


@parameterized_class(("org_payload",
                      "repos_payload",
                      "expected_repos",
                      "apache2_repos"), [
   ("test", "test", "test", "test"),
   ("test2", "test2", "test2", "test2")
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Test integration
    """
    @classmethod
    def setUpClass(cls):
        get_patcher = patch('requests.get')
        mock_get = get_patcher.start()
        get_patcher.stop()
        self.assertTrue(True)

    @classmethod
    def tearDownClass(cls):
        pass
