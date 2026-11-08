from adodbapi.ado_consts import directions
from kivy.properties import StringProperty
from kivy.uix.screenmanager import NoTransition, SlideTransition
from kivymd.uix.screen import Screen
from kivy.animation import Animation, AnimationTransition

from app.screens import BaseScreen
from app.utils.screen_switcher import switch_to


class MainScreen(BaseScreen):
    name = StringProperty("main_screen")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_manager_bind(self):
        self.manager.get_screen("learn_screen").on_data_loaded = self.enable_button

    def enable_button(self):

        self.ids.spinner.opacity = 0
        self.ids.start_btn.disabled = False
    def start(self):
        switch_to(self.manager, "learn_screen", transition=SlideTransition(direction="left"))
