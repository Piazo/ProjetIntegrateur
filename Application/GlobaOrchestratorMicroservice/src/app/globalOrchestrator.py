from urllib.request import Request
from flask import Flask

import orchestrator

app = Flask(__name__)

class globalOrchestrator:
    @app.route("/{int:zone}")
    def getNewZone(zone: int):
        bestNode=0
        if zone==1:
            #utiliser l'orchestrator de zone 1
            # importer les autres trucs
            # 
            bestNode= orchestrator.getBestNode()
        return bestNode