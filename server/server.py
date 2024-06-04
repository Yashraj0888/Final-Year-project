from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)


@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    data = request.get_json()
    total_sqft = data['area_sq_ft']
    location = data['location']
    bhk = data['bhk']
    bath = data['bathrooms']

    estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
    response = jsonify({'estimated_price': estimated_price})

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
