from flask import Flask, render_template, request, redirect,jsonify,session,url_for
import functions
from functions import Image
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

# @app.route('/switch',methods=['POST'])
# def switch():
#     if request.method == 'POST' and 'checked' in request.values:
#         checked = (request.values['checked']) == 'true'
#         if checked:
#             images[1].toggleInOrOut()
#         # inOrOutSender = int(request.form['inOrOutSender'])
#         # images[inOrOutSender].toggleInOrOut()
#         print(request.values)
#         print('-'*150)
#         magIdx = Image.takenMag
#         if magIdx == 1:
#             phaseIdx = 2
#         else:
#             phaseIdx = 1
#         newFourierToMag = images[magIdx].getMasked(x1,y1,w1,h1,not images[1].takenInOrOut,1)
#         newFourierToPhase = images[phaseIdx].getMasked(x2,y2,w2,h2,not images[1].takenInOrOut,0)
#         newImgPath = Image.mixMagAndPhase(newFourierToMag,newFourierToPhase)
#         images[3] = Image(newImgPath)
#         print(newImgPath)
#         return json.dumps({0: f' <img src="{newImgPath}">'
#         })
#         return render_template('main.html',images = images)
    
#     if request.method == 'POST' and 'sender' in request.form:
#         sender = int(request.form['sender'])
#         if sender in [11,22]:
#             Image.takenMag = 1
#         else:
#             Image.takenMag = 2
#         return render_template('main.html',images = images)

@app.route('/upload',methods=['GET','POST'])
def uploadPhoto():
    if request.method == 'POST':
        sender = int(request.form['sender'])
        name = request.form['img'+f'{sender}']
        picPath = os.path.join(app.config['UPLOAD_FOLDER'],name)          
        print('-'*54)
        print(picPath)
        images[sender] = Image(picPath)
        Image.takenMag = sender
        # magPath = images[sender].getPathOfMagOrPhasePlot(1)
        # return json.dumps({0: f' {magPath}'  })
        # print(images[1].spatialDomainPath)
        return render_template('main.html',images = images)

@app.route('/switch',methods=['GET','POST'])
def getMag():
    if request.method == 'POST': 
        sender = int(float(request.values['sender']))      
        print('-'*54)
        if sender == 11 or sender == 22:
            sender = 1
        else:
            sender = 2
        Image.takenMag = sender
        magPath = images[sender].getPathOfMagOrPhasePlot(1)
        if sender == 1:
            other = 2
        else:
            other = 1
        phasePath = images[other].getPathOfMagOrPhasePlot(0)
        return json.dumps({0: f' ../static/assets/{magPath}',1:f' ../static/assets/{phasePath}',2:f'<h2>Magnitude</h2>',3:f'<h2>Phase</h2>' })

@app.route('/getC',methods=['POST'])
def switch():
    if request.method == 'POST':
        if 'checked1' in request.values:
            checked = request.values['checked1'] == 'true'
            images[1].takenInOrOut = not checked
        elif 'checked2' in request.values:
            checked = request.values['checked2'] == 'true'
            images[2].takenInOrOut = not checked
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
    print(magIdx)
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

    