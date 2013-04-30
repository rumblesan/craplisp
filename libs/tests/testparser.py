#!/usr/bin/env python

import unittest
from parser import parser


class Testparser(unittest.TestCase):

    @staticmethod
    def header():
        print("\n")
        print("*************************************")
        print("    Running tests on parser")
        print("*************************************")
        print("\n")

    def setUp(self):
        self.parser = parser()

    def tearDown(self):
        del self.parser

    def test_creation(self):
        self.assertIsInstance(self.parser, parser)

    def test_creation_with_args(self):
        input_tokens = [("PAREN",  "("),
                        ("NUMBER", "34"),
                        ("PAREN",  ")")]
        p = parser(input_tokens)
        self.assertIsInstance(p, parser)

    def test_basic_parse(self):
        input_tokens = [("PAREN",  "("),
                        ("NUMBER", "34"),
                        ("PAREN",  ")")]
        correct_output = [["34"]]
        self.parser.setup(input_tokens)
        self.parser.parse()
        self.assertListEqual(correct_output, self.parser.output)

    def test_bigger_input_parse(self):
        input_tokens = [("PAREN",  "("),

                        ("SYMBOL", "+"),

                        ("PAREN",  "("),
                        ("SYMBOL", "*"),
                        ("NUMBER", "345"),
                        ("NUMBER", "86"),
                        ("PAREN",  ")"),

                        ("PAREN",  "("),
                        ("SYMBOL", "/"),
                        ("NUMBER", "100"),
                        ("NUMBER", "5"),
                        ("PAREN",  ")"),

                        ("PAREN",  ")")]
        correct_output = [["+", ["*", "345", "86"], ["/", "100", "5"]]]
        self.parser.setup(input_tokens)
        self.parser.parse()
        self.assertListEqual(correct_output, self.parser.output)

    def test_multisection_parse(self):
        input_tokens = [("PAREN",  "("),
                        ("NAME",   "defn"),
                        ("NAME",   "a"),
                        ("NUMBER", "20"),
                        ("PAREN",  ")"),

                        ("PAREN",  "("),
                        ("SYMBOL", "+"),

                        ("PAREN",  "("),
                        ("SYMBOL", "*"),
                        ("NUMBER", "345"),
                        ("NAME",   "a"),
                        ("PAREN",  ")"),

                        ("PAREN",  "("),
                        ("SYMBOL", "/"),
                        ("NUMBER", "100"),
                        ("NUMBER", "5"),
                        ("PAREN",  ")"),

                        ("PAREN",  ")")]
        correct_output = [["defn", "a", "20"],
                          ["+", ["*", "345", "a"], ["/", "100", "5"]]]
        self.parser.setup(input_tokens)
        self.parser.parse()
        self.assertListEqual(correct_output, self.parser.output)
