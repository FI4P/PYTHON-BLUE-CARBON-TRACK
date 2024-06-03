from modules.searoutesApi import SeaRoutes;
from modules.applicationMenu import ApplicationMenu;
from database import firebase


vessel = SeaRoutes.Searoute.getVesselByName("teste")

firebase.insertVessel(vessel)

print("teste")