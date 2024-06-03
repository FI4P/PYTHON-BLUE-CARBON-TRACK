class ApplicationMenu:
    def __init__(self):
        self._applicationMenu = {
            "Options": ["1", "2", "3", "4", "5"],
            "Functionalities": ["Adicionar embarcação", "Remover embarcação", "Listar embarcações","Emissão de CO2 por embarcacão especifica", "Análise das embarcações disponiveis"]
        }

    def loadMenu(self):
        for i in range(len(self._applicationMenu["Options"])):
            print(f"\033[92m{self._applicationMenu['Options'][i]}\033[0m - {self._applicationMenu['Functionalities'][i]}")


