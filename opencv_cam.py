from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2
import pickle
import os
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screen import Screen
import time
from kivy.lang import Builder

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

labels = {}

with open("labels.pkl", 'rb') as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()} # Reverse key and value

class KivyCamera(Image):
    def __init__(self, capture, fps, **kwargs):
        super(KivyCamera, self).__init__(**kwargs)
        self.capture = capture
        self.event = Clock.schedule_interval(self.update, 1.0 / fps)
        
    def update(self, dt):

        if cv2.waitKey(20) & 0xFF == ord('q'):
            self.capture.release()
            cv2.destroyAllWindows()
            
        ret, frame = self.capture.read()
        if ret:
            faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_alt2.xml')
            frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # added
            faces = faceCascade.detectMultiScale(frameGray, 1.1, 4)  # added

            for (x, y, w, h) in faces:  # added
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # added
                
                end_cord_x = x+w
                end_cord_y = y+h
                roi_gray = frameGray[y:end_cord_y, x:end_cord_x]  # Region of interest for gray (y_start-y_end)
                roi_color = frame[y:end_cord_y, x:end_cord_x] # Region of interest for color
                
                # Recognize people using deep learning model
                id, conf = recognizer.predict(roi_gray) # Only gray
                if conf>=45:
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    name = labels[id]
                    color = (255,255,255)
                    stroke = 2
                    cv2.putText(frame,name,(x,y),font,1,color,stroke,cv2.LINE_AA)

            # convert it to texture
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tostring()
            image_texture = Texture.create(
                size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            # display image from the texture
            self.texture = image_texture

class CamApp(MDApp):
    def build(self):
        self.capture = cv2.VideoCapture(0)
        self.my_camera = KivyCamera(capture=self.capture, fps=30)
        
        return self.my_camera

    def on_stop(self):
        #without this, app will not exit even if the window is closed
        self.capture.release()

if __name__ == '__main__':
    CamApp().run()