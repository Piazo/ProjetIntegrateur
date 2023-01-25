from flask import Flask, jsonify, request
import requests
import tensorflow as tf
import pandas as pd


app = Flask(__name__)

class modelMicroserviceControler:
    @app.route("/test", methods=['GET'])
    def test(): 
        print("[MOD1] test")
        return "letsgooooo, je suis la ((:"
    
    def predictedLatency(liste: list): # add actual model here, atm just returns average
        model = tf.keras.models.load_model('./Node3')
        latences=liste
        df=pd.DataFrame()
        df['val'] = latences
        df['median'] = df['val'].rolling(3).median()
        df['mean'] = df['val'].rolling(4).mean()
        df = df.drop(columns=['val'])
        df.dropna(inplace=True)
        val = df.values.tolist()
        return model.predict([val])
    
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
        







    