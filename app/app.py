
from flask import Flask, request, jsonify, render_template
import logging
from utility import convert_date_to_n
from model import predict

app = Flask(__name__)
app.debug = True


@app.route("/", methods=['GET', 'POST'] )
def index():
       if request.method == "POST":
              date = request.form["date"]
              num_of_days = convert_date_to_n(date)
              pred = predict(num_of_days)
              print(pred, flush=True)
              
              return pred
       return render_template('index.html')


if __name__ == '__main__':
       app.run(debug=False)

