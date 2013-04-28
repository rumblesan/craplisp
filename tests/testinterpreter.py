#!/usr/bin/env python

import unittest
from interpreter import interpreter


class Testinterpreter(unittest.TestCase):

    @staticmethod
    def header():
        print("\n")
        print("*************************************")
        print("    Running tests on interpreter")
        print("*************************************")
        print("\n")

    def setUp(self):
        self.interpreter = interpreter()

    def tearDown(self):
        del self.interpreter

    def test_creation(self):
        self.assertIsInstance(self.interpreter, interpreter)

    def test_single_num(self):
        program = [5]
        self.interpreter.setup(program)
        result = self.interpreter.run()
        self.assertEqual(5, result)

    def test_plus_basic(self):
        program = [["+", 5, 4]]
        self.interpreter.setup(program)
        result = self.interpreter.run()
        self.assertEqual(9, result)

    def test_plus_multi(self):
        program = [["+", 5, 4, 3, 2, 1]]
        self.interpreter.setup(program)
        result = self.interpreter.run()
        self.assertEqual(15, result)

    def test_minus(self):
        program = [["-", 5, 4]]
        self.interpreter.setup(program)
        result = self.interpreter.run()
        self.assertEqual(1, result)

    def test_minus_multi(self):
        program = [["-", 10, 2, 2, 3]]
        self.interpreter.setup(program)
        result = self.interpreter.run()
        self.assertEqual(3, result)

    def test_multiply(self):
        program = [["*", 5, 4]]
        self.interpreter.setup(program)
        result = self.interpreter.run()
        self.assertEqual(20, result)

    def test_multiply_multi(self):
        program = [["*", 5, 4, 2, 3]]
        self.interpreter.setup(program)
        result = self.interpreter.run()
        self.assertEqual(120, result)

    def test_divide(self):
        program = [["/", 10, 2]]
        self.interpreter.setup(program)
        result = self.interpreter.run()
        self.assertEqual(5, result)

    def test_divide_multi(self):
        program = [["/", 100, 2, 5]]
        self.interpreter.setup(program)
        result = self.interpreter.run()
        self.assertEqual(10, result)

    def test_maths_nested(self):
        program = [["+",
                   ["*", 3, 5],
                   ["-", 9,
                       ["*", 2, 2]],
                   5]]
        self.interpreter.setup(program)
        result = self.interpreter.run()
        self.assertEqual(25, result)

    def test_greaterthan(self):
        program = [[">", 5, 4]]
        self.interpreter.setup(program)
        result = self.interpreter.run()
        self.assertTrue(result)

        program = [[">", 5, 6]]
        self.interpreter.setup(program)
        result = self.interpreter.run()
        self.assertFalse(result)

    def test_greaterthan_multi(self):
        program = [[">", 5, 4, 3]]
        self.interpreter.setup(program)
        result = self.interpreter.run()
        self.assertTrue(result)

        program = [[">", 5, 4, 6]]
        self.interpreter.setup(program)
        result = self.interpreter.run()
        self.assertFalse(result)

    def test_lessthan(self):
        program = [["<", 5, 6]]
        self.interpreter.setup(program)
        result = self.interpreter.run()
        self.assertTrue(result)

        program = [["<", 5, 4]]
        self.interpreter.setup(program)
        result = self.interpreter.run()
        self.assertFalse(result)

    def test_lessthan_multi(self):
        program = [["<", 5, 6, 7]]
        self.interpreter.setup(program)
        result = self.interpreter.run()
        self.assertTrue(result)

        program = [["<", 5, 6, 5]]
        self.interpreter.setup(program)
        result = self.interpreter.run()
        self.assertFalse(result)

    def test_equal(self):
        program = [["=", 5, 5]]
        self.interpreter.setup(program)
        result = self.interpreter.run()
        self.assertTrue(result)

        program = [["=", 5, 4]]
        self.interpreter.setup(program)
        result = self.interpreter.run()
        self.assertFalse(result)

    def test_equal_multi(self):
        program = [["=", 5, 5, 5]]
        self.interpreter.setup(program)
        result = self.interpreter.run()
        self.assertTrue(result)

        program = [["=", 5, 5, 3]]
        self.interpreter.setup(program)
        result = self.interpreter.run()
        self.assertFalse(result)

    def test_bool_and(self):
        program = [["and",
                   ["=", 5, 5],
                   ["=", 5, 5]]]
        self.interpreter.setup(program)
        result = self.interpreter.run()
        self.assertTrue(result)

        program = [["and",
                   ["=", 5, 5],
                   ["=", 5, 6]]]
        self.interpreter.setup(program)
        result = self.interpreter.run()
        self.assertFalse(result)

    def test_bool_or(self):
        program = [["or",
                   ["=", 5, 5],
                   ["=", 5, 5]]]
        self.interpreter.setup(program)
        result = self.interpreter.run()
        self.assertTrue(result)

        program = [["or",
                   ["=", 5, 5],
                   ["=", 5, 6]]]
        self.interpreter.setup(program)
        result = self.interpreter.run()
        self.assertTrue(result)

        program = [["or",
                   ["=", 5, 7],
                   ["=", 5, 6]]]
        self.interpreter.setup(program)
        result = self.interpreter.run()
        self.assertFalse(result)

    def test_bool_not(self):
        program = [["not", ["=", 5, 5]]]
        self.interpreter.setup(program)
        result = self.interpreter.run()
        self.assertFalse(result)

        program = [["not", ["=", 5, 6]]]
        self.interpreter.setup(program)
        result = self.interpreter.run()
        self.assertTrue(result)

