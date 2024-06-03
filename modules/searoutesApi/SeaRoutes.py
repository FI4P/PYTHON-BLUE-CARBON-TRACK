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
    
