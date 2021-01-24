from flask import Flask, request, jsonify
import base64
from PIL import Image
from io import BytesIO
from flask_cors import CORS



app = Flask(__name__)    
CORS(app)


def convert(img_data):
    with open("image.jpg", "wb") as fh:
        fh.write(base64.decodebytes(img_data))

@app.route("/predict", methods=['POST'])       
def predict():
    if request.method == 'POST':
        content = request.get_json(silent=True)
        print(content)
        base64Img = content['img']
        base64Img = base64Img.encode('ascii')
        print(base64Img)
        convert(base64Img)
        return base64Img
        #parse into pytorch model
        #send into nischay's function
        #return to results back to the front end
    
if __name__ == "__main__":        
    app.run()                     


