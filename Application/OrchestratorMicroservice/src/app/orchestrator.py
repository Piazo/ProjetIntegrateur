# from urllib.request import urlopen
from flask import Flask, request
import json
import requests

app = Flask(__name__)

class orchestator:
    @app.route("/app/bestnode/", methods=['GET', 'POST'])
    def getBestNode():
        # Juste pour tester, en vrai on se connecte au bdd
        #latencies1 = {"prev": [1.22, 0.34, 0.91, 2.59, 1, 1.14]}
        #latencies2 = {"prev": [1.4, 1.4, 1.4, 1.4, 1.4, 1.4]}
        #latencies3 = {"prev": [0.91, 0.91, 0.91, 0.91, 0.91, 0.91]}
        #print(latencies1)
        #print(type(latencies1))

        #get latencies from data base
        response = requests.get('http://localhost:50004/BDDMicroservice/getDB')
        latencies= json.loads(response.text)
        latencies1= {"prev": latencies[0]}
        latencies2= {"prev": latencies[1]}
        latencies3= {"prev": latencies[2]}

        latencyList= []
        bestNode={}

        # Send requests to prediction microservices 
        predicted1 = requests.post('http://model1:5000/predict', json=latencies1)
        latencyList.append(predicted1.json())
        predicted2 = requests.post('http://model2:5000/predict', json=latencies2)
        latencyList.append(predicted2.json())
        predicted3 = requests.post('http://model3:5000/predict', json=latencies3)
        latencyList.append(predicted3.json())

        # add new values to the database
        # add docker to database
        parameters1 = {'node': 1, 'moyenne': predicted1}
        response = requests.post('http://localhost:50004/BDDMicroservice/insert', json=parameters1)
        parameters2 = {'node': 2, 'moyenne': predicted2}
        response = requests.post('http://localhost:50004/BDDMicroservice/insert', json=parameters2)
        parameters3 = {'node': 3, 'moyenne': predicted3}
        response = requests.post('http://localhost:50004/BDDMicroservice/insert', json=parameters3)
        
        print(latencyList)
        print("pred1:", predicted1)
        print(".text :", predicted1)
        
        # return latencyList # "jusqu'ici ca va <33 "
        #send list of latencies to result processing microservice and return the best nodes
        bestNode=requests.post('http://processing:5000/getResult', json=latencyList)
        return bestNode.text

    @app.route("/app/changezone/", methods=['GET'])
    def changezone():
        args = request.args
        zone = args.get('zone')
        # send messsge to global orchestrator
        url=requests.get('http://localhost:50003/getUrl?zone=1')
        return url.text

