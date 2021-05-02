#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
writerscript.cli module

Command Line Interface for WriterScript.

Copyright (c) 2020 Saket Upadhyay | x64mayhem

https://github.com/Saket-Upadhyay/WriterScript
"""

from __future__ import print_function

import argparse
import setup

import writerscript


def main():
    """Run application as a CLI executable"""
    a1=arg_parser = argparse.ArgumentParser(
        prog="wscript",
        description="A Writer-Script EsoLang interpreter Module written in Python3",
        argument_default=argparse.SUPPRESS,
        epilog="~ <3 X64M"
    )

    a2=arg_parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s {0}".format(setup.__VERSION__),
    )

    a3=arg_parser.add_argument('-e',action='store_true',help='Toggle Execution',dest="execute")

    a3=arg_parser.add_argument('-s','--script',metavar='target_script',action='store',type=str,help='Writer Script to Execute,accepted inputs : .txt, .pen',dest="script")

    a4=arg_parser.add_argument('-g',action='store_true',help='Toggle Generator',dest="generate")
    a5=arg_parser.add_argument('-sbf',metavar='SourceBFCode',action='store',type=str,help='Source oneliner BF Code File, accepted inputs : .txt',dest="srcbf")
    arg_parser.add_argument('-stxt',metavar='SourceTXT',action='store',type=str,help='Source oneliner Text Template File : .txt',dest="srctxt")
    arg_parser.set_defaults(func=lambda args: arg_parser.print_help())

    args = arg_parser.parse_args()


    gen=False
    exe=False

    args = arg_parser.parse_args()

    try:
        if args.generate:
            gen=True
        else:
            gen=False
    except Exception:
        pass
    try:
        if args.execute:
            exe=True
        else:
            exe=False
    except Exception:
        pass




    try:
        if(gen):
            if args.srcbf and args.srctxt:
                writerscript.gen(args.srcbf,args.srctxt)
            else:
                arg_parser.print_usage()

        elif(exe):
            sourcecode = writerscript.load_source(args.script)

            if sourcecode:
                writerscript.evaluate(sourcecode)
            else:
                arg_parser.print_usage()
        else:
            arg_parser.print_usage()
    except AttributeError:
        arg_parser.print_usage()
        exit(-1)
    except KeyboardInterrupt:
        print("\nError (x_x) : User Interrupt, Exiting.")
        exit(-1)


if __name__ == "__main__":
    main()
