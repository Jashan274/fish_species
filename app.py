from flask import Flask, render_template, request, jsonify
import joblib
import os

app = Flask(__name__)

# Print current working directory for debugging
print("Current working directory:", os.getcwd())

# Define the path to the model files
model_path = os.path.join(os.getcwd(), 'Lab#4', 'classifying_fishes.pkl')
encoder_path = os.path.join(os.getcwd(), 'Lab#4', 'label_encoder.pkl')

# Load trained model and label encoder
try:
    model = joblib.load(model_path)
    le = joblib.load(encoder_path)
    print("Model and LabelEncoder loaded successfully.")
except FileNotFoundError:
    print(
        f"Error: Could not find the model files at '{model_path}' or '{encoder_path}'. Please check the file paths.")
    exit(1)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    weight = float(data['Weight'])
    length1 = float(data['Length1'])
    length2 = float(data['Length2'])
    length3 = float(data['Length3'])
    height = float(data['Height'])
    width = float(data['Width'])

    # Make prediction
    prediction = model.predict(
        [[weight, length1, length2, length3, height, width]])
    predicted_species = le.inverse_transform(prediction)[0]

    return jsonify({'predicted_species': predicted_species})


if __name__ == '__main__':
    app.run(debug=True)
