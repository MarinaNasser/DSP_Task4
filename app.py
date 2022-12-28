from flask import Flask, render_template, request, redirect,jsonify
import functions
import cv2
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('main.html')

@app.route('/mag2', methods=['POST'] )
def mag2():
    img = cv2.imread('static\\assets\\OIP.jpg',0)
    img_fft,img_magnitude,img_phase = functions.fourier_transform_shift(img)
    path =  functions.plot_magnitude(img_magnitude)



if __name__ == "__main__":
    app.run(debug=True, threaded=True)

    