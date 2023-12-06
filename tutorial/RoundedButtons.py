from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('Rounded.kv')

class MyLayout(Widget):
    pass

class ButtonApp(App):
    def build(self):
        Window.clearcolor = (.9,.9,.7,1)
        return MyLayout()
    
if __name__ == '__main__':
    ButtonApp().run()