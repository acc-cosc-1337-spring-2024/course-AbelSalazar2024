#HW3 unit test

import unittest

from src.homework.d_repetition.repetition import get_factorial, sum_odd_number

class Test_Config(unittest.TestCase):

    def test_get_factorial(self):
        self.assertEqual(get_factorial(4), 24)
        self.assertEqual(get_factorial(5), 120)
        self.assertEqual(get_factorial(6), 720)

    def test_sum_odd_number(self):
        self.assertEqual(sum_odd_number(7), 16)
        self.assertEqual(sum_odd_number(9), 25)
        self.assertEqual(sum_odd_number(10), 25)
        
        