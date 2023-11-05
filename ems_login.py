from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.utils import rgba

from FirebaseRealtimeDB import login as fb_login
from colors import Colors


kv = Builder.load_file('ems_login.kv')
class EMSLogin(Screen):
    def __init__(self, **kwargs):
        super(EMSLogin, self).__init__(**kwargs)
        Window.clearcolor = rgba(*Colors.BEIGE, 1)
    
    def login(self, email, password, ems_id, errorlbl):
        print(email, password)
        if len(ems_id) < 12:
            return False
        return fb_login(email, password)