from flask import Flask, render_template, request, redirect,jsonify
import os

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('main.html')

@app.route('/image1')
def save():
    file = request.files['ImageFile']
    audio=file.save(os.path.join('static/assets/image1.jpg'))
    path='static/assets/records/recorded_Sound.wav'

if __name__ == "__main__":
    app.run(debug=True, threaded=True)

    