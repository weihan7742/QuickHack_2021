#%%
from kivymd.app import MDApp
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.screen import Screen
from kivy.uix.button import Button
from kivymd.uix.textfield import MDTextField
import os

"""
TODO
1. Move selfie photo to specific directory - DONE
2. User can input name 
3. Create directory based on user input
4. Integrate camera app with opencv face recognition
"""

class SelfieCameraApp(MDApp):

    def build(self):
        # Initialize camera object
        self.camera_obj = Camera()
        self.camera_obj.resolution = (800,800)

        # Button which triggers the "take photo" function
        button_obj = Button(text="Click Here")
        button_obj.size_hint = (0.5,0.2)
        button_obj.pos_hint = {'x':.25, 'y': .25}
        button_obj.bind(on_press=self.take_selfie)

        # Box Layout
        layout = Screen()
        layout.add_widget(self.camera_obj)
        layout.add_widget(button_obj)
        # layout.add_widget(self.some_name)
        return layout

    def take_selfie(self,*args):
        pic_name = "./selfie.png"
        self.camera_obj.export_to_png(pic_name)
        self.move_dir(pic_name)
    
    def move_dir(self,pic_name):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        test_dir = os.path.join(BASE_DIR, r"images\test")

        og_pic_dir = os.path.join(BASE_DIR,pic_name)
        new_pic_dir = os.path.join(test_dir,pic_name)
        os.rename(og_pic_dir, new_pic_dir)

if __name__ == '__main__':
    SelfieCameraApp().run()
# %%
