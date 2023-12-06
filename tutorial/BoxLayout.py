from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
# from kivy.uix.image import Image

Builder.load_file('Box.kv')

class MayLayout(Widget):
    def submit(self):
        #create var for widget
        name = self.ids.name_input.text
        #update the label
        self.ids.name_label.text = f'Hello {name}'
        #clear input box
        self.ids.name_input.text = ""

class BoxApp(App):
    def build(self):
        Window.clearcolor = (.9,.9,1,1)
        return MayLayout()
    
if __name__ == '__main__':
    BoxApp().run()