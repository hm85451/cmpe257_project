
from flask import Flask, request, jsonify, render_template
import logging
from utility import convert_date_to_n, trading_strategy
from model import predict
from datetime import timedelta
app = Flask(__name__)
app.debug = True


@app.route("/", methods=['GET', 'POST'] )
def index():
       if request.method == "POST":
              date = request.form["date"]
              num_of_days = convert_date_to_n(date)
              pred = predict(num_of_days)
              print(pred, flush=True)
              
              # buy_day, sell_day = trading_strategy(pred) 
              # this will return the sale and buy date by adding the buy_day and sell_day to the choosen date
              # if the buy_day or sell_day is -1 then it will return NA
              buy_day, sell_day = trading_strategy(pred)
              if buy_day == -1:
                     buy_date = "NA"
              else:
                     buy_date = date + timedelta(days=buy_day)
              if sell_day == -1:
                     sell_date = "NA"
              else:
                     sell_date = date + timedelta(days=sell_day)
              
              return pred
       return render_template('index.html')


if __name__ == '__main__':
       app.run(debug=False)

