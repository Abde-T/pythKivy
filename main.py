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
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color
from kivy.properties import Clock


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

# WidgetsApp().run()


class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample3(Widget):
    pass

class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(3)
        self.vy = dp(4)
        with self.canvas:
            Line(points=(100,100, 400,500), width=2)
            Color(0,1,0)
            Line(circle=(400,200, 50), width=2)
            Line(rectangle=(400,400, 50,50), width=2)
            self.rect = Rectangle(pos=(500,200), size=(150,100))
            self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))
        Clock.schedule_interval(self.update, 1/60)


    def on_button_click(self):
        x,y = self.rect.pos
        w,h = self.rect.size
        inc = dp(10)

        diff = self.width - (x+w)
        if diff<inc:
            inc = diff

        x += inc
        self.rect.pos = (x, y)

    def on_size(self, *args):
        self.ball.pos = (self.center_x-  self.ball_size/2, self.center_y - self.ball_size/2)

    def update(self, dt):
        x,y = self.ball.pos
        w,h = self.ball.size
 
        x+=self.vx
        y+=self.vy

        if y + self.ball_size>self.height:
            y=self.height-self.ball_size
            self.vy = -self.vy
        if x + self.ball_size>self.width:
            x=self.width-self.ball_size
            self.vx = -self.vx
        if y<0:
            y=0
            self.vy = -self.vy
        if x <0:
            x=0
            self.vx = -self.vx

        self.ball.pos = (x, y)


class CanvasApp(App):
    pass

# CanvasApp().run()

class CanvasExample4App(App):
    pass

# CanvasExample4App().run()



class CanvasExample6(Widget):
    pass

class CanvasExample6App(App):
    pass

CanvasExample6App().run()