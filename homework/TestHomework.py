import unittest
from unittest import mock
from homework.EpamHomework import EpamHomework

class TestHomework(unittest.TestCase):
    def test_odd_even_indexes(self):
        tests = [
            (
                (
                    [1, 3, 5, 7],
                    [8, 2, 7, 4]
                ),
                [3, 7, 8, 7]
            ),
            (
                (
                    [10],
                    [2, 3, 4]
                ),
                [2, 4]
            ),
            (
                (
                    [1, 3, 5, 7],
                    []
                ),
                [3, 7]
            ),
            (
                (
                    [1, 3, 5, 7],
                    ['a', 'b', 'c', 'd']
                ),
                [3, 7, 'a', 'c']
            ),
            (
                (
                    [],
                    []
                ),
                []
            ),
        ]

        for params, expected_result in tests:
            self.assertEqual(
                EpamHomework.odd_even_indexes(*params),
                expected_result
            )