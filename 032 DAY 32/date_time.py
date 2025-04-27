import datetime as dt

weekdays = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
months = ["",'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

now = dt.datetime.now()
year = now.year
month = now.month
time = now.time()
day_of_wk = now.weekday()

print(f"Current Time is {time} \nToday's {weekdays[day_of_wk+1]}\nCurrent Month is {months[month]} \nDay of the week {day_of_wk+1}")

d_o_b = dt.datetime(year= 2004,month= 11,day= 1)
print(d_o_b)

