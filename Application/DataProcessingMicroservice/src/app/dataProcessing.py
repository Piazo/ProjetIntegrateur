from urllib.request import urlopen
from flask import Flask
import json

app = Flask(__name__)

class dataProcessing:
    @app.route("DataProcessingMicroservice/", methods=['POST']) 
    def process_data():
        #get json from url
        with open (url) as file :
            data = json.load(file)
        return data

    
    