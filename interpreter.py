#!/usr/bin/env python


class interpreter(object):

    def __init__(self):
        self.symbol_table = {}
        self.method_table = {}
        self.setup_method_table()

    def setup(self, program):
        self.program = program

    def run(self):
        for el in self.program:
            result = self.interpret(el)
            if result:
                return result

    def interpret(self, data):
        if isinstance(data, list):
            expr = data.pop(0)
            return self.interpret_expression(expr, data)
        elif data in self.symbol_table:
            return self.symbol_table[data]
        else:
            return data

    def interpret_expression(self, expr, args):
        if expr in self.method_table:
            return self.method_table[expr](args)
        else:
            print("error")

    def setup_method_table(self):
        self.method_table["+"] = self.plus
        self.method_table["-"] = self.minus
        self.method_table["*"] = self.mult
        self.method_table["/"] = self.divide

        self.method_table[">"] = self.greaterthan
        self.method_table["<"] = self.lessthan
        self.method_table["="] = self.equals

        self.method_table["and"] = self.bool_and
        self.method_table["or"] = self.bool_or
        self.method_table["not"] = self.bool_not

        self.method_table["define"] = self.cond
        self.method_table["cond"] = self.define

    # maths
    def plus(self, args):
        if len(args) is 0:
            return 0
        else:
            val = self.interpret(args.pop(0))
            return val + self.plus(args)

    def minus(self, args):
        val = args.pop(0)
        for v in args:
            val -= self.interpret(v)
        return val

    def mult(self, args):
        if len(args) is 0:
            return 1
        else:
            val = self.interpret(args.pop(0))
            return val * self.mult(args)

    def divide(self, args):
        val = args.pop(0)
        for v in args:
            val /= self.interpret(v)
        return val

    # comparison
    def greaterthan(self, args):
        pass

    def lessthan(self, args):
        pass

    def equals(self, args):
        pass

    # boolean
    def bool_and(self, args):
        pass

    def bool_or(self, args):
        pass

    def bool_not(self, args):
        pass

    # conditional
    def cond(self, args):
        pass

    # define
    def define(self, args):
        pass


if __name__ == '__main__':
    import unittest
    from tests.testinterpreter import Testinterpreter
    Testinterpreter.header()
    unittest.main()