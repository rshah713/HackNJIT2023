from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.utils import rgba

from colors import Colors


kv = Builder.load_file('patient_signup.kv')
class PatientSignup(Screen):
    pass

    
    # def __init__(self, **kwargs):
    #     super(PatientSignup, self).__init__(**kwargs)
    #     Window.clearcolor = rgba(*Colors.BEIGE, 1)

    # def get_info(self, patpass, patemail):
    #     print(patemail.text)
    #     print(patpass.text)
        