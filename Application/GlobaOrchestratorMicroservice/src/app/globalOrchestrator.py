from urllib.request import Request
from flask import Flask


app = Flask(__name__)

class globalOrchestrator:
    @app.route("/getUrl/{int:zone}")
    def getNewZone(zone: int):
        bestNode=0
        if (zone==1):
            #l'orchestrator renvoie au local orchestrator l'url du local orchestrator 1 
            newZone= "http://localhost:4999//app/bestnode/"
        elif (zone==2):
            #l'orchestrator renvoie au local orchestrator l'url du local orchestrator 2 
            newZone= "http://localhost:4999//app/bestnode/"
        elif (zone==3):
            #l'orchestrator renvoie au local orchestrator l'url du local orchestrator 3 
            newZone= "http://localhost:4999//app/bestnode/"
        return newZone