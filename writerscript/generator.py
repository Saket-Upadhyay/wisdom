"""
writerscript.generator module.
BrainFuck To Writer Script Generator with custom Text.

Copyright (c) 2020 Saket Upadhyay

https://github.com/Saket-Upadhyay/WriterScript
"""
bf2ws_dir = {
    '+': 5,
    '-': 6,
    '[': 7,
    ']': 8,
    '>': 9,
    '<': 10,
    ',': 11,
    '.': 12
}

def bf2wsop(bfstr):
    opcodes=[]
    for i in bfstr:
        opcodes.append(bf2ws_dir[i])
    return opcodes

def GEN(BFsourceDATA,TextSourceData):

    bfc=BFsourceDATA
    lims=bf2wsop(bfc)

    cycle=False
    

    sum=0
    for i in lims:
        sum+=i
    

    sourcedat=TextSourceData

    srcString=sourcedat.split(' ')

    if (len(srcString)<sum):
        print("WARNING (>_>) - Not Enough Source Feed : "+str(sum)+" Words Needed, but, only "+str(len(srcString))+" Loaded.\nTrying to reuse the buffer by activating cycling mode, but this is experimental feature and sometimes cause long delay and will result in repeated text blocks in output. Try to Provide text source with enough words.\n")

    while(len(srcString)<sum):
        srcString+=srcString
        cycle=True
        

    if cycle:
        print("INFO (o_o) :Source Feed : "+str(sum)+" Words Needed, "+str(len(srcString))+" Provided [Block Cycle Mode].\n")
    else:
        print("INFO (o_o) :Source Feed : "+str(sum)+" Words Needed, "+str(len(srcString))+" Provided [Linear Mode].\n")



    sptr=0
    dptr=0
    FINALDATA=""
    for lim in lims:
        dat=""
        dptr+=lim
        try:
            for i in range(sptr,dptr):
                    dat+=srcString[i]+' '
        except IndexError:
            print("Error (x_x) - Not Enough Source Feed : "+str(sum)+" Words Needed, "+str(len(srcString))+" Provided. Exiting.")
            exit(-1)

        dat=dat[0:-1]
        FINALDATA=FINALDATA+dat+','+'\n'
        sptr+=lim
    print("DONE (^_^).")
    return FINALDATA


if __name__ == "__main__":
    pass