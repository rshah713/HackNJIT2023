from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import Screen

from colors import Colors
from FirebaseRealtimeDB import get_patient_info
kv = Builder.load_file('ems_dashboard.kv')
class EMSDashboard(Screen):
    pass

