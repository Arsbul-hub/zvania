from kivy.uix.screenmanager import *

from app.screens.MainScreen import *
from app.screens.LearnScreen import *
from app.layouts import get_all_layouts
from app.widgets.ImageButton import *

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager


def init_screens(container):
    main_screen = MainScreen()
    container.add_widget(main_screen)

    enter_screen = LearnScreen()
    container.add_widget(enter_screen)
    container.switch_to(main_screen, transition=NoTransition())
    main_screen.on_manager_bind()
    enter_screen.on_manager_bind()

class MainApp(MDApp):
    def build(self):
        for path in get_all_layouts():
            Builder.load_file(path)
        root_screen = ScreenManager()
        init_screens(root_screen)

        return root_screen
