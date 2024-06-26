#HW6 unittest

import unittest

from src.homework.i_dictionaries_sets.sets import get_students_who_took_prog1_and_prog2, get_students_who_took_prog1_not_prog_2, get_students_who_took_prog2_not_prog_1, get_students_who_took_prog2_only

class Test_Config(unittest.TestCase):

    def test_get_students_who_took_prog1_and_prog2(self):
        prog1 = {'Student1', 'Student2', 'Student3'}
        prog2 = {'Student3', 'Student4', 'Student5'}
        expected_result = {'Student3'}
        self.assertEqual(get_students_who_took_prog1_and_prog2(prog1, prog2), expected_result)

    def test_get_students_who_took_prog2_only(self):
        prog1 = {'Student1', 'Student2', 'Student3'}
        prog2 = {'Student3', 'Student4', 'Student5'}
        expected_result = {'Student4', 'Student5'}
        self.assertEqual(get_students_who_took_prog2_only(prog1, prog2), expected_result)

    def test_get_students_who_took_prog1_not_prog_2(self):
        prog1 = {'Student1', 'Student2', 'Student3'}
        prog2 = {'Student3', 'Student4', 'Student5'}
        expected_result = {'Student1', 'Student2'}
        self.assertEqual(get_students_who_took_prog1_not_prog_2(prog1, prog2), expected_result)

    def test_get_students_who_took_prog2_not_prog_1(self):
        prog1 = {'Student1', 'Student2', 'Student3'}
        prog2 = {'Student3', 'Student4', 'Student5'}
        expected_result = {'Student4', 'Student5'}
        self.assertEqual(get_students_who_took_prog2_not_prog_1(prog1, prog2), expected_result)
