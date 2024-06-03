from modules.applicationMessages import applicationMessages;
from modules.searoutesApi import SeaRoutes;
from modules.applicationMenu import ApplicationMenu;
from database import firebase
from modules.searoutesApi.apiInputsValidations import inputs; 

apiInputs = inputs.ApiInputs()
messages = applicationMessages.Messages()
class ApplicationMenu:
    def __init__(self):
        self._applicationMenu = {
            "Options": ["1", "2", "3", "4", "5"],
            "Functionalities": ["Adicionar embarcação ao banco de dados", "Remover embarcação do banco de dados", "Listar embarcações disponíveis","Emissão de CO2 por embarcacão especifica", "Análise das embarcações disponiveis"]
        }

    def loadMenu(self):
        messages.welcomeMessage()
        messages.applicationDivisor()
        messages.optionMessage("\033[1;34m Selecione uma das opções disponíveis: \033[0m")
        for i in range(len(self._applicationMenu["Options"])):
            print(f"\033[92m{self._applicationMenu['Options'][i]}\033[0m - {self._applicationMenu['Functionalities'][i]}")
        
        messages.applicationDivisor()
        
        return self.inputValidation("", self._applicationMenu["Options"])
    
    def inputValidation(self, optionInput, possibleOptions, action = "option"):
        messages.optionMessage("\033[1;34m Sua opção: \033[0m")
        option = input(optionInput)
        while (option not in possibleOptions):
            messages.errorMessages(action)
            option = input(optionInput)
        return option

    def choosedOption(self, selectedOption):
        if(selectedOption == "1"):
            vesselName = input("Digite o nome da embarcação:  ")
            vessel = SeaRoutes.Searoute.getVesselByName(vesselName)
            firebase.insertVessel(vessel)
            return
        if(selectedOption == "3"):
            allVessls = firebase.getAllVessels()
            print(allVessls)
            

