from flask import Flask, render_template, request, redirect,jsonify
import functions
import numpy as np
import cv2
import os

app = Flask(__name__)

picFolder = os.path.join('static','assets')
app.config['UPLOAD_FOLDER'] = picFolder


@app.route('/')
def home():
    # pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'OIP.jpg')
    return render_template('main.html',path = 0)

@app.route("/mag1/", methods=['POST'])
def magnitude1():
    img1 = cv2.imread('static\\assets\\OIP.jpg',0) # da ely m7tagen ngebo mn el style.js
    img_fft1,img_magnitude1,img_phase1 = functions.fourier_transform_shift(img1)
    path =  functions.plot_magnitude(img_magnitude1)
    return render_template('main.html');

@app.route("/phase1/", methods=['POST'])
def phase1():
    img1 = cv2.imread('static\\assets\\OIP.jpg',0) # da ely m7tagen ngebo mn el style.js
    img_fft1,img_magnitude1,img_phase1 = functions.fourier_transform_shift(img1)
    path =  functions.plot_phase(img_phase1)
    return render_template('main.html');

@app.route("/mag2/", methods=['POST'])
def magnutude2():
    img2 = cv2.imread('static\\assets\\santa.jpg',0) # da ely m7tagen ngebo mn el style.js
    img_fft2,img_magnitude2,img_phase2= functions.fourier_transform_shift(img2)
    path =  functions.plot_magnitude(img_magnitude2)
    return render_template('main.html');
   

@app.route("/phase2/", methods=['POST'])
def phase2():
    img2 = cv2.imread('static\\assets\\santa.jpg',0) # da ely m7tagen ngebo mn el style.js
    img_fft2,img_magnitude2,img_phase2= functions.fourier_transform_shift(img2)
    path =  functions.plot_phase(img_phase2)
    return render_template('main.html');


@app.route('/',methods=['POST'])
def uploadPhoto():
    if request.method == 'POST':
          
        print('reached upload photo---------------------------------')
        name = request.form['img']
        pic1 = os.path.join(app.config['UPLOAD_FOLDER'],name)  
        print(pic1)
        img2 = cv2.imread(pic1,0)
        _,mag,_ = functions.fourier_transform_shift(img2)
        # pathOfMag = os.path.join(app.config['UPLOAD_FOLDER'],'mag.jpg')
        # cv2.imwrite(pathOfMag,mag)
        pathOfMag = functions.plot_magnitude(mag)
        
        return render_template('main.html',path = pic1,pathOfMag = pathOfMag)
    
if __name__ == "__main__":
    app.run(debug=True, threaded=True)

    