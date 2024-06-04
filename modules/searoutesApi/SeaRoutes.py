import requests

class Searoute:
    @staticmethod
    def getVesselByName(vesselName):
        if not isinstance(vesselName, str):
            raise ValueError("O nome do navio deve ser uma string.")
        if vesselName.isspace():
            vesselName = vesselName.replace(" ", "%20")
            
        endpoint = f"https://api.searoutes.com/vessel/v2/{vesselName}/info"
        headers = {
            "accept": "application/json",
            "x-api-key": "EUiWPXCu0p887kiSoIcPC2v623mEdVO45otMVZJv"
        }
        
        try:
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status() 
            if(response.status_code == 200):
                vesselsArray = response.json()
                return vesselsArray[0]
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"An error occurred: {req_err}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return None
    
    def getVesselPosition(vesselImo):
        url = f"https://api.searoutes.com/vessel/v2/{vesselImo}/position"

        headers = {
            "accept": "application/json",
            "x-api-key": "EUiWPXCu0p887kiSoIcPC2v623mEdVO45otMVZJv"
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            coordinates = data[0]['position']['geometry']['coordinates']
            return coordinates
        else:
            return None

    @staticmethod
    def getCo2ByGivenVessel(vesselImo):
        base_url = f"https://api.searoutes.com/co2/v2/direct/sea?&imo={vesselImo}"

        headers = {
            "accept": "application/json",
            "x-api-key": "EUiWPXCu0p887kiSoIcPC2v623mEdVO45otMVZJv"
        }

        params = {
            "fromLocode": "FRMRS",       # Localização de origem
            "toLocode" : "HKHKG",        # Localização de destino
            "allowIceAreas": "false",    # Permitir áreas de gelo
            "avoidHRA": "false",         # Evitar áreas de alto risco
            "avoidSeca": "false",        # Evitar áreas de controle de emissões de enxofre
            "nContainers": 1,            # Número de contêineres
            "vesselImo": vesselImo      # Número IMO da embarcação
        }   

        try:
            response = requests.get(base_url, headers=headers ,params=params)
            response.raise_for_status()  # Lança uma exceção para códigos de status HTTP diferentes de 200
            data = response.json()
            return data["co2e"]
        except Exception as err:
            print(f'Não foi possivel encontrar a informação da embarcação providenciada!')
        return None

