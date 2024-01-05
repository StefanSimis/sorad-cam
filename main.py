from flask import Flask, render_template, Response, request, send_from_directory, redirect, url_for
from picamera import Picamera
import os
import datetime

try:
    camera = Picamera(hflip=0, vflip=1, res='full')

    app = Flask(__name__)


    @app.route('/')
    @app.route('/index')
    def index():
        try:
            size = os.path.getsize('static/latest-image.jpg')
            size = size/1024.
            mtime = os.path.getmtime('static/latest-image.jpg')
            mtime = datetime.datetime.fromtimestamp(mtime)
        except Exception as msg:
            size = 'no image found'
            mtime = 'no image found'
            print(msg)
            print(os.listdir('.'))
        return render_template('index.html', size=size, mtime=mtime)

    @app.route('/getpicture')
    def get_picture():
        # take picutre and send jpg with current configuration
        camera.take_picture()
        return send_from_directory(directory='static', filename='latest-image.jpg')

    @app.route('/getfull')
    def get_picture_full():
        # configure as full res, take picture and send as jpeg
        camera.configure(hflip=0, vflip=1, res='full')
        camera.take_picture()
        return send_from_directory(directory='static', filename='latest-image.jpg')

    @app.route('/getlow')
    def get_picture_low():
        # configure as full res, take picture and send as jpeg
        camera.configure(hflip=0, vflip=1, res='low')
        camera.take_picture()
        return send_from_directory(directory='static', filename='latest-image.jpg')

    @app.route('/getmedium')
    def get_picture_medium():
        # configure as full res, take picture and send as jpeg
        camera.configure(hflip=0, vflip=1, res='medium')
        camera.take_picture()
        return send_from_directory(directory='static', filename='latest-image.jpg')

except RuntimeError:
    raise
except KeyboardInterrupt:
    camera.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
