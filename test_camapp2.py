#%%
from kivymd.app import MDApp
from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.screen import Screen
from kivy.uix.button import Button
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import os
import cv2
"""
TODO
1. Move selfie photo to specific directory - DONE
2. User can input name - Done
3. Create directory based on user input
4. Integrate camera app with opencv face recognition
"""

class SelfieCameraApp(MDApp):

    def build(self):
        # Initialize camera object
        self.camera_obj = Camera()
        self.camera_obj.resolution = (800,800)

        # Button which triggers the "take photo" function
        button_obj = MDRectangleFlatButton(text="Camera",pos_hint={'center_x': 0.5, 'center_y': 0.5})
        button_obj.bind(on_press=self.take_selfie)

        # Input box to retrieve name
        self.description = MDTextField(text="Enter name",pos_hint={'center_x':0.5,'center_y':0.8},size_hint_x=None,width=300,on_release=self.take_selfie)

        # Box Layout
        layout = Screen()
        layout.add_widget(self.camera_obj)
        layout.add_widget(button_obj)
        layout.add_widget(self.description)
        return layout

    def take_selfie(self,*args):
        """
        If database doesn't work:
            # Create a directory if not yet exist
            # Get the #number of files in the directory + 1
            # Append number to self.description + ".png"
            # Export to png
            # Move picture to the directory 
        """
        pic_name = self.description.text+".png"
        self.camera_obj.export_to_png(pic_name)
        self.move_dir(pic_name)
    
    def move_dir(self,pic_name):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        test_dir = os.path.join(BASE_DIR, r"images\test")

        og_pic_dir = os.path.join(BASE_DIR,pic_name)
        new_pic_dir = os.path.join(test_dir,pic_name)
        os.rename(og_pic_dir, new_pic_dir)

class KivyCamera(Image):
    def __init__(self, capture, fps, **kwargs):
        super(KivyCamera, self).__init__(**kwargs)
        self.capture = capture
        Clock.schedule_interval(self.update, 1.0 / fps)

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            # convert it to texture
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tobytes()
            image_texture = Texture.create(
                size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            # display image from the texture
            self.texture = image_texture
class CamApp(App):
    def build(self):
        self.capture = cv2.VideoCapture(0)
        self.my_camera = KivyCamera(capture=self.capture, fps=30)
        return self.my_camera

    def on_stop(self):
        #without this, app will not exit even if the window is closed
        self.capture.release()

if __name__ == '__main__':
    # SelfieCameraApp().run()
    CamApp().run()
# %%
