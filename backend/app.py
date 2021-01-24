from flask import Flask, request, jsonify
import base64
from PIL import Image
from io import BytesIO
from flask_cors import CORS
import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns




app = Flask(__name__)    
CORS(app)


def convert(img_data):
    with open("image.jpg", "wb") as fh:
        fh.write(base64.decodebytes(img_data))

numVotes = 0
data = pd.read_csv('10_year_disparities.csv')



class person():
    def __init__(self,age,gender,race):
        self.age = age
        self.gender = gender
        self.race = race
        self.numVotes = 0
        person.classify(self)
        
    def classify(self):    
        numVotes = 0.0
    
        rowNames = list(data['Label'])    
        for i in data['Label']:
            if (str(self.age) in i) or (self.gender in i) or (self.race in i):
                numVotes = numVotes + float(data.iloc[rowNames.index(i)]['Average'])
        self.numVotes = numVotes




@app.route("/predict", methods=['POST'])       
def predict():
    if request.method == 'POST':
        content = request.get_json(silent=True)
        base64Img = content['img']
        base64Img = base64Img.replace("data:image/jpeg;base64,","")
        base64Img = base64Img.encode('ascii')
        convert(base64Img)
        return base64Img
        #parse into pytorch model
        #send into nischay's function
        #return to results back to the front end

@app.route("/predictManuel", methods=['POST'])
def predictManuel():
    if request.method == 'POST':
        content = request.get_json(silent=True)
        age = content['a']
        gender = content['g']
        race = content['r']
        p = person(age, gender, race)
        jsonStr = json.dumps(p.__dict__)
        print(jsonStr)
        return jsonStr
        

    
if __name__ == "__main__":        
    app.run()                     


