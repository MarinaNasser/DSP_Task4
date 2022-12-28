from flask import Flask, render_template, request, redirect,jsonify
import functions
import numpy as np


app = Flask(__name__)
@app.route('/')
def home():
    return render_template('main.html')


@app.route("/mag1/", methods=['POST'])
def magnitude1():
    #Moving forward code
    forward_message = "Moving Forward..."
    print("mag1")
    return render_template('main.html', forward_message=forward_message);

@app.route("/phase1/", methods=['POST'])
def phase1():
    #Moving forward code
    forward_message = "Moving Forward..."
    print("phase1")
    return render_template('main.html', forward_message=forward_message);

@app.route("/mag2/", methods=['POST'])
def magnutude2():
    #Moving forward code
    forward_message = "Moving Forward..."
    print("mag2")
    return render_template('main.html', forward_message=forward_message);

@app.route("/phase2/", methods=['POST'])
def phase2():
    #Moving forward code
    forward_message = "Moving Forward..."
    print("phase2")
    return render_template('main.html', forward_message=forward_message);

if __name__ == "__main__":
    app.run(debug=True, threaded=True)

    