from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.utils import rgba

from colors import Colors
from FirebaseRealtimeDB import verify_emt


kv = Builder.load_file('ems_dinput.kv')
class EMSDinput(Screen):
    def check_dl_num(self, license):
        return verify_emt(license)