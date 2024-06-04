
from modules.applicationMenu import ApplicationMenu;

applicationMenu = ApplicationMenu.ApplicationMenu()

def main():
    menuId = applicationMenu.loadMenu()    
    applicationMenu.choosedOption(menuId)

main()

