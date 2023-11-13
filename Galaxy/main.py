from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.context_instructions import Color

class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)


    V_NB_LINES = 7
    V_L_SPACING = .1
    vertical_Lines = []

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        # print(str(self.width), str(self.height))
        self.init_vertical_lines()
    def on_parent(self, widget, parent):
        pass

    def on_size(self, *args):
        # print(str(self.width), str(self.height))
        # self.perspective_point_x = self.width/2
        # self.perspective_point_y = self.height*0.75
        self.update_vertical_lines()
    def on_perspective_point_x(self, widget, value):
        # print("on_perspective_point_x", str(value))
        pass
    
    def on_perspective_point_y(self, widget, value):
        # print("on_perspective_point_y", str(value))
        pass

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
        offset = -int(self.V_NB_LINES/2)
        for i in range (0, self.V_NB_LINES):
            line_x = int(central_line_x + offset * spacing)
            self.vertical_Lines[i].points = [line_x,0, line_x, self.height]
            offset += 1


class GalaxyApp(App):
    pass

GalaxyApp().run()