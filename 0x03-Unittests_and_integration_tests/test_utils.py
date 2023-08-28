#!/usr/bin/env python3
"""
Parameterize a unit test
"""
import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Tests the 'access_nested_map' function
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self,
                               nested_map: Dict,
                               path: Tuple[str],
                               expected_result: Union[Dict, int]) -> None:
        """
        Tests `access_nested_map`'s output
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)


if __name__ == "__main__":
    unittest.main()
