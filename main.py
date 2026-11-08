from config import Config

import ctypes

from kivy.config import Config as KivyConfig


if Config.TEST_PHONE:
    user32 = ctypes.windll.user32
    width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    KivyConfig.set('kivy', 'show_fps', 1)
    # KivyConfig.set("graphics", "width", int(9 / 16 * height * Config.USE_SCREEN_HEIGHT))
    # KivyConfig.set("graphics", "height", int(height * Config.USE_SCREEN_HEIGHT))
    KivyConfig.set('graphics', 'resizable', True)

    KivyConfig.set("modules", "screen", "onex,portrait,scale=0.6")
    KivyConfig.write()

from app import MainApp

if __name__ == "__main__":
    MainApp().run()
