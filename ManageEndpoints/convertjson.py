import requests
import json


def getendpoint(endpoint, payload, filename):
    obtainedEndPoint = requests.get(endpoint, params=payload)
    jsonEndPoint = obtainedEndPoint.json()

    with open(filename, "w") as file:
        json.dump(jsonEndPoint, file, indent=4)

    with open(filename, "r") as file:
        jsonEndPoint = json.load(file)
    