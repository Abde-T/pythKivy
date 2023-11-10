from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(0,10):
            b = Button(text = str(i+1), size_hint=(None,None), size=(dp(100), dp(100)))
            self.add_widget(b)



class GridLayoutExample(GridLayout):
    pass


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.orientation = "vertical"
    #     b1 = Button(text = "A")
    #     b2 = Button(text = "B")
    #     b3 = Button(text = "C")

    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


# TheLabApp().run()

class WidgetsExample(GridLayout):
    my_text = StringProperty('1')
    text_input_str = StringProperty('fuck')
    # slider_value_txt = StringProperty('50')
    count = 1
    count_enabled = BooleanProperty(False)
    def on_button_click(self):
        if self.count_enabled:
            self.count += 1
            self.my_text = str(self.count)

    def on_toggle_button_state(self, widget):
        print("toggle state" + widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            widget.background_color = [2,0,0]
            self.count_enabled = False
        else:
            widget.text = 'ON'
            widget.background_color = [0,1,0]
            self.count_enabled = True
    
    def on_switch_active(self, widget):
        print("toggle state" + str(widget.active))
        # print(str(widget.active)) 
        
    
    def on_slider_value(self, widget):
        self.slider_value_txt = str(int(widget.value))


    def on_text_validate(self, widget):
        self.text_input_str = widget.text


class WidgetsApp(App):
    pass


WidgetsApp().run()