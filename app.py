from flask import Flask,request,jsonify
from flask import render_template

from writerscript import generator
import base64
from modules.brainfuckgenerator import BFGenerator

app: Flask = Flask(__name__)
SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'

global FORMDATA
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
    FORMDATA={'name': 'Saket Upadhyay', 'cardno': '3714 496353 98431', 'expdate': '08/78', 'cvv': '345'}
    datmod=str(FORMDATA)
    data_bytes=datmod.encode('ascii')
    base64data=base64.b64encode(data_bytes)
    base64text=base64data.decode('ascii')
    bfg=BFGenerator()
    bf_source=bfg.text_to_brainfuck(base64text)


    with open('data/source.txt','r') as src:
        sourcedat=list(src)[0].strip('\n')

    ws_source=generator.GEN(bf_source,sourcedat)

    with open('temp/out.pen','w') as tempout:
        tempout.write(ws_source)

    return render_template('resp.html',NEWDATA=ws_source,RAWDATA=FORMDATA)


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
