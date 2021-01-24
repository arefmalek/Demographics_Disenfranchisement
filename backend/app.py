from flask import Flask, request, jsonify
import base64
from PIL import Image
from io import BytesIO


app = Flask(__name__)       

def convert(img_data):
    with open("image.jpg", "wb") as fh:
        fh.write(base64.decodebytes(img_data))

@app.route("/predict", methods=['POST'])       
def predict():
    if request.method == 'POST':
        content = request.get_json(silent=True)
        base64Img = content['img']
        base64Img = base64Img.encode('ascii')
        convert(base64Img)
        return base64Img
        #parse into pytorch model
        #send into nischay's function
        #return to results back to the front end
    
if __name__ == "__main__":        
    app.run()                     


