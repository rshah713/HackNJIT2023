from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager

from welcome_window import Welcome
from ems_login import EMSLogin
class WindowManager(ScreenManager):
    pass

class MedifyApp(App):
    def build(self):
        return 

if __name__ == '__main__':
    MedifyApp().run()
