#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
writerscript module.
A Brain F*ck derivative based on number of words as opcode.

Copyright (c) 2020 Saket Upadhyay

https://github.com/Saket-Upadhyay/WriterScript
"""

from __future__ import print_function

import sys
import ply.yacc as yacc
import ply.lex as lex

tokens = (
    "INC",
    "DEC",
    "SHL",
    "SHR",
    "OUT",
    "IN",
    "OPEN_LOOP",
    "CLOSE_LOOP",
)

t_INC = r'5'
t_DEC = r'6'
t_SHL = r'10'
t_SHR = r'9'
t_OUT = r'12'
t_IN = r'11'
t_OPEN_LOOP = r'7'
t_CLOSE_LOOP = r'8'


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


t_ignore = " \t"


def t_error(t):
    t.lexer.skip(1)


def p_commands(p):
    """
    commands : command
             | commands command
    """
    if len(p) == 2:
        p[0] = Commands()
        p[0].commands = [p[1]]
        return

    if not p[1]:
        p[1] = Commands()

    p[1].commands.append(p[2])
    p[0] = p[1]


def p_command(p):
    """
    command : INC
            | DEC
            | SHL
            | SHR
            | OUT
            | IN
            | loop
    """
    if isinstance(p[1], str):
        p[0] = Command(p[1])
    else:
        p[0] = p[1]


def p_loop(p):
    """
    loop : OPEN_LOOP commands CLOSE_LOOP
    """
    p[0] = Loop(p[2])


def p_error(p):
    print("Syntax error in input!")


class WriterScriptProgram:
    def __init__(self, source):
        self.source = source

    def run(self):
        self.data = [0] * 1000
        self.location = 0
        commands = self.parse(self.source)
        commands.run(self)

    def parse(self, source):
        lexer = lex.lex()
        parser = yacc.yacc(debug=False, write_tables=False)
        return parser.parse(source)

    def __str__(self):
        return str(self.parse(self.source))


class Commands:
    def __init__(self):
        self.commands = []

    def run(self, program):
        for command in self.commands:
            command.run(program)

    def __str__(self):
        return "".join([str(command) for command in self.commands])


class Command:
    def __init__(self, command):
        self.command = command

    def run(self, program):
        if isinstance(self.command, Loop):
            self.command.run(program)

        if self.command == t_INC:
            if program.data[program.location] >= 255:
                program.data[program.location]=0
            else:
                program.data[program.location] += 1
        if self.command == t_DEC:
            if program.data[program.location] <= 0:
                program.data[program.location]=255
            else:
                program.data[program.location] -= 1
            
        if self.command == t_SHL:
            program.location -= 1
        if self.command == t_SHR:
            program.location += 1
        if self.command == t_OUT:
            sys.stdout.write(chr(program.data[program.location]))
        if self.command == t_IN:
            try:
                RIN=int(input("Input (0-255) >"))
                if RIN<0 or RIN>255:
                    print("\nError (x_x) : I/O Exception, Exiting.")
                    exit(-1)
                else:
                    program.data[program.location]=RIN
            except Exception:
                print("\nError (x_x) : I/O Exception, Exiting.")
                program.data = None
                exit(-1)


    def __str__(self):
        return self.command


class Loop:
    def __init__(self, commands):
        self.commands = commands

    def run(self, program):
        while program.data[program.location] != 0:
            self.commands.run(program)

    def __str__(self):
        return t_OPEN_LOOP + str(self.commands) + t_CLOSE_LOOP
