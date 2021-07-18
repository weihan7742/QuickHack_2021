# Creating the App
import os

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivy.uix.camera import Camera
from sqlite import *
import shutil
import glob


from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.camera import Camera
from opencv_cam import CamApp

# declare screens
class PreLoadScreen(Screen):
    pass

class WelcomeScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class RememberScreen(Screen):
    pass

class RecogniseScreen(Screen):
    pass

class ScreenManager(ScreenManager):
    pass

class CameraClickScreen(Screen):
    def capture(self):
        camera = self.ids['camera']
        camera.export_to_png("image.png")
        self.image = "image.png"
        print("Captured")

    def get_image(self):
        return self.image

# App class
class iKnowU(MDApp):

    dialog = None
    cam_app = CamApp()

    def build(self):
        self.num = 0
        self.image = 0
        buildkv = Builder.load_file("main.kv")
        return buildkv

    def popup_msg(self):
        if not self.dialog:
            self.dialog = MDDialog(text="This person has been saved.",
                                   buttons = [
                                       MDRectangleFlatButton(text="Close", on_press=self.close_popup)])
        self.dialog.open()

    def close_popup(self,obj):
        self.dialog.dismiss()


    def save_image(self, name, relationship):
        path = "image.png"
        if not get_family_id(name, '', '1234'):
            insert_family('1234', "image.png", name, '')
            os.mkdir("images/" + name + "/")
            destination = "images/" + name + '/' + name + "_1" + ".png"
            shutil.move(str(path), destination)
        else:
            list_of_files = glob.glob('/images/' + name + '/*')  # * means all if need specific format then *.csv
            latest_file = max(list_of_files, key=os.path.getctime)
            num = int(latest_file[-1])
            id = get_family_id(name, '', '1234')
            insert_image(id, '1234', "image.png", relationship)
            destination = "images/" + name + '/' + name + '/_' + str(num+1) + ".png"
            shutil.move(str(path), destination)

if __name__ == "__main__":
    iKnowU().run()
