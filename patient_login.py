from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.utils import rgba

from FirebaseRealtimeDB import login as fb_login
from colors import Colors


kv = Builder.load_file('patient_login.kv')
class PatientLogin(Screen):
    def __init__(self, **kwargs):
        super(PatientLogin, self).__init__(**kwargs)
        Window.clearcolor = rgba(*Colors.BEIGE, 1)
        
    def on_pre_enter(self, *args):
        self.manager.transition.direction = 'left'

    def login(self, patemail, patpass, errorlbl):
        if not fb_login(patemail.text, patpass.text):
            errorlbl.text = 'Email or password could not be verified.'
            return False
        print(patemail.text)
        print(patpass.text)
        return fb_login(patemail.text, patpass.text)
        