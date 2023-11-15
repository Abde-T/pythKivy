from kivy.config import Config
Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '400')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, Clock
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.context_instructions import Color
from kivy.core.window import Window
from kivy import platform

class MainWidget(Widget):
    from transforms import transform, transform_2D, transform_perspective
    from userActions import on_keyboard_up, on_keyboard_down, on_touch_up, on_touch_down, keyboard_closed

    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    V_NB_LINES = 10
    V_L_SPACING = .25
    vertical_Lines = []

    H_NB_LINES = 15
    H_L_SPACING = .1
    horizontal_Lines = []

    SPEED = 4
    current_offset_y = 0

    SPEED_X = 12 
    current_offset_x = 0
    current_speed_x = 0

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        # print(str(self.width), str(self.height))
        self.init_vertical_lines()
        self.init_horizontal_lines()

        if self.is_desktop():
            self.keyboard = Window.request_keyboard(self.keyboard_closed, self)
            self.keyboard.bind(on_key_down=self.on_keyboard_down)
            self.keyboard.bind(on_key_up=self.on_keyboard_up)

        Clock.schedule_interval(self.update, 1.0 / 60.0)


    def is_desktop(self):
        if platform in ('linux', 'win', 'macosx'):
            return True
        return False

    # def on_parent(self, widget, parent):
    #     pass

    # def on_size(self, *args):
    #     # print(str(self.width), str(self.height))
    #     # self.perspective_point_x = self.width/2
    #     # self.perspective_point_y = self.height*0.75
    #     # self.update_vertical_lines()
    #     # self.update_horizontal_lines()
    #     pass


    # def on_perspective_point_x(self, widget, value):
    #     # print("on_perspective_point_x", str(value))
    #     pass
    
    # def on_perspective_point_y(self, widget, value):
    #     # print("on_perspective_point_y", str(value))
    #     pass

    def init_vertical_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            # self.line = Line(points=[100, 0, 100, 100 ])  
            for i in range (0, self.V_NB_LINES):
                self.vertical_Lines.append(Line())

    def update_vertical_lines(self):
        central_line_x = int(self.width/2)
        #self.line.points = [ center_x,0 , center_x, 100]
        spacing = self.V_L_SPACING * self.width
        offset = -int(self.V_NB_LINES/2)+0.5
        for i in range (0, self.V_NB_LINES):
            line_x = central_line_x + offset * spacing +self.current_offset_x

            x1,y1= self.transform(line_x, 0)
            x2,y2= self.transform(line_x, self.height)
            self.vertical_Lines[i].points = [x1,y1, x2, y2]
            offset += 1


    def init_horizontal_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            # self.line = Line(points=[100, 0, 100, 100 ])  
            for i in range (0, self.H_NB_LINES):
                self.horizontal_Lines.append(Line())


    def update_horizontal_lines(self):
        central_line_x = int(self.width/2)
        spacing = self.V_L_SPACING * self.width
        offset = -int(self.V_NB_LINES/2)+0.5

        x_min = central_line_x + offset * spacing + self.current_offset_x
        x_max = central_line_x - offset * spacing + self.current_offset_x
        spacing_y = self.H_L_SPACING * self.height

        for i in range (0, self.H_NB_LINES):
            line_y = i * spacing_y - self.current_offset_y
            x1,y1= self.transform(x_min, line_y)
            x2,y2= self.transform(x_max, line_y)
            self.horizontal_Lines[i].points = [x1,y1, x2, y2]


    def update(self, dt):
        time_factor = dt*60
        self.update_vertical_lines()
        self.update_horizontal_lines()
        self.current_offset_y += self.SPEED * time_factor

        spacing_y = self.H_L_SPACING * self.height
        if self.current_offset_y >= spacing_y:
            self.current_offset_y -= spacing_y

        self.current_offset_x += self.current_speed_x * time_factor


class GalaxyApp(App):
    pass

GalaxyApp().run()

