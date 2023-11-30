import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    # initialize infinite keywords
    def __init__(self, **kwargs):
        #call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        #set columns
        self.cols = 1
        self.row_force_default = True
        self.row_default_height = 120
        self.col_force_default = True
        self.col_default_width = 100

        #create second grid
        self.top_grid = GridLayout(row_force_default = True, #forcing the hight and width
                                   row_default_height = 40,
                                   col_force_default = True,
                                   col_default_width = 100)
        self.top_grid.cols = 2


        #add top grid to the app
        self.add_widget(self.top_grid)

        #add widgets
        self.top_grid.add_widget(Label(text='Name: '))
        #add input box
        self.name = TextInput(multiline = False) 
        self.top_grid.add_widget(self.name)

        self.top_grid.add_widget(Label(text='last Name: '))
        #add input box
        self.last_name = TextInput(multiline = False ) 
        self.top_grid.add_widget(self.last_name)

        self.top_grid.add_widget(Label(text='last wish: '))
        #add input box
        self.wish = TextInput(multiline = False ) 
        self.top_grid.add_widget(self.wish)

        #create submit button
        self.submit = Button(text="Submit",
            font_size = 32,
            size_hint_y = None,
            height = 50,
            size_hint_x = None,
            width = 200,
            )
        #bind button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        last_name = self.last_name.text
        wish =  self.wish.text
        #print it to screen
        self.add_widget(Label(text=f"{name}, {last_name}, Wishes to be, {wish}"))
        #clear input box
        self.name.text = ''
        self.last_name.text = ''
        self.wish.text = ''

class MyApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == '__main__':
    MyApp().run()