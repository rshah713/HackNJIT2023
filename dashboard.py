from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.utils import rgba

from colors import Colors

kv = Builder.load_file("dashboard.kv")
from FirebaseRealtimeDB import update_patient_info                
class Dashboard(Screen):
    def __init__(self, **kwargs):
        super(Dashboard, self).__init__(**kwargs)
        Window.clearcolor = rgba(*Colors.BEIGE, 1)

    def update_creds(self, info):
        info=[i.text for i in info]
        infodic={"name": info[0],
                 "age": info[1],
                 "weight": info[2],
                 "height": info[3],
                 "blood type": info[4],
                 "dlid": info[5],
                 "medical conditions": info[6],
                 "allergies": info[7],
                 "medication": info[8],}
        update_patient_info(infodic)
