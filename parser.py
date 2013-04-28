#!/usr/bin/env python


class parser(object):

    def __init__(self):
        self.tokens = []
        self.output = []

    def setup(self, tokens):
        self.tokens = tokens

    def parse(self):
        # reversing so we can just keep calling pop
        data = list(self.tokens)
        data.reverse()
        # assuming the first element is a PAREN
        # Also assuming that the parens are already balanced
        el = data.pop()
        if el[1] is not "(":
            print("ERROR HERE")
        else:
            self.output = self.parse_list(data)

    def parse_list(self, token_data):
        out = []
        while True:
            el = token_data.pop()
            if el[1] is "(":
                out.append(self.parse_list(token_data))
            elif el[1] is ")":
                break
            else:
                out.append(el[1])
        return out


if __name__ == '__main__':
    import unittest
    from tests.testparser import Testparser
    Testparser.header()
    unittest.main()
