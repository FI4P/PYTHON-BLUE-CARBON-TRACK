from modules.applicationMessages import applicationMessages;
import json;

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
        
    
    def extractCo2Infos(co2Data):
        limites_risco = {
            "intensity": 0.1,
            "total": 1000000,
            "ttw": 800000,
            "wtt": 200000
        }
        emissionObj = {}
        total_intensity = 0
        total_total = 0
        total_ttw = 0
        total_wtt = 0
        cont = 0
        
        for embarcacao in co2Data:
            dados_emissao = co2Data[embarcacao]
            total_intensity += dados_emissao["intensity"]
            total_total += dados_emissao["total"]
            total_ttw += dados_emissao["ttw"]
            total_wtt += dados_emissao["wtt"]
            cont += 1
        media_intensity = total_intensity / cont
        media_total = total_total / cont
        media_ttw = total_ttw / cont
        media_wtt = total_wtt / cont
        
        risco_intensity = media_intensity > limites_risco["intensity"]
        risco_total = media_total > limites_risco["total"]
        risco_ttw = media_ttw > limites_risco["ttw"]
        risco_wtt = media_wtt > limites_risco["wtt"]
        
        alertMessage = ""
        if risco_intensity or risco_total or risco_ttw or risco_wtt:
            alertMessage = "Emissões acima dos limites aceitáveis. Risco de impacto ambiental elevado."
        else:
            alertMessage = "Emissões dentro dos limites aceitáveis. Baixo risco de impacto ambiental."
        
        emissionObj["Média da instensidade"] = media_intensity
        emissionObj["Média Total de emissão"] = media_total
        emissionObj["Média de TTW"] = media_ttw
        emissionObj["Média da WTT"] = media_wtt
        emissionObj["message"] = alertMessage
        
        return emissionObj        
        
    
    def co2InfosPrint(co2Data):
        messages.spaceDivisor(1)
        messages.successMessage("Relatório de análise geral das emissões")
        messages.applicationDivisor()
        for key in co2Data.keys():
            if(key == "message"):
                return messages.successMessage(f"Resultado final: {co2Data[key]}")
            print(f"{key} das embarcações: {co2Data[key]}")
        messages.applicationDivisor()
        
    
    def geralInfos():
        marineTraffic = "https://www.marinetraffic.com/en/ais/home/centerx:17.5/centery:33.8/zoom:7"
        messages.successMessage("Informações gerais de embarcações")
        messages.spaceDivisor(1)
        print(f"Caso não saiba informações como Local de partida e Destino da sua embarcação acesse: {marineTraffic} ")
        messages.applicationDivisor()
        

            