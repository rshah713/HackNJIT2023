from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.utils import rgba

from colors import Colors


kv = Builder.load_file('ems_signup.kv')
class EMSSignup(Screen):
    def on_pre_enter(self, *args):
        self.manager.transition.direction = 'up'
    
    def on_pre_leave(self, *args):
        self.manager.transition.direction = 'down'