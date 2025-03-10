import requests
import json
from ManageEndpoints import convertjson as cjson
import os

consola = int(0)
userName = "kreindo"
api_key: str = "de7WcnZBJWfwLI6Z4qthX3MMtAZIpkf0"

payload = {"y": api_key,
           "g": 1,}

allConsolesfile = "allconsoles.json"

url_allConsoles = "https://retroachievements.org/API/API_GetConsoleIDs.php"
url_allGames = "https://retroachievements.org/API/API_GetGameList.php"

allConsoles = cjson.getendpoint(url_allConsoles,payload,allConsolesfile)

