#%%
from kivymd.app import MDApp
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.screen import Screen
from kivy.uix.button import Button
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton
import os
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

if __name__ == '__main__':
    SelfieCameraApp().run()
# %%
