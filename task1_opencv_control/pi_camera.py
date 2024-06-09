import picamera
import io
import time

pcam = picamera.PiCamera()
class Camera(object):
    def __init__(self):
        #...
        print("Starting pi camera")

    def get_frame(self):
        streaming = io.BytesIO()
        pcam.start_preview()
        time.sleep(0.5)
        pcam.capture(streaming, format='jpeg')
        frame = streaming.getvalue()
        print("Capturing frame from pi camera")
        return frame