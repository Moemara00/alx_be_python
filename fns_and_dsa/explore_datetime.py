import datetime


# print(dir(datetime))
def display_current_datetime():
    global current_date
    current_date = datetime.datetime.now()
    print(current_date)


display_current_datetime()

days_added = int(input("Enter a number of days: "))

def alculate_future_date():
    future_date = current_date + datetime.timedelta(days=days_added)
    
    print(future_date)

alculate_future_date()