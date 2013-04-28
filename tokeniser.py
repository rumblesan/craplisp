#!/usr/bin/env python

import re


class tokeniser(object):

    def __init__(self):
        self.char_re = re.compile("""[a-zA-Z0-9"']""")

    def setup(self, program_data):
        self.program = program_data

    def long_token(self, char):
        if self.char_re.match(char):
            return True
        else:
            return False

    def parse(self):
        output = []
        current_token = ""

        for c in self.program:

            if c == " ":
                if len(current_token) > 0:
                    output.append(current_token)
                    current_token = ""
                else:
                    continue
            else:
                if self.long_token(c) is True:
                    current_token += c
                else:
                    if len(current_token) > 0:
                        output.append(current_token)
                        current_token = ""
                    output.append(c)

        return output


if __name__ == '__main__':
    import unittest
    from tests.testtokeniser import Testtokeniser
    Testtokeniser.header()
    unittest.main()
