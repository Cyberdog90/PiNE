# PiNE Ver. 1.0

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class Main(App):
    def build(self):
        self.title = "PiNE"
        return TextField()


class TextField(GridLayout):
    def __init__(self):
        super(TextField, self).__init__()
        self.username = TextInput()
        self.cols = 1
        self.add_widget(self.username)


if __name__ == "__main__":
    Main().run()
