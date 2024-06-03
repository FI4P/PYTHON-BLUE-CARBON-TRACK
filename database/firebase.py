import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from modules.searoutesApi import SeaRoutes;



# Fetch the service account key JSON file contents
cred = credentials.Certificate('database/authFirebase.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://bluecarbontracking-default-rtdb.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('/')

def insertVessel(vessel):

    if not isinstance(vessel, object):
        return print("O argumento deve ser um objeto!")

    try:
        ref.child('vessels').push(vessel)
        print("Inclusão bem-sucedida")
    except Exception as e:
        print("Ocorreu um erro ao inserir no banco de dados:", e)








