from flask import Flask, render_template, request, redirect,jsonify
import functions
import numpy as np
import cv2


app = Flask(__name__)
@app.route('/')
def home():
    return render_template('main.html')

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
if __name__ == "__main__":
    app.run(debug=True, threaded=True)

    