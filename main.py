#Modified by smartbuilds.io
#Date: 27.09.20
#Desc: This web application serves a motion JPEG stream
# main.py
# import the necessary packages
from flask import Flask, render_template, Response, request, send_from_directory, redirect, url_for
from picamera import Picamera

camera = Picamera()

# App Globals (do not edit)
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/picture')
def take_picture():
    camera.take_picture()
    return redirect(url_for('index'))

@app.route('/getpicture')
def get_picture():
    camera.take_picture()
    return send_from_directory(directory='static', filename='latest-image.jpg')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
