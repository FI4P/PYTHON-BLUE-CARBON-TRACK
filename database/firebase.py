import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from modules.searoutesApi import SeaRoutes;
from modules.applicationMessages import applicationMessages;
from modules.searoutesApi.apiInputsValidations.inputs import ApiInputs;


messages = applicationMessages.Messages()

# Fetch the service account key JSON file contents
cred = credentials.Certificate('database/authFirebase.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://bluecarbontracking-default-rtdb.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('vessels')

def insertVessel(vessel):

    if not isinstance(vessel, object):
        return print("O argumento deve ser um objeto!")

    try:
        ref.child(f'vessel_{vessel["imo"]}').set(vessel)
        messages.successMessage("Inclusão bem-sucedida!")
        messages.applicationDivisor()   
    except Exception as e:
        messages.errorMessages(f"Ocorreu um erro ao inserir a embarcaççao no banco de dados! {e}")

def getAllVessels():
    
    try:
        allVessels = ref.get()
        formatedVessels = ApiInputs.formatAllVessels(allVessels)
        return formatedVessels
    except Exception as e:
        messages.errorMessages(f"Ocorreu um erro ao listar as embarcações disponíveis! {e}")

def deleteVessel(vesselImo):
    try:
        ref.child(f"vessel_{vesselImo}").delete()
        messages.successMessage("Remoção bem-sucedida!")
        messages.applicationDivisor()
        return 
    except Exception as e:
        messages.errorMessages(f"O imo inserido não é válido ou não existe no banco de dados!")
        
        
def insertVesselCo2Info(vessel, co2Data):
    try:
        co2Ref = db.reference("co2Infos")
        co2Ref.child(f'vessel_{vessel}_co2').set(co2Data)
        messages.applicationDivisor()   
    except Exception as e:
        messages.errorMessages(f"Ocorreu um erro ao inserir a embarcaççao no banco de dados! {e}")

def getAllCo2Infos():
    try:
        co2Ref = db.reference("co2Infos")
        allVesselsCo2Infos = co2Ref.get()
        return allVesselsCo2Infos
    except Exception as e:
        messages.errorMessages(f"Ocorreu um erro ao listar as informações das embarcações disponíveis! {e}")




