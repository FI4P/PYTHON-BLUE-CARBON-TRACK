from modules.searoutesApi import SeaRoutes;
from modules.applicationMenu import applicationMenu;
from database import firebase

menu = applicationMenu.ApplicationMenu()



vessel = SeaRoutes.Searoute.getVesselByName("nyc")

firebase.insertVessel(vessel)

menu.loadMenu()


