from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen 

kv = Builder.load_file('iknow.kv')

class WelcomeScreen(Screen):
    pass

class IdentifyPersonScreen(Screen):
    pass

class SelfDescriptionScreen(Screen):
    pass

class LabelPhotosScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class IKnowApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    IKnowApp().run()