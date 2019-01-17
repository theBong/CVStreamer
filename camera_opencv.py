import cv2
from base_camera import BaseCamera
import numpy as np

face_cascade = cv2.CascadeClassifier('/home/paul/Desktop/Work/UI/Site/haarcascade_frontalcatface.xml')

class Camera(BaseCamera):
    status = None
    video_source = 0
    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def getstat(a):
        Camera.status = a

    @staticmethod
    def frames():
        
        camera = cv2.VideoCapture(Camera.video_source)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, frame = camera.read()
            # frame = cv2.resize(frame, (704, 396))
            if Camera.status == 1:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                print("THIS LINE IS RUN")
            
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                if len(faces) > 0:
                    print("SUPS")
                for (x,y,w,h) in faces:
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

            

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', frame)[1].tobytes()

