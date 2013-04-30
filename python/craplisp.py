#!/usr/bin/env python

from libs import tokeniser, parser, interpreter

from sys import argv, exit


def error(message, callstack):
    print(message)
    for f in callstack:
        name = f[0]
        args = str(f[1])
        values = str(f[2])
        print("%s called with %s values for args %s" % (name, values, args))
    exit(1)


def main():
    inputfile = argv[1]

    with open(inputfile) as fp:
        input_program = fp.read()

    t = tokeniser(input_program)
    t.tokenise()

    p = parser(t.output)
    p.parse()

    i = interpreter(p.output, error)

    print(i.run())


if __name__ == '__main__':
    main()
