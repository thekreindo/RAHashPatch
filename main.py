import requests
import json
import os

consola = int(0)
userName = "kreindo"
api_key: str = "de7WcnZBJWfwLI6Z4qthX3MMtAZIpkf0"

payload = {"y": api_key,
           "g": 1}

allConsoles = "https://retroachievements.org/API/API_GetConsoleIDs.php"
allGames = "https://retroachievements.org/API/API_GetGameList.php"

reqAllConsoles = requests.get(allConsoles, params=payload)
reqAllConsolesjson = reqAllConsoles.json()

with open("allconsole.json", "w") as file:
    json.dump(reqAllConsolesjson, file, indent=4)

with open("allconsole.json", "r") as file:
    reqAllConsolesjson = json.load(file)

consoleId = reqAllConsolesjson[consola]["ID"]
consoleName = reqAllConsolesjson[consola]["Name"]

print(f"The console ID for {consoleName} is {consoleId}")
