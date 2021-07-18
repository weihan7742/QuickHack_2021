# Creating a Login Page

# Creating the App

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


# declare screens
class WelcomeScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass



class iKnowU(MDApp):

    def build(self):
        buildkv = Builder.load_file("main.kv")
        return buildkv

if __name__ == "__main__":
    iKnowU().run()
