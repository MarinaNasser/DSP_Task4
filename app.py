from flask import Flask, render_template, request, redirect,jsonify,session
import functions
from functions import Image
import numpy as np
import cv2
import os

app = Flask(__name__)

picFolder = os.path.join('static','assets')
app.config['UPLOAD_FOLDER'] = picFolder

images = [0,0,0,0]

@app.route('/')
def home():
    return render_template('main.html',images = images)

@app.route('/switch',methods=['POST'])
def switch():
    if request.method == 'POST':
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
        images[sender] = Image(picPath)
        
        return render_template('main.html',images = images)

@app.route('/getC',methods=['POST'])
def getC():
    
    x = int(request.values['x'])
    print('-'*54)
    print(x)
    return "0"
if __name__ == "__main__":
    app.run(debug=True)

    