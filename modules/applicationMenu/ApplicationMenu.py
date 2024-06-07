from modules.applicationMessages import applicationMessages;
from modules.searoutesApi import SeaRoutes;
from modules.applicationMenu import ApplicationMenu;
from database import firebase
from modules.searoutesApi.apiInputsValidations.inputs import ApiInputs;


messages = applicationMessages.Messages()
class ApplicationMenu:
    def __init__(self):
        self._applicationMenu = {
            "Options": ["1", "2", "3", "4", "5", "0"],
            "Functionalities": ["Adicionar embarcação ao banco de dados", "Remover embarcação do banco de dados", "Listar embarcações disponíveis","Emissão de CO2 por embarcacão especifica", "Análise das embarcações disponiveis", "Informações gerais - Embarcações"]
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
        if(selectedOption == "2"):
            vesselImo = input("Digite o IMO da embarcação:  ")
            firebase.deleteVessel(vesselImo)
            return
        if(selectedOption == "3"):
            allVessels = firebase.getAllVessels()
            ApiInputs.formatPrint(allVessels)
            return
        if(selectedOption == "4"):
            vesselImo = input("Digite o IMO da embarcação:  ")
            departurePort = input("Digite o porto destino da embarcação:  ")
            destinationPort = input("Digite o porto destino da embarcação:  ")
            co2Emission = SeaRoutes.Searoute.getCo2ByGivenVessel(vesselImo, departurePort,destinationPort)
            name = SeaRoutes.Searoute.getVesselPosition(vesselImo)
            if(not co2Emission):
                messages.errorMessages("Não foi possivel encontrar a informação da embarcação!")
                return
            if(name):
                co2Emission["name"] = name
            firebase.insertVesselCo2Info(vesselImo, co2Emission)
            co2EmissionData = ApiInputs.co2Infos(co2Emission)
            ApiInputs.printco2Infos(co2EmissionData, vesselImo)
            return
        if(selectedOption == "5"):
            allCo2Infos = firebase.getAllCo2Infos()
            extractData = ApiInputs.extractCo2Infos(allCo2Infos)
            ApiInputs.co2InfosPrint(extractData)
            return
        if(selectedOption == "0"):
            ApiInputs.geralInfos()
            return
        

            
            

