from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.utils import rgba

from colors import Colors


kv = Builder.load_file('patient_signup.kv')
class PatientSignup(Screen):
    def __init__(self, **kwargs):
        super(PatientSignup, self).__init__(**kwargs)
        Window.clearcolor = rgba(*Colors.BEIGE, 1)
        
    def on_pre_enter(self, *args):
        self.manager.transition.direction = 'up'
        
    def on_pre_leave(self, *args):
        self.manager.transition.direction = 'down'

    def valid_credentials(self, patemail, patpass, patpassconfirm, patDriverId):
        if patpass.text!=patpassconfirm.text:
            return False
        if "" in [patemail.text, patpass.text, patpassconfirm.text, patDriverId.text]:
            return False
        if "@" not in patemail:
            return False
        
        return True        