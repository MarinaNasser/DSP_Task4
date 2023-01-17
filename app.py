from flask import Flask, render_template, request, redirect,jsonify,session,url_for
import functions
from functions import Image
import numpy as np
import cv2
import os
import json


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
picFolder = os.path.join('static','assets')
app.config['UPLOAD_FOLDER'] = picFolder

images = [0,Image('static/assets/img8.jpg'),Image('static/assets/img8.jpg'),Image('static/assets/result8109.jpg')]

@app.route('/')
def home():
    return render_template('main.html',images = images)

@app.route('/switch',methods=['POST'])
def switch():
    if request.method == 'POST' and 'inOrOutSender' in request.form:
        inOrOutSender = int(request.form['inOrOutSender'])
        images[inOrOutSender].toggleInOrOut()
        return render_template('main.html',images = images)
    
    if request.method == 'POST' and 'sender' in request.form:
        sender = int(request.form['sender'])
        if sender in [11,22]:
            Image.takenMag = 1
        else:
            Image.takenMag = 2
        return render_template('main.html',images = images)

@app.route('/',methods=['GET','POST'])
def uploadPhoto():
    if request.method == 'POST':
        sender = int(request.form['sender'])
        name = request.form['img'+f'{sender}']
        picPath = os.path.join(app.config['UPLOAD_FOLDER'],name)          
        print('-'*54)
        print(picPath)
        images[sender] = Image(picPath)
        Image.takenMag = sender
        magPath = images[sender].getPathOfMagOrPhasePlot(1)
        return json.dumps({0: f' <img src="{magPath}">'})
        # print(images[1].spatialDomainPath)
        return render_template('main.html',images = images)

@app.route('/getC',methods=['POST'])
def getC():
    
    x1 = int(float(request.values['x1']))
    y1 = int(float(request.values['y1']))
    w1 = int(float(request.values['w1']))
    h1 = int(float(request.values['h1']))
    x2 = int(float(request.values['x2']))
    y2 = int(float(request.values['y2']))
    w2 = int(float(request.values['w2']))
    h2 = int(float(request.values['h2']))
    print(request.values)
    print('-'*150)
    magIdx = Image.takenMag
    if magIdx == 1:
        phaseIdx = 2
    else:
        phaseIdx = 1
    newFourierToMag = images[magIdx].getMasked(x1,y1,w1,h1,not images[1].takenInOrOut,1)
    newFourierToPhase = images[phaseIdx].getMasked(x2,y2,w2,h2,not images[1].takenInOrOut,0)
    newImgPath = Image.mixMagAndPhase(newFourierToMag,newFourierToPhase)
    images[3] = Image(newImgPath)
    print(newImgPath)
    return json.dumps({0: f' <img src="{newImgPath}">'
     })
    # return '0'
    # return redirect(url_for('home', images=images))
    return render_template('main.html',images = images)
if __name__ == "__main__":
    app.run(debug=True)

    