from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen


class BaseScreen(Screen):
    name = StringProperty("")

    def on_manager_bind(self): pass

    def on_switch_bind(self): pass