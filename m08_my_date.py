"""MEDIUM - Display the date and time"""



# Solution 1
print(__import__("datetime").datetime.now().strftime("Today is %Y-%m-%d and it is %H:%M:%S."))



# Solution 2
import datetime
print(f"{datetime.datetime.now():Today is %Y-%m-%d and it is %H:%M:%S}.")



# Solution 3
today = __import__("datetime").datetime.today()
print(f"Today is {today.year:04d}-{today.month:02d}-{today.day:02d} \
and it is {today.hour:02d}:{today.minute:02d}:{today.second:02d}.")
