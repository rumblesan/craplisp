#!/usr/bin/env python

from programreader import programreader

import re


class tokeniser(programreader):

    def __init__(self, program=None):
        self.space_re = re.compile("""[\s]""")
        self.num_re = re.compile("""[0-9]""")
        self.sym_re = re.compile("""[^"\s()]""")

        self.output = []

        super(tokeniser, self).__init__(program)

    def is_number(self, char):
        return self.num_re.match(char) is not None

    def is_symbol(self, char):
        return self.sym_re.match(char) is not None

    def is_whitespace(self, char):
        return self.space_re.match(char) is not None

    def parse_number(self):
        num = ""
        while True:
            if self.is_number(self.peek()):
                num += self.next()
            else:
                break
        return ("NUMBER", int(num))

    def parse_symbol(self):
        symbol = ""
        while True:
            if self.is_symbol(self.peek()):
                symbol += self.next()
            else:
                break
        return ("SYMBOL", symbol)

    def parse_string(self):
        string = ""
        #skip the double quote at the front
        self.next()
        while True:
            c = self.peek()
            if c is '"' or c is "":
                #skip the second double quote
                self.next()
                break
            else:
                string += self.next()
        return ("STRING", string)

    def tokenise(self):

        while not self.finished:
            c = self.peek()

            if self.is_whitespace(c):
                self.next()
                pass
            elif c is "(" or c is ")":
                self.output.append(("PAREN", c))
                self.next()
            elif self.is_number(c):
                self.output.append(self.parse_number())
            elif self.is_symbol(c):
                self.output.append(self.parse_symbol())
            elif c is '"':
                self.output.append(self.parse_string())
            elif c is "":
                self.finished = True


if __name__ == '__main__':
    import unittest
    from tests.testtokeniser import Testtokeniser
    Testtokeniser.header()
    unittest.main()
