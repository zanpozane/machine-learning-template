from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load the trained model
model = joblib.load('models/model.pkl')

# Initialize Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON request data
    data = request.get_json()

    # Extract the input features from the data
    features = np.array([data['progres_pekerjaan']]).reshape(1, -1)

    # Make a prediction
    prediction = model.predict(features)[0]

    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)