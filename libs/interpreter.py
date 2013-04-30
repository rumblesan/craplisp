#!/usr/bin/env python


class interpreter(object):

    def __init__(self, program=None, error_callback=None):
        self.symbol_table = {}
        self.method_table = {}
        self.setup_method_table()
        self.scopes = []
        self.local_scope = {}

        # error callback should accept an error message and
        # the callstack info
        self.error_callback = error_callback
        self.callstack = []

        self.functions = {}

        self.program = []

        if program:
            self.load(program)

    def load(self, program):
        self.program = program

    def error(self, msg):
        self.error_callback(msg, self.callstack)

    def run(self):
        for el in self.program:
            result = self.interpret(el)
            if result is not None:
                return result

    def create_local_scope(self, name, args, values):
        self.callstack.append((name, args, values))
        if len(args) is not len(values):
            self.error("Should be as many args as names")
        else:
            scope = {}
            for (k, v) in zip(args, values):
                scope[k] = v
            self.scopes.append(self.local_scope)
            self.local_scope = scope

        return scope

    def exit_local_scope(self):
        self.callstack.pop()
        if len(self.scopes) > 0:
            self.local_scope = self.scopes.pop()
        else:
            self.local_scope = {}

    def interpret(self, data):
        if isinstance(data, list):
            return self.interpret_expression(data[0], data[1:])
        elif data in self.local_scope:
            return self.interpret(self.local_scope[data])
        elif data in self.symbol_table:
            return self.symbol_table[data]
        else:
            return data

    def interpret_expression(self, expr, args):
        if expr in self.functions:
            return self.interpret_function(expr, self.functions[expr], args)
        if expr in self.method_table:
            return self.method_table[expr](args)
        else:
            self.error("%s doesn't appear to be a valid function" % expr)

    def interpret_function(self, name, func, args):
        self.create_local_scope(name, func['args'], args)
        r = self.interpret(func['body'])
        self.exit_local_scope()
        return r

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
            val = self.interpret(args[0])
            return val + self.plus(args[1:])

    def minus(self, args):
        val = self.interpret(args[0])
        for v in args[1:]:
            val -= self.interpret(v)
        return val

    def mult(self, args):
        if len(args) is 0:
            return 1
        else:
            val = self.interpret(args[0])
            return val * self.mult(args[1:])

    def divide(self, args):
        val = self.interpret(args[0])
        for v in args[1:]:
            val /= self.interpret(v)
        return val

    # comparison
    def greaterthan(self, args):

        def gt_recur(c, a):
            if len(a) is 1:
                n = self.interpret(a[0])
                return c > n
            else:
                n = self.interpret(a[0])
                return (c > n) and gt_recur(n, a[1:])
        current = self.interpret(args[0])
        return gt_recur(current, args[1:])

    def lessthan(self, args):

        def lt_recur(c, a):
            if len(a) is 1:
                n = self.interpret(a[0])
                return c < n
            else:
                n = self.interpret(a[0])
                return (c < n) and lt_recur(n, a[1:])
        current = self.interpret(args[0])
        return lt_recur(current, args[1:])

    def equals(self, args):

        def eq_recur(c, a):
            if len(a) is 1:
                n = self.interpret(a[0])
                return c == n
            else:
                n = self.interpret(a[0])
                return (c == n) and eq_recur(n, a[1:])
        current = self.interpret(args[0])
        return eq_recur(current, args[1:])

    # boolean
    def bool_and(self, args):
        if len(args) is 0:
            return True
        else:
            v = self.interpret(args[0])
            if not v:
                return False
            else:
                return v and self.bool_and(args[1:])

    def bool_or(self, args):
        if len(args) is 0:
            return False
        else:
            v = self.interpret(args[0])
            if v:
                return True
            else:
                return v or self.bool_or(args[1:])

    def bool_not(self, args):
        if len(args) is not 1:
            self.error("Should only be one arg for not")
        else:
            return not self.interpret(args[0])

    # conditional
    def cond(self, args):
        statements = args[0]
        for c in statements:
            if self.interpret(c[0]) is True:
                return self.interpret(c[1])
        self.error("Error, no true condition in cond")

    # define
    def define(self, args):

        def define_var(args):
            self.symbol_table[args[0]] = self.interpret(args[1])

        def define_func(args):
            func = {}
            header = args[0]
            body = args[1]
            name = header[0]
            func['args'] = header[1:]
            func['body'] = body
            self.functions[name] = func

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
