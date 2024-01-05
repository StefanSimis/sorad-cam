from flask import Flask, render_template, Response, request, send_from_directory, redirect, url_for
from picamera import Picamera

camera = Picamera(hflip=0, vflip=1, res='full')
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/picture')
def take_picture():
    # take picture with current configuration
    camera.take_picture()
    return redirect(url_for('index'))

@app.route('/getpicture')
def get_picture():
    # take picutre and send jpg with current configuration
    camera.take_picture()
    return send_from_directory(directory='static', filename='latest-image.jpg')

@app.route('/full')
def take_picture_full():
    # configure as full res and take picture
    camera.configure(hflip=0, vflip=1, res='full')
    camera.take_picture()
    return redirect(url_for('index'))

@app.route('/getfull')
def get_picture_full():
    # configure as full res, take picture and send as jpeg
    camera.configure(hflip=0, vflip=1, res='full')
    camera.take_picture()
    return send_from_directory(directory='static', filename='latest-image.jpg')

@app.route('/low')
def take_picture_low():
    # configure as full res and take picture
    camera.configure(hflip=0, vflip=1, res='low')
    camera.take_picture()
    return redirect(url_for('index'))

@app.route('/getlow')
def get_picture_low():
    # configure as full res, take picture and send as jpeg
    camera.configure(hflip=0, vflip=1, res='low')
    camera.take_picture()
    return send_from_directory(directory='static', filename='latest-image.jpg')

@app.route('/medium')
def take_picture_medium():
    # configure as full res and take picture
    camera.configure(hflip=0, vflip=1, res='medium')
    camera.take_picture()
    return redirect(url_for('index'))

@app.route('/getmedium')
def get_picture_medium():
    # configure as full res, take picture and send as jpeg
    camera.configure(hflip=0, vflip=1, res='medium')
    camera.take_picture()
    return send_from_directory(directory='static', filename='latest-image.jpg')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
