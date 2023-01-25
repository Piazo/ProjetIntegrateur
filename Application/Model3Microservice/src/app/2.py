from flask import Flask, jsonify, request
import requests


app = Flask(__name__)

class modelMicroserviceControler:
    @app.route("/test", methods=['GET'])
    def test(): 
        print("[MOD1] test")
        return "letsgooooo, je suis la ((:"
    
    def predictedLatency(list: list): # add actual model here, atm just returns average
        sum = 0.0
        for val in list:
            sum += val
        mean = sum / len(list)
        return mean
    
    @app.route("/predict", methods=['POST'])
    def predicts():
        print("[MOD1] getPrediction")
        prev = request.get_json(force=True)
        print(prev)
        latency = modelMicroserviceControler.predictedLatency(prev['prev'])
        # latency=requests.post('http://172.17.0.2:51001/predict', json=prev)
        return jsonify({
            'latency': latency
            })
        







    