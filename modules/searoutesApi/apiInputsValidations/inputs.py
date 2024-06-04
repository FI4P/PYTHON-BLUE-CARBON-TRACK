from modules.applicationMessages import applicationMessages;

messages = applicationMessages.Messages()


class ApiInputs:
    def formatAllVessels(allVessels):
        formatedVessels = []
        keyMapping = {
            "imo": "International Maritime Organization ID",
            "length": "Largura",
            "maxDraft": "maxDraft",
            "name": "Nome",
            "width": "Largura",
            
        }

        for key in allVessels.keys():
            vesselObj = {}
            for vesselKey in allVessels[key].keys():
                if vesselKey in keyMapping:
                    vesselObj[keyMapping[vesselKey]] = allVessels[key][vesselKey]
            formatedVessels.append(vesselObj)
        return formatedVessels
                
    def formatPrint(arrayVessels):
        messages.spaceDivisor(1)
        messages.successMessage("Listagem de embarcações")
        messages.applicationDivisor()
        for i in range(len(arrayVessels)):
            print(f" \033[1;34m Embarcação: {arrayVessels[i]['Nome']} \033[0m")
            for key in arrayVessels[i].keys():
                print(f"{key} da embarcação: {arrayVessels[i][key]}")
            messages.applicationDivisor()
        return
            
    def co2Infos(co2eData):
        formattedEmissionsData = {
            'Emissões Totais WTW (g CO2e)': co2eData['total'],
            'Emissões WTT (g CO2e)': co2eData['wtt'],
            'Emissões TTW (g CO2e)': co2eData['ttw'],
            'Fator de Intensidade (kg CO2e por t.km)': co2eData['intensity']
        }
        return formattedEmissionsData
    
    def printco2Infos(co2Data, vesselImo):
        messages.spaceDivisor(1)
        messages.successMessage(f"Relatório de emissão de C02: {vesselImo}")
        messages.applicationDivisor()
        for key in co2Data.keys():
            print(f"{key} da embarcação: {co2Data[key]}")
        messages.applicationDivisor()
        
        

            