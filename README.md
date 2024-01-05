This code was originally forked from https://github.com/EbenKouao/pi-camera-stream-flask.git under MIT licence
The original code was stripped down to work on a Raspberry Pi Zero W, all video elements were removed

# A flask app to serve Pi camera images
The Pi streams the output of the camera module over the web via Flask. Devices connected to the same network would be able to access the service via

```
<raspberry_pi_ip:5000>
```

## Library dependencies

```
sudo pip3 install flask
sudo pip3 install picamera2

```
## Launch web service
```python main.py```

## Load image through browser

Point the browser to 
```
<raspberry_pi_ip:5000>
```
This should show the latest available image

Additional routes to generate new images: 
```
<raspberry_pi_ip:5000/picture>    - take a picture using the current configuration and show it
<raspberry_pi_ip:5000/getpicture> - take a picture and send it as jpeg stream
<raspberry_pi_ip:5000/getlow>     - configure the camera to low resolution [1202x648], take a picture and send it as jpeg stream
<raspberry_pi_ip:5000/getmedium>  - configure the camera to medium resolution [2404x1296], take a picture and send it as jpeg stream
<raspberry_pi_ip:5000/getfull>    - configure the camera to full resolution [4608x2592], take a picture and send it as jpeg stream
```

The initial camera configuration is the full resolution. Horizontal and Vertical flipping can be set in main.py 





