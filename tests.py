from datetime import datetime
import requests as request
from getpass import getpass

endpoint = "http://127.0.0.1:8000/api/token/"
username = input("Nom:")
password = getpass("Votre mot de passe: ")

# data for the authentication
data = {
   "password": password,
   "username":username
}

# only post can be use to obtain the token
get_response = request.post(endpoint, data=data)

# print(get_response.json())

# headers configuration : ajouter pour n'import quelle autre request
token = get_response.json()['access']
headers = {
    "Authorization" : f"WEND-PANGA {token}"
}

mission={
      "exercice_conerne": 2,
      "vehicule_concerne": 2,
      "trajet_concerne": 1,
      "motif": "Approvissionement",
      "etat_mission": False,
      "date_mission": datetime.now().date
    }
if get_response.status_code ==200:
    # endpoint = "http://127.0.0.1:8000/exercices"

    # get_exo =  request.get(endpoint, headers=headers)
    # print(get_exo.json())

    endPointAjoutMission="http://127.0.0.1:8000/missions/creer/"

    get_resp = request.post(endPointAjoutMission,data=mission, headers=headers)
    
    print(get_resp.json())

# https://httpbin.org/ : Good web site about http verbs