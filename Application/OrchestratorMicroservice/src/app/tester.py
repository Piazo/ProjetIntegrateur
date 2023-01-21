from flask import Flask, request
import requests

app = Flask(__name__)

class orchestator:
    @app.route("/getPrediction", methods=['GET', 'POST'])
    def getPrediction():
        print("[ORCH] getPrediction")
        prev = request.get_json(force=True)
        #return prev
        #send requests to prediction microservice 
        # print(prev)
        latency= requests.post('http://model1:5000/predict', json=prev)
        print(latency.text)

        #send list of latencies to result processing microservice and return the best nodes
        # bestNode=requests.get('http://localhost:50001/getResult', json=latencyList)
        return latency.text

    @app.route("/test", methods=['GET', 'POST'])
    def test(): 
        print("[ORCH] test")
        # msg = requests.get('http://172.25.0.2:5000/test', allow_redirects=False, data="", headers="")
        # msg = "ohyessssss je suis la (:"

        msg = requests.get('http://model1:5000/test')
        print(msg.text)
        return msg.text


