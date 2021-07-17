from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

"""
TODO
1. Move selfie photo to specific directory
2. User can input name
3. Create directory based on user input
4. Integrate camera app with opencv face recognition
"""

class SelfieCameraApp(App):

    def build(self):
        self.camera_obj = Camera()
        self.camera_obj.resolution = (800,800)

        button_obj = Button(text="Click Here")
        button_obj.size_hint = (.5,.2)
        button_obj.pos_hint = {'x':.25, 'y': .25}
        button_obj.bind(on_press=self.take_selfie)

        layout = BoxLayout()
        layout.add_widget(self.camera_obj)
        layout.add_widget(button_obj)
        return layout

    def take_selfie(self,*args):
        print("Take selfie :)")
        self.camera_obj.export_to_png("./selfie.png")

if __name__ == '__main__':
    SelfieCameraApp().run()