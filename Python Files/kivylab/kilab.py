from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class Stack_y(StackLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(0, 10):
            butt = Button(text=str(i + 1), size_hint=(.2, .5))
            self.add_widget(butt)


class theApp(App):
    pass


class PongWidget(Widget):
    pass


theApp().run()
