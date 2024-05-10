from datetime import datetime, timedelta

def convert_date_to_n(date):
    #first date in the training_data
    start_date = '2014-09-17'
    
    # Convert the start and end dates to datetime objects
    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_obj = datetime.strptime(date, '%Y-%m-%d')

    # Calculate the difference between the end date and start date
    delta = end_date_obj - start_date_obj

    # Extract the number of days from the timedelta object and add 1
    # Adding 1 to include both the start and end dates in the count
    num_dates = delta.days + 1

    return num_dates


def trading_strategy(price):
    buy_day = -1
    sell_day = -1

   
    min_ind = price.index(min(price))
    max_ind = price.index(max(price))

   # If the price goes up and then down, buy on the low day and sell on the high day
    if min_ind < max_ind:
        buy_day = min_ind
        sell_day = max_ind

    # If the price goes all the way down, sell on the high day
    elif max_ind < min_ind and min_ind == len(price) - 1:
        sell_day = max_ind

    # If the price goes all the way up, sell on the high day and don't buy
    elif max_ind < min_ind and max_ind == len(price) - 1:
        sell_day = max_ind

    return [buy_day, sell_day]
