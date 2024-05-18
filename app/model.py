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

def InputValue(x,pred):
    x_f = np.delete(x, (0), axis=0)
    x_f = np.vstack([x_f,pred])
    return x_f


def predict(date_count):
    seq_length = 60
    features = ['Open', 'High', 'Low', 'Close','Volume']
    
    input_sequence = np.load("inputSequence.npy")
    scaler = joblib.load('scaler.pkl')
    
    model = tf.keras.models.load_model('model/tf2.9/btc_usd_lstm.h5')
    
    ind = date_count - seq_length #offset for selecting input sequence
    
    N=7
    N_predictions=[]
    x = input_sequence[ind]
    for _ in range(N):
        pred = model.predict(x.reshape((1,seq_length,len(features))))
        x = InputValue(x,pred)
        pred = scaler.inverse_transform(pred)
        N_predictions.append(np.array(pred).reshape(len(features)).tolist())
    
    return N_predictions




# # Load the dataset
# data = pd.read_csv('data/BTC-USD.csv')

# # Select relevant features
# features = ['Open', 'High', 'Low', 'Close','Volume']
# data = data[features]

# # Preprocess the data
# scaler = MinMaxScaler(feature_range=(0, 1))
# scaled_data = scaler.fit_transform(data)

# seq_length = 60
# input_sequence = create_sequences(scaled_data, seq_length)

# np.save("inputSequence.npy", input_sequence)
# joblib.dump(scaler, 'scaler.pkl')
