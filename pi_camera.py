import datetime
import time
import picamera

'''
TODO
REQUIRES Raspbian Buster OS or a work around to work with the legacy picamera library
Capture picture at a interval
Update the picture at intervals

Send data to sensehat raspberry
    - Python has a inbuilt system call library, 
        which you can use to SCP or ssh files to another device
'''


with picamera.PiCamera() as camera:
    try:
        while True:
            camera.resolution = (1024, 768)
            time.sleep(2)
            camera.capture('foo.jpg')
            time.sleep(2)
            camera.capture('foo2.jpg')
    except KeyboardInterrupt:
        pass
        
