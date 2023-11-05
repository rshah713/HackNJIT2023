import pyrebase

'''
Medical Information Format
info = {  "name" : "Jonas",
          "age" : "15",
          "weight" : "145",
          "height" : "5'10",
          "blood type" : "A",
          "dlid" : "122441",
          "medical conditions" : "None",
          "allergies" : "Sound",
          "medication" : "None"
}
'''

config = {
  'apiKey': "AIzaSyBLCdqXHMYP-Hm0maNclOpiWK-UsiQ-Eto",
  'authDomain' : "medify-37830.firebaseapp.com",
  'databaseURL': "https://medify-37830-default-rtdb.firebaseio.com",
  'projectId' : "medify-37830",
  'storageBucket' : "medify-37830.appspot.com",
  'messagingSenderId' : "882712357939",
  'appId' : "1:882712357939:web:f924a4b3f753079639c746",
  'measurementId' : "G-5H0GB0Z7WQ"
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()
auth = firebase.auth()


def login(email, password):
    id_token = None

    try:
        id_token = auth.sign_in_with_email_and_password(email, password)["idToken"]
    except:
        print("Invalid credentials")

    return id_token is not None


def create_acct(email, password):
    auth.create_user_with_email_and_password(email, password)


def verify_emt(ems_id):
    emt_list = database.child("emts").get().val()
    return ems_id in emt_list


def update_patient_info(info):
    patients = database.child("patients").get().val()

    if info["dlid"] in patients:
        for key in info:
            patients[info["dlid"]][key] = info[key]
        database.child("patients").set(patients)
    else:
        patients[info["dlid"]] = info
        database.child("patients").set(patients)


def get_patient_info(dlid):
    patient_info = None
    
    try:
        patient_info = database.child("patients").child(dlid).get().val()
    except:
        print("User not found!!!")
    return patient_info

'''
def update_patient_info(info):
    patients = database.child("patients").get().val()

    if info["dlid"] in patients:
        for key in info:
            database.child("patients").child(info["dlid"]).update({key: info[key]})
    else:
        database.child("patients").set({info["dlid"] : info})

'''