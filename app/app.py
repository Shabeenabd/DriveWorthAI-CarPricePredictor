from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import datetime

app = Flask(__name__)

# Load the saved model, scaler, and brand information
def load_artifacts():
    global model, scaler, brands
    model = pickle.load(open('../model/saved_model.pkl','rb'))
    scaler = pickle.load(open('../artifacts/scaler.pkl','rb'))
    brands = pickle.load(open('../artifacts/brands.pkl','rb'))

load_artifacts()

def predict_price(form_data: list) -> float:
    """
    Predict the car price based on form input.
    
    Args:
        form_data (list): List of form values [Brand, Year, KMs Driven, Ownership, Fuel Type]
    
    Returns:
        float: Predicted price of the car
    """
    # Initialize feature vector
    feature_names = model.feature_names_in_
    input_vector = np.zeros(feature_names.shape)

    # Extract form inputs
    car_brand, year, kms_driven, owner_type, fuel_type = form_data[1], form_data[2], form_data[3], form_data[4], form_data[5]

    # Calculate car age
    current_year = datetime.date.today().year
    car_age = current_year - int(year)

    # Scale numerical features (kms driven and age)
    input_vector[:2] = scaler.transform(np.expand_dims([float(kms_driven), car_age], axis=0))

    # One-hot encode categorical features if they exist in training features
    feature_mapping = {
        f'car_{car_brand}': car_brand,
        f'ownership_{owner_type}': owner_type,
        f'fuel_type_{fuel_type}': fuel_type
    }

    for feature_key in feature_mapping:
        if feature_key in feature_names:
            feature_idx = np.where(feature_names == feature_key)[0][0]
            input_vector[feature_idx] = 1

    # Predict log price and convert back using exponential
    predicted_log_price = model.predict(input_vector[np.newaxis, ...])
    predicted_price = np.exp(predicted_log_price)

    return list(predicted_price)



@app.route('/')
def home():
    """
    Render the home page with the brand options.
    """
    return render_template('index.html', data=brands, url='/predict')
    

@app.route('/predict', methods=['POST'])
def predict():
    """
    Handle prediction requests from the form submission.
    """
    form_data = list(request.form.values())

    try:
        prediction = predict_price(form_data)
        return prediction
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)