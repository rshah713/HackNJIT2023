from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.utils import rgba

from colors import Colors


kv = Builder.load_file('ems_login.kv')
class EMSLogin(Screen):
    def __init__(self, **kwargs):
        super(EMSLogin, self).__init__(**kwargs)
        Window.clearcolor = rgba(*Colors.BEIGE, 1)