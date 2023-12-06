from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
# from kivy.uix.image import Image

Builder.load_file('float.kv')

class MLayout(Widget):
    pass

class FloatApp(App):
    def build(self):
        Window.clearcolor = (.9,.9,1,1)
        return MLayout()
    
if __name__ == '__main__':
    FloatApp().run()