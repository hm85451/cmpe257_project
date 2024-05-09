import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
import keras
import joblib

# Create sequences of data for LSTM model
def create_sequences(data, seq_length):
    X = []
    for i in range(len(data) - seq_length):
        X.append(data[i:(i + seq_length)])
    return np.array(X)

def predict(date_count):
    seq_length = 60
    features = ['Open', 'High', 'Low', 'Close','Volume']
    
    input_sequence = np.load("inputSequence.npy")
    scaler = joblib.load('scaler.pkl')
    
    model = tf.keras.models.load_model('model/tf2.9/btc_usd_lstm.h5')
    
    input_date = date_count - 60
    x = input_sequence[input_date]
    pred = model.predict(x.reshape((1,seq_length,len(features))))
    pred = scaler.inverse_transform(pred)

    return pred.tolist()




# Load the dataset
data = pd.read_csv('data/BTC-USD.csv')

# Select relevant features
features = ['Open', 'High', 'Low', 'Close','Volume']
data = data[features]

# Preprocess the data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data)

seq_length = 60
input_sequence = create_sequences(scaled_data, seq_length)

np.save("inputSequence.npy", input_sequence)
joblib.dump(scaler, 'scaler.pkl')