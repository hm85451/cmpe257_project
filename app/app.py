
from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
import tensorflow as tf
import keras

app = Flask(__name__)

model = tf.keras.models.load_model('btc_usd_lstm.h5')


@app.route('/', methods=['GET'])
def home():
       return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
       return "prediction"

if __name__ == '__main__':
       app.jinja_env.auto_reload = True
       app.config['TEMPLATES_AUTO_RELOAD'] = True
       app.run(debug=True)

