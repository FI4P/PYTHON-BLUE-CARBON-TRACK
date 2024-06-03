from modules.searoutesApi import SeaRoutes;
from modules.applicationMenu import ApplicationMenu;
from database import firebase

applicationMenu = ApplicationMenu.ApplicationMenu()

def main():
    menuId = applicationMenu.loadMenu()    
    applicationMenu.choosedOption(menuId)

main()

