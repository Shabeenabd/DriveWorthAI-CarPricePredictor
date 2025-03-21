# Drive Worth AI - AI Powered Car Price Predictor 🚗
Welcome to DriveWorthAI, an innovative AI-powered tool designed to predict car prices based on various car features. Whether you're a car enthusiast, a buyer, or a seller, DriveWorthAI provides accurate and reliable price predictions to help you make informed decisions.


🚀 **Live Demo**
**checkout the application [Click here](https://car-price-prediction-8a9y.onrender.com/) 🌐**
## 🌟 Table of Contents

- [Project Overview](#-project-Overview)
- [Key Features](#-key-features)
- [How It Works](#-how-it-works)
- [Installation Instructions](#-installation-instructions)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Model Performance](#-model-performance)

-----

## 🔍 Project Overview
DriveWorthAI is an AI-powered car price prediction model designed to estimate the market value of a car based on key features such as kilometers driven, manufacturing year, ownership type, fuel type, and more.

This project combines the power of machine learning with a sleek and interactive web interface built using Flask, HTML, and Tailwind CSS. DriveWorthAI makes it easy for users to input car details and get real-time price predictions — all from a user-friendly browser-based interface.

Whether you’re buying a used car or planning to sell yours, DriveWorthAI ensures you're informed, confident, and in control of your car deal negotiations.



## ✨ Key Features
- **AI-powered price prediction :** Get instant and accurate car price estimations based on industry patterns and historical data.
- **User-Friendly Web Interface :** Clean, minimal, and interactive web design built with HTML and Tailwind CSS.
- **Modular Backend :** Flask-based architecture, making it easy to extend or deploy on cloud platforms.
- **Real-time :** Predictions: Instant feedback based on user input without the need to wait.

## 🛠️ How It Works
- **Data Collection :** The model is trained on a comprehensive dataset containing various car features and their corresponding prices.
- **Model Training :** A Linear Regression model is trained to learn the relationship between car features and prices.
- **Web Application :** The trained model is integrated into a Flask web application, allowing users to interact with the model through a web interface
- **Price Prediction :** Users input car details, and the model predicts the price based on the provided features.

## 📋 Installation Instructions

To get started with this project, follow the instructions below to set up the environment and install the necessary dependencies.

### Step 1: Clone the Repository

```bash
git clone https://github.com/Shabeenabd/DriveWorthAI-CarPricePredictor.git
cd DriveWorthAI-CarPricePredictor
```
### Step 2: Set Up Python Environment
1. Create a virtual environment:
```bash
python3 -m venv venv
```
2. Activate the virtual environment:
```bash
# For Windows
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate

```
3. Install the required Python dependencies:
```bash
pip install -r requirements.txt
```

## 🎯 Project Structure

```bash
DriveWorthAI/
│
├── app                                            # Web Application 
│    ├── templates                                  
│    │       └── index.html                        # Main HTML file for the web app's front-end interface
│    ├── app.py                                    # Flask application to serve ML model  
│    └── requirements.txt                          # Dependencies for Web Application 
│   
├── artifacts
│     ├── brands.pkl                               # Car Brands details
│     └── scaler.pkl                               # Pretrained Scaler for data transformation
│
├── data                                           # Dataset
│     ├── car_price.csv
│     └── cardekho.csv     
│  
├── model                                          
│     └── saved_model.pkl                          # Trained ML Model
│
├── src                                            
│    ├── feature_engineering.ipynb                 # Data Preprocessing and Feature Engineering
│    ├── model_build.ipynb                         # Model Training
│    └── model_evaluate.ipynb                      # Model Testing
│
├── requirements.txt                               # Project Dependencies
│
└── README.md                                      # This README file
```

## 🚀 Getting Started
#### 1. Data Preprocessing & Feature Engineering
Navigate to the src directory and then launch jupyter to run ipynb notebook files
```bash
cd src
jupyter notebook
```
Run feature_engineering.ipynb to process the data (processed_data.csv will be generated).
#### 2. Model Training
Run model_build.ipynb notebook to train the ML model on the preprocessed data.
Model will be saved in the model folder
#### 3. Model Testing
Run the model_evaluate.ipynb to test the model performance
#### 4. Model Deploy
Navigate to the app directory and then launch flask application to serve the model
```bash
cd app
gunicorn app:app
```

## 📊 Model Performance

- Training Accuracy: 95%
- Validation Accuracy: 93%
- Inference Time: <100ms
