#!/usr/bin/env python

from programreader import programreader

import re


class tokeniser(programreader):

    def __init__(self):
        self.char_re = re.compile("""[a-zA-Z]""")
        self.space_re = re.compile("""[\s]""")
        self.num_re = re.compile("""[0-9]""")
        self.sym_re = re.compile("""[^a-zA-Z0-9"\s()]""")

        self.output = []

    def is_char(self, char):
        if self.char_re.match(char):
            return True
        else:
            return False

    def is_number(self, char):
        if self.num_re.match(char):
            return True
        else:
            return False

    def is_symbol(self, char):
        if self.sym_re.match(char):
            return True
        else:
            return False

    def is_whitespace(self, char):
        if self.space_re.match(char):
            return True
        else:
            return False

    def parse_number(self):
        num = ""
        while True:
            if self.is_number(self.peek()):
                num += self.next_c()
            else:
                break
        return ("NUMBER", int(num))

    def parse_name(self):
        name = ""
        while True:
            if self.is_char(self.peek()):
                name += self.next_c()
            else:
                break
        return ("NAME", name)

    def parse_symbol(self):
        symbol = ""
        while True:
            if self.is_symbol(self.peek()):
                symbol += self.next_c()
            else:
                break
        return ("SYMBOL", symbol)

    def parse_string(self):
        string = ""
        #skip the double quote at the front
        self.next_c()
        while True:
            c = self.peek()
            if c is '"' or c is "":
                #skip the second double quote
                self.next_c()
                break
            else:
                string += self.next_c()
        return ("STRING", string)

    def tokenise(self):

        while not self.finished:
            c = self.peek()

            if self.is_whitespace(c):
                self.next_c()
                pass
            elif c is "(" or c is ")":
                self.output.append(("PAREN", c))
                self.next_c()
            elif self.is_number(c):
                self.output.append(self.parse_number())
            elif self.is_char(c):
                self.output.append(self.parse_name())
            elif c is '"':
                self.output.append(self.parse_string())
            elif c is "":
                self.finished = True
            elif self.is_symbol(c):
                self.output.append(self.parse_symbol())


if __name__ == '__main__':
    import unittest
    from tests.testtokeniser import Testtokeniser
    Testtokeniser.header()
    unittest.main()
