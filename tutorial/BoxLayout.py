from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
# from kivy.uix.image import Image

Builder.load_file('Box.kv')

class MayLayout(Widget):
    pass

class BoxApp(App):
    def build(self):
        Window.clearcolor = (.9,.9,1,1)
        return MayLayout()
    
if __name__ == '__main__':
    BoxApp().run()