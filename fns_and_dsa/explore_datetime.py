from datetime import datetime, timedelta


# print(dir(datetime))
def display_current_datetime():
    global current_date
    current_date = datetime.now()
    print(current_date)


display_current_datetime()

days_added = int(input("Enter a number of days: "))

def calculate_future_date():
    future_date = current_date +timedelta(days=days_added)
    
    print(future_date)

calculate_future_date()