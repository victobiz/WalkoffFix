# coding: utf-8

"""
    WALKOFF

    An active cyber defense development framework enabling orchestration capabilities to be written once and deployed across WALKOFF-enabled orchestration tools. https://nsacyber.github.io/WALKOFF/  # noqa: E501

    The version of the OpenAPI document: 0.9.1
    Contact: walkoff@nsa.gov
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import walkoff_client
from walkoff_client.api.authorization_api import AuthorizationApi  # noqa: E501
from walkoff_client.rest import ApiException


class TestAuthorizationApi(unittest.TestCase):
    """AuthorizationApi unit test stubs"""

    def setUp(self):
        self.api = walkoff_client.api.authorization_api.AuthorizationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_login(self):
        """Test case for login

        Login and get access and refresh tokens  # noqa: E501
        """
        pass

    def test_logout(self):
        """Test case for logout

        Logout of walkoff  # noqa: E501
        """
        pass

    def test_refresh(self):
        """Test case for refresh

        Get a fresh access token  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
