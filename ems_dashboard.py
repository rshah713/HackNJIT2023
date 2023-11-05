from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import Screen

from colors import Colors
from FirebaseRealtimeDB import get_patient_info
kv = Builder.load_file('ems_dashboard.kv')

class EMSDashboard(Screen):
    def on_enter(self):
        self.fill_labels()
    def fill_labels(self):
        dlid = App.get_running_app().get_dlid()
        info = get_patient_info(dlid)
        self.ids.patname.text += info["name"]
        self.ids.patage.text += info["age"]
        self.ids.patheight.text += info["height"]
        self.ids.patweight.text += info["weight"]
        self.ids.patBT.text += info["blood type"]
        self.ids.patID.text += info["dlid"]
        self.ids.patMedCond.text += info["medical conditions"]
        self.ids.patAllergies.text += info["allergies"]
        self.ids.patMedication.text += info["medication"]
                                      
        print(info)

