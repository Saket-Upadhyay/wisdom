#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
WriterScript to BF Translator

Copyright (c) 2020 Saket Upadhyay | x64mayhem

https://github.com/Saket-Upadhyay/WriterScript
"""

bf2ws_dir = {
    '+': '5',
    '-': '6',
    '[': '7',
    ']': '8',
    '>': '9',
    '<': '10',
    ',': '11',
    '.': '12'
}
ws2bf_dir = {v: k for k, v in bf2ws_dir.items()}

import argparse as ap
import os

def getOpcodeFromFile(tarfile):
    with open(tarfile,'r') as infile:
        lines=infile.readlines()
        opcodebuffer=[]
        for line in lines:
            count=0
            line=line.split(' ')
            for word in line:
                if ((word == ',') or (word == '.')):
                    break;
                elif ((',' in word) or ('.' in word)):
                    count+=1
                    break;
                else:
                    count+=1
            opcodebuffer.append(str(count))
    return opcodebuffer


def ws_2_bf(wscript):
    out = ''
    try:
        for c in wscript:
            out += ws2bf_dir[c]
    except KeyError as e:
        print("Not a valid Writer Script.")
        exit(-1)
    return out

def bf_2_ws(bf_code):
    out = ''
    for c in bf_code:
        try:
            out += bf2ws_dir[c] + ' '
        except KeyError as e:
            pass
    return out




def getCodeSeq(tfile):
    opcodeSEQ=getOpcodeFromFile(tfile)
    opcodestring=""
    for opcode in opcodeSEQ:
        opcodestring+=" "+opcode

    return opcodestring



if __name__ == "__main__":

    bf_code2 = '+++++++++++++++++++++++++[>++>+++>++++>+++++<<<<-]+++++++++++++++++++++++++>>+++++.>+++++.++.----------.++.+++++.>--------..........<<<<++++++++.-----------------------.'
    bf_code='++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.'

    parser=ap.ArgumentParser(description='WriterScript Esoteric Language', epilog='~ with <3 by X64M')
    parser.add_argument('-s','--script',metavar='target_script',action='store',type=str,help='accepted inputs : .txt, .pen, .md')
    parser.add_argument('-t','--ture',action='store_true')

    args=parser.parse_args()
    print(args)
    targetfile=args.script

    if(targetfile != '') and (targetfile != None):
        if (targetfile in os.listdir()):
            opcodeseq=getOpcodeFromFile(targetfile)
            bfcode=ws_2_bf(opcodeseq)
            print(bfcode)
        else:
            print("File not found. Check name.")

    else:
        print("Script File not provided. use -h to check usage")
        print(bf_2_ws(bf_code))
        exit(-1)
