# Creating the App
import os

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivy.uix.camera import Camera
from QuickHack_2021.sqlite import *


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
        camera.export_to_png("IMG_{}.png")
        print("Captured")

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

<<<<<<< HEAD
    def load_facial(self):
        self.cam_app.run()

    def stop_facial(self):
        self.cam_app.my_camera.stop()
=======
    def capture(self):
        self.num += 1
        camera = self.ids['camera']
        camera.export_to_png("temp_images/IMG_{" + self.num + "}.png")
        self.image = "temp_images/IMG_{" + self.num + "}.png"
        print("Captured")

    def save_image(self):
        if not get_family_id('d', 'n', '1234'):
            insert_family('1234', self.image, '')
        else:
            id = get_family_id('1234')
            insert_image(id, '1234', self.image, )

        os.remove(self.image)
>>>>>>> d9668b2e94867d3a11ed54f0622459e842e0f702

if __name__ == "__main__":
    iKnowU().run()
