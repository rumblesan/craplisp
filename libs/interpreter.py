#!/usr/bin/env python


class interpreter(object):

    def __init__(self, tokens=None):
        self.symbol_table = {}
        self.method_table = {}
        self.setup_method_table()
        if tokens:
            self.setup(tokens)

    def setup(self, program):
        self.program = program

    def run(self):
        for el in self.program:
            result = self.interpret(el)
            if result is not None:
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

        self.method_table["define"] = self.define
        self.method_table["cond"] = self.cond

    # maths
    def plus(self, args):
        if len(args) is 0:
            return 0
        else:
            val = self.interpret(args.pop(0))
            return val + self.plus(args)

    def minus(self, args):
        val = self.interpret(args.pop(0))
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
        val = self.interpret(args.pop(0))
        for v in args:
            val /= self.interpret(v)
        return val

    # comparison
    def greaterthan(self, args):

        def gt_recur(c, a):
            if len(a) is 1:
                n = self.interpret(a.pop(0))
                return c > n
            else:
                n = self.interpret(a.pop(0))
                return (c > n) and gt_recur(n, a)
        current = self.interpret(args.pop(0))
        return gt_recur(current, args)

    def lessthan(self, args):

        def lt_recur(c, a):
            if len(a) is 1:
                n = self.interpret(a.pop(0))
                return c < n
            else:
                n = self.interpret(a.pop(0))
                return (c < n) and lt_recur(n, a)
        current = self.interpret(args.pop(0))
        return lt_recur(current, args)

    def equals(self, args):

        def eq_recur(c, a):
            if len(a) is 1:
                n = self.interpret(a.pop(0))
                return c == n
            else:
                n = self.interpret(a.pop(0))
                return (c == n) and eq_recur(n, a)
        current = self.interpret(args.pop(0))
        return eq_recur(current, args)

    # boolean
    def bool_and(self, args):
        if len(args) is 0:
            return True
        else:
            v = self.interpret(args.pop(0))
            if not v:
                return False
            else:
                return v and self.bool_and(args)

    def bool_or(self, args):
        if len(args) is 0:
            return False
        else:
            v = self.interpret(args.pop(0))
            if v:
                return True
            else:
                return v or self.bool_or(args)

    def bool_not(self, args):
        if len(args) is not 1:
            print("Should only be one arg for not")
        else:
            return not self.interpret(args.pop(0))

    # conditional
    def cond(self, args):
        statements = args[0]
        for c in statements:
            if self.interpret(c[0]) is True:
                return self.interpret(c[1])
        print("Error, no true condition in cond")

    # define
    def define(self, args):

        def define_var(args):
            self.symbol_table[args[0]] = self.interpret(args[1])

        def define_func(args):
            print("can't define functions yet")
            pass

        if isinstance(args[0], list):
            define_func(args)
        else:
            define_var(args)

        return None


if __name__ == '__main__':
    import unittest
    from tests.testinterpreter import Testinterpreter
    Testinterpreter.header()
    unittest.main()
