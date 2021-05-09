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
import os

from writerscript.interpreter import WriterScriptProgram
from writerscript.translator import getCodeSeq
from writerscript.generator import GEN


def load_source(file):
    if os.path.isfile(file):
        if ((os.path.splitext(file)[1] == ".pen") or (os.path.splitext(file)[1] == ".txt")):
            script_data=getCodeSeq(file)
            return script_data

        else:
            print("Not Valid Scripting File", file=sys.stderr)
            return False

    else:
        print("WriterScript: file does not exist", file=sys.stderr)
        return False


def evaluate(source):
    # Run WriterScript Interpreter

    program = WriterScriptProgram(source)
    program.run()

def gen(BFSF,TXTSF):
    GEN(BFSF,TXTSF)