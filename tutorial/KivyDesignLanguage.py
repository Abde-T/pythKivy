from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('h.kv')

class MyGridLayout(Widget):
    name = ObjectProperty(None)
    lastname = ObjectProperty(None)
    wish = ObjectProperty(None)


    def press(self):
        name = self.name.text
        lastname = self.lastname.text
        wish =  self.wish.text
        #print it to screen
        print(f"{name}, {lastname}, Wishes to be, {wish}")
        #self.add_widget(Label(text=f"{name}, {lastname}, Wishes to be, {wish}"))
        #clear input box
        self.name.text = ''
        self.lastname.text = ''
        self.wish.text = ''

class DesignLanguageApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == '__main__':
    DesignLanguageApp().run()