#!/usr/bin/env python


class programreader(object):

    def __init__(self, program=None):
        self.program = ""
        self.length = 0
        self.count = 0
        self.finished = True

        if program:
            self.load(program)

    def load(self, program_data):
        self.program = program_data
        self.length = len(program_data)
        self.count = 0
        self.finished = False

    def next_c(self):
        if self.count >= self.length:
            self.finished = True
            return ""
        else:
            c = self.program[self.count]
            self.count += 1
            return c

    def unnext_c(self):
        if self.count > 0:
            self.count -= 1

    def peek(self):
        if self.count >= self.length:
            return ""
        else:
            c = self.program[self.count]
            return c


if __name__ == '__main__':
    import unittest
    from tests.testprogramreader import Testprogramreader
    Testprogramreader.header()
    unittest.main()
