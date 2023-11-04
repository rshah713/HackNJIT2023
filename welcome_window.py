from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.utils import rgba

from colors import Colors

kv = Builder.load_file("welcome.kv")
                       
class Welcome(Screen):
    def __init__(self, **kwargs):
        super(Welcome, self).__init__(**kwargs)
        Window.clearcolor = rgba(*Colors.BEIGE, 1)