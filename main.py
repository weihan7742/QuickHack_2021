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
from train_faces import Train

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
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        path_dir = os.path.join(BASE_DIR,path)
        image_dir = os.path.join(BASE_DIR, "images",name)


        if not os.path.exists(image_dir):
            # insert_family('1234', "image.png", name, '')
            os.mkdir("images/" + name + "/")
            destination = "images/" + name + '/' + name + "_1" + ".png"
            shutil.move(str(path), destination)
        else:
            # Get the number of files in the directory 
            root, dirs, files = next(os.walk(image_dir))
            num = len(files)
            # id = get_family_id(name, '', '1234')
            # insert_image(id, '1234', "image.png", relationship)
            insert_image = os.path.join(BASE_DIR,"images",name,name+"_"+str(num+1)+".png")
            os.rename(path_dir,insert_image)

    def run_facial(self):
        CamApp().run()


    def training(self):
        Train().training()

if __name__ == "__main__":
    iKnowU().run()
