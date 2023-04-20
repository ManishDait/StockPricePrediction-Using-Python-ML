# Stock Price Prediction Web Application

This is a simple web application that uses machine learning to predict future stock prices based on historical data. The application is built using Python Flask web framework.

## Installation

1. Clone the repository.
```
git clone https://github.com/ManishDait/StockPricePrediction-Using-Python-ML.git
```
2. Navigate to project directory.
```
cd StockPricePrediction-Using-Python-ML
```
3. Install the required packages using pip.
```
pip install -r requirements.txt
```

## Usage

1. Start the Flask server.
```
python app.py
```
2. Open your web browser and go to http://localhost:5000.

3. Select the stock symbol (e.g. LT) and the number of intervals to predict.

## How it works

The application uses machine learning to train a model on historical stock prices. The model is then save to `.pickle` format and is used to predict future prices based on the input parameters.
