from flask import Flask,request,jsonify
from flask import render_template

import writerscript as ws
import base64

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
    return render_template('resp.html',DATA=FORMDATA)


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
