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
