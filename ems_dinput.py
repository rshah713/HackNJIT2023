from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.utils import rgba
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button

from colors import Colors
from FirebaseRealtimeDB import verify_emt


kv = Builder.load_file('ems_dinput.kv')
class EMSDinput(Screen):
    
    def check_dl_num(self, license):
        b = Button(text="Error verifying license")
        is_valid = verify_emt(license)
        if not is_valid:
            popup = Popup(title='Test popup',
    content=b, size=(200, 400))
            b.bind(on_press=popup.dismiss)
            popup.open()
            return False
        return True