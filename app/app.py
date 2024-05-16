
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
              nth_day_from_start = convert_date_to_n(date)
              pred_list = predict(nth_day_from_start+1)#+1 because input is the next day after selected day
              pred_list_json = jsonify(pred_list)
              print(pred_list_json.get_json(), flush=True)
              return pred_list_json
       return render_template('index.html')


if __name__ == '__main__':
       app.run(debug=True)

