
from flask import Flask, request, jsonify, render_template
import logging
from utility import convert_date_to_n, trading_strategy
from model import predict
from datetime import timedelta, datetime
app = Flask(__name__)
app.debug = True


@app.route("/", methods=['GET', 'POST'] )
def index():
       buy_date = "NA"
       sell_date = "NA"
       if request.method == "POST":
              date = request.form["date"]
              nth_day_from_start = convert_date_to_n(date)
              pred_list = predict(nth_day_from_start+1)#+1 because input is the next day after selected day
              pred_list_json = jsonify(pred_list)
              #print(pred_list_json.get_json(), flush=True)
              price_arr = []
              for pred in pred_list:
                     price_arr.append(pred[0])

              buy_day, sell_day = trading_strategy(price_arr)
              date = datetime.strptime(date, "%Y-%m-%d")
              if buy_day == -1:
                     buy_date = "NA"
              else:
                     buy_date = (date + timedelta(days=buy_day)).strftime("%Y-%m-%d")
              if sell_day == -1:
                     sell_date = "NA"
              else:
                     sell_date = (date + timedelta(days=sell_day)).strftime("%Y-%m-%d")
              
              print("Buy date: ", buy_date, flush=True)
              print("Sell date: ", sell_date, flush=True)
              
              return jsonify(pred_list=pred_list, buy_date=buy_date, sell_date=sell_date)
       return render_template('index.html')


if __name__ == '__main__':
       app.run(debug=True)

