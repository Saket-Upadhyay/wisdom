from flask import Flask,request,jsonify
from flask import render_template
import random

import writerscript
from writerscript import generator
import base64
from modules.brainfuckgenerator import BFGenerator

app: Flask = Flask(__name__)
SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'

global FORMDATA
global DECODEDDATA
DECODEDDATA=''
FORMDATA= ''

@app.route('/')
def hello_world():
    return render_template("splash.html")


@app.route('/main')
def maincandy():
    return render_template("candymain.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/why')
def why():
    return render_template("why.html")


@app.route('/creditcard')
def creditcard():
    return render_template("card.html")


@app.route('/comp')
def comp():
    return render_template("comp.html")


@app.route('/getcarddata',methods=['POST'])
def getcarddata():
    global FORMDATA
    data=request.form.to_dict()
    print(data)
    FORMDATA=data
    return "OK"

@app.route('/checkformdatarender')
def checkformdatarender():
    global FORMDATA
    # FORMDATA={'name': 'Saket Upadhyay', 'cardno': '3714 496353 98431', 'expdate': '08/78', 'cvv': '345'}
    datmod=str(FORMDATA)
    data_bytes=datmod.encode('ascii')
    base64data=base64.b64encode(data_bytes)
    base64text=base64data.decode('ascii')
    bfg=BFGenerator()
    bf_source=bfg.text_to_brainfuck(base64text)

    rindex=random.randint(0,6) # choose any one of the 5 sources given in source.txt
    print("using data source "+str(rindex)+"\n")
    with open('data/source.txt','r') as src:
        sourcedat=list(src)[rindex].strip('\n')


    ws_source=generator.GEN(bf_source,sourcedat)

    with open('temp/out.pen','w') as tempout:
        tempout.write(ws_source)

    return render_template('resp.html',NEWDATA=ws_source,RAWDATA=FORMDATA)



@app.route('/decodeobfsdata',methods=['GET','POST'])
def decodeobfsdata():
    global DECODEDDATA
    if request.method == 'POST':
        # obfsdata=request.values.get('obfsdata')
        obfsdata=request.form.to_dict()
        print(obfsdata)
        obfsdata=obfsdata['obfsdata']
        if obfsdata:
            decoderoutine(obfsdata)
            return render_template('decode.html', DATAFROMAPI=DECODEDDATA)
        else:
            return render_template('decode.html',DATAFROMAPI="ERROR : EMPTY FORM DATA")
    elif request.method == 'GET':
            return render_template('decode.html',DATAFROMAPI="No data decoded, first do POST request")




def decoderoutine(obfsdata):
    global DECODEDDATA
    DATA = obfsdata
    lines = DATA.split(', ')

    with open("data/out.pen", 'w') as srcfile:
        for line in lines:
            srcfile.write(line)
            srcfile.write(',\n')
    try:
        sourcecode = writerscript.load_source("data/out.pen")
    except Exception:
        exit(-1)

    if sourcecode:
        open('temp/data.txt', 'w').close()
        writerscript.evaluate(sourcecode)
        base64endocedStr = ""
        with open('temp/data.txt', 'r') as datafile:
            base64endocedStr = datafile.readline()
        base64endocedStr = base64endocedStr.strip()
        # print(base64endocedStr)
        decodedb64data=base64.b64decode(base64endocedStr).decode()
        # print(decodedb64data)
        DECODEDDATA=decodedb64data

if __name__ == '__main__':
    # Clearing all the file contents for security
    open('temp/data.txt', 'w').close()
    open('data/out.pen', 'w').close()
    open('temp/out.pen', 'w').close()
    app.run("0.0.0.0", 5000)
