#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from holes import num_buracos


class TestNumHoles(unittest.TestCase):
    def test_parameter_acceptance(self):
        self.assertFalse(num_buracos())
        self.assertFalse(num_buracos(None))
        self.assertFalse(num_buracos([]))

    def test_reject_dictionaries(self):
        self.assertFalse(num_buracos({'a': 1}))
    
    def test_reject_numbers(self):
        self.assertFalse(num_buracos(666))

    def test_accept_string_of_numbers(self):
        self.assertEqual(num_buracos('666'), 0)

    def test_reject_list_of_numbers(self):
        self.assertFalse(num_buracos([1, 2, 3]))
        self.assertFalse(num_buracos([1, 'aaa', 3]))
        self.assertFalse(num_buracos(['1', 'aaa', 3]))
        self.assertFalse(num_buracos(['1', 'aaa', None]))

    def test_correctness(self):
        self.assertEqual(num_buracos(['aaa', 'b01']), 4)
        self.assertEqual(num_buracos('b01'), 1)
        self.assertEqual(num_buracos('b01'), 1)
        self.assertEqual(num_buracos('ABc'), 3)
        self.assertEqual(num_buracos(''), 0)

if __name__ == '__main__':
    unittest.main()
