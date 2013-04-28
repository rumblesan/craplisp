#!/usr/bin/env python

import unittest
from tokeniser import tokeniser


class Testtokeniser(unittest.TestCase):

    @staticmethod
    def header():
        print("\n")
        print("*************************************")
        print("    Running tests on tokeniser")
        print("*************************************")
        print("\n")

    def setUp(self):
        self.tokeniser = tokeniser()

    def tearDown(self):
        del self.tokeniser

    def test_creation(self):
        self.assertIsInstance(self.tokeniser, tokeniser)

    def test_is_char(self):
        self.assertTrue(self.tokeniser.is_char("c"))
        self.assertFalse(self.tokeniser.is_char("4"))

    def test_is_number(self):
        self.assertTrue(self.tokeniser.is_number("4"))
        self.assertFalse(self.tokeniser.is_number("c"))

    def test_is_symbol(self):
        self.assertTrue(self.tokeniser.is_symbol("+"))
        self.assertFalse(self.tokeniser.is_symbol("c"))

    def test_simple_program(self):
        input_program = "()"
        correct_output = [("PAREN", "("), ("PAREN", ")")]
        self.tokeniser.load(input_program)
        self.tokeniser.tokenise()
        self.assertListEqual(correct_output, self.tokeniser.output)

    def test_bigger_program(self):
        correct_output = [("PAREN",  "("),
                          ("SYMBOL", "+"),
                          ("PAREN",  "("),
                          ("SYMBOL", "*"),
                          ("NUMBER", "4"),
                          ("NUMBER", "5"),
                          ("PAREN",  ")"),
                          ("NUMBER", "4"),
                          ("PAREN",  ")")]
        input_program = "(+ (* 4 5) 4)"
        self.tokeniser.load(input_program)
        self.tokeniser.tokenise()
        self.assertListEqual(correct_output, self.tokeniser.output)

#    def test_longer_variable_program(self):
#        correct_output = ["(", "+", "(", "*", "45", "579", ")", "4000", ")"]
#        input_program = "(+ (* 45 579) 4000)"
#        token_output = self.tokeniser.tokenise(input_program)
#        self.assertListEqual(correct_output, token_output)
#
#    def test_badly_formatted_program(self):
#        correct_output = ["(", "+", "(", "*", "45", "579", ")", "4000", ")"]
#        input_program = "(+(*   45 579  )4000)   "
#        token_output = self.tokeniser.tokenise(input_program)
#        self.assertListEqual(correct_output, token_output)
#
#    def test_string_and_names_program(self):
#        correct_output = ["(", "cond", "(", ">", "45", "579", ")",
#                          "(", "=", '"foo"', '"bar"', ")", ")"]
#        input_program = '(cond (> 45 579) (= "foo" "bar"))'
#        token_output = self.tokeniser.tokenise(input_program)
#        self.assertListEqual(correct_output, token_output)
