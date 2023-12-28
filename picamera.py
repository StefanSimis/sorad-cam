from picamera2 import Picamera2, libcamera

class Picamera(object):
    def __init__(self, hflip=0, vflip=1, res='full'):
        self.pc = Picamera2()
        self.configure(hflip=hflip, vflip=vflip, res=res)
        self.pc.start()


    def __del__(self):
        self.pc.stop()

    def configure(self, hflip=0, vflip=1, res='full'):
        self.pc.stop()
        if res == 'full':
            imres = (4608, 2592)
        elif res == 'medium':
            imres = (2404, 1296)
        elif res == 'low':
            imres = (1202, 648)
        else:
            imres = (4608, 2592)

        camera_config = self.pc.create_still_configuration(main={"size": imres},
                                                           transform=libcamera.Transform(vflip=vflip, hflip=hflip))
        self.pc.configure(camera_config)
        self.pc.start()

    def take_picture(self):
        af_result = self.pc.autofocus_cycle()
        self.pc.capture_file('static/latest-image.jpg')
