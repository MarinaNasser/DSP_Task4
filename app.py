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
    img = cv2.imread('static\\assets\\OIP.jpg',0)
    img_fft,img_magnitude,img_phase = functions.fourier_transform_shift(img)
    path =  functions.plot_magnitude(img_magnitude)


    return render_template('main.html');

@app.route("/phase1/", methods=['POST'])
def phase1():
    print("phase1")
    return render_template('main.html');

@app.route("/mag2/", methods=['POST'])
def magnutude2():
    print("mag2")
    return render_template('main.html');

@app.route("/phase2/", methods=['POST'])
def phase2():
    print("phase2")
    return render_template('main.html');

if __name__ == "__main__":
    app.run(debug=True, threaded=True)

    