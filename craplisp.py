#!/usr/bin/env python

from libs import tokeniser, parser, interpreter

from sys import argv


def main():
    inputfile = argv[1]

    with open(inputfile) as fp:
        input_program = fp.read()

    t = tokeniser()
    p = parser()
    i = interpreter()

    t.load(input_program)
    t.tokenise()

    p.setup(t.output)
    p.parse()

    i.setup(p.output)
    result = i.run()

    print(result)


if __name__ == '__main__':
    main()
