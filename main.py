from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager

from welcome_window import Welcome
from ems_login import EMSLogin
from ems_signup import EMSSignup
from ems_dinput import EMSDinput
from ems_dashboard import EMSDashboard
from patient_login import PatientLogin
from patient_signup import PatientSignup
from dashboard import Dashboard
class WindowManager(ScreenManager):
    pass

class MedifyApp(App):
    def build(self):
        return
    def save_dlid(self, dlid):
        self.dlid = dlid
    def get_dlid(self):
        return self.dlid

if __name__ == '__main__':
    MedifyApp().run()