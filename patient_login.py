from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.utils import rgba

from colors import Colors


kv = Builder.load_file('patient_login.kv')
class PatientLogin(Screen):
    def __init__(self, **kwargs):
        super(PatientLogin, self).__init__(**kwargs)
        Window.clearcolor = rgba(*Colors.BEIGE, 1)

    def get_info(self, patpass, patemail):
        print(patemail.text)
        print(patpass.text)
        