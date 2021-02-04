#!/usr/bin/env python3
""" Test SUITE Unittest module Task """
import requests
from unittest import mock
from unittest.mock import patch, PropertyMock
import unittest
from parameterized import parameterized

from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Class for testing Nested Map function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        """ Test method return output """
        real_output = access_nested_map(map, path)
        self.assertEqual(real_output, expected_output)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        '''
            Tests access_nested_map for raised expections.
        '''
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    '''
    get_json tests.
    '''

    @parameterized.expand([
        ('http://example.com', {"payload": True}),
        ('http://holberton.io', {"payload": False})
    ])
    def test_get_json(self, url, expected_result):
        '''
            Tests if get_json function returns the expected result.
        '''
        with mock.patch('utils.requests') as mock_request:
            mock_request.get.return_value = expected_result
            x = mock_request.get(url)
            self.assertEqual(expected_result, x)


class TestMemoize(unittest.TestCase):
    """
    utils.memoize tests.
    """
    def test_memoize(self):
        '''
            Test memoize.
        '''
        class TestClass:
            ''' TestClass for memoize. '''
            def a_method(self):
                ''' Returns 42. '''
                return 42

            @memoize
            def a_property(self):
                ''' Returns the class a_method . '''
                return self.a_method()

        with patch.object(TestClass, 'a_method') as am:
            am.return_value = 42
            tc = TestClass()
            self.assertEqual(tc.a_property, am.return_value)
            self.assertEqual(tc.a_property, am.return_value)
            am.assert_called_once()
