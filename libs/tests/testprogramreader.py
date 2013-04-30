#!/usr/bin/env python

import unittest
from programreader import programreader


class Testprogramreader(unittest.TestCase):

    @staticmethod
    def header():
        print("\n")
        print("*************************************")
        print("    Running tests on programreader")
        print("*************************************")
        print("\n")

    def setUp(self):
        self.programreader = programreader()

    def tearDown(self):
        del self.programreader

    def test_creation(self):
        self.assertIsInstance(self.programreader, programreader)

    def test_load(self):
        self.assertTrue(self.programreader.finished)
        self.programreader.load("this is just a test")
        self.assertFalse(self.programreader.finished)
        self.assertEqual(19, self.programreader.length)

    def test_creation_arg_load(self):
        test_program = "this is just a test"
        p = programreader(test_program)
        self.assertFalse(p.finished)
        self.assertEqual(19, p.length)

    def test_empty(self):
        self.programreader.load("")
        self.assertEqual("", self.programreader.peek())
        self.assertFalse(self.programreader.finished)
        self.assertEqual("", self.programreader.next_c())
        self.assertTrue(self.programreader.finished)

    def test_end_condition(self):
        self.programreader.load("ab")
        self.assertEqual("a", self.programreader.peek())
        self.assertEqual("a", self.programreader.next_c())
        self.assertFalse(self.programreader.finished)
        self.assertEqual("b", self.programreader.peek())
        self.assertEqual("b", self.programreader.next_c())
        self.assertFalse(self.programreader.finished)
        self.assertEqual("", self.programreader.peek())
        self.assertEqual("", self.programreader.next_c())
        self.assertTrue(self.programreader.finished)

    def test_unnext(self):
        self.programreader.load("ab")
        self.assertEqual("a", self.programreader.peek())
        self.assertEqual("a", self.programreader.next_c())
        self.assertFalse(self.programreader.finished)
        self.assertEqual("b", self.programreader.peek())
        self.programreader.unnext_c()
        self.assertEqual("a", self.programreader.peek())
        self.assertEqual("a", self.programreader.next_c())
        self.assertFalse(self.programreader.finished)
        self.assertEqual("b", self.programreader.peek())
        self.assertEqual("b", self.programreader.next_c())
        self.assertFalse(self.programreader.finished)
        self.assertEqual("", self.programreader.peek())
        self.assertEqual("", self.programreader.next_c())
        self.assertTrue(self.programreader.finished)

    def test_char_commands(self):
        input_program = "abcdefg"
        self.programreader.load(input_program)
        self.assertEqual("a", self.programreader.peek())
        self.assertEqual("a", self.programreader.next_c())
        self.assertEqual("b", self.programreader.next_c())
        self.assertEqual("c", self.programreader.next_c())
        self.assertEqual("d", self.programreader.peek())
        self.assertEqual("d", self.programreader.peek())
        self.programreader.unnext_c()
        self.assertEqual("c", self.programreader.peek())
        self.assertEqual("c", self.programreader.next_c())
        self.assertEqual("d", self.programreader.next_c())
        self.assertEqual("e", self.programreader.next_c())
        self.assertEqual("f", self.programreader.next_c())
        self.assertEqual("g", self.programreader.next_c())
        self.assertEqual("", self.programreader.peek())
        self.assertEqual("", self.programreader.peek())
        self.assertEqual("", self.programreader.next_c())
        self.assertTrue(self.programreader.finished)

    def test_with_list(self):
        input_data = [1, 2, 3, 4, 5]
        self.programreader.load(input_data)
        self.assertEqual(1, self.programreader.peek())
        self.assertEqual(1, self.programreader.next_c())
        self.assertEqual(2, self.programreader.next_c())
        self.assertEqual(3, self.programreader.next_c())
        self.assertEqual(4, self.programreader.peek())
        self.assertEqual(4, self.programreader.peek())
