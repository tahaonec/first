from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class InterFace(FloatLayout):
    def print_msg(self):
        data = self.ids.textInput.text
        self.ids.label.text = data


class FirstApp(App):
    pass


FirstApp().run()
