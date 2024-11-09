from flask import Flask, request, jsonify
import pandas as pd
from your_code_file import MachineLearning  # Import your MachineLearning class

# Initialize the Flask app and create an instance of your ML model
app = Flask(__name__)
ml = MachineLearning()

# Define an endpoint for training the model
@app.route('/train', methods=['POST'])
def train():
    try:
        ml.flow_training()  # Call the training method in your class
        return jsonify({'status': 'Training complete'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Define an endpoint for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the POST request
        data = request.json['data']  # Assuming the input is a JSON object
        prediction = ml.predict(data)  # Add a predict method to your class if needed
        return jsonify({'prediction': prediction})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Start the server on port 5000
