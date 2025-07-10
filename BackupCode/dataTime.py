# from datetime import datetime

# now = datetime.now()
# print("Current date and time:", now)
# print("Date:", now.date())
# print("Time:", now.time())
# print("Year:", now.year)
# print("Month:", now.month)
# print("Day:", now.day)
# print("Hour:", now.hour)
# print("Minute:", now.minute)

# formated_date = now.strftime("%d-%m-%Y %H:%M:%S %p")
# print("Formatted date:", formated_date)

# date_str = "13-06-2025"
# converted= datetime.strptime(date_str, "%d-%m-%Y")
# print("Converted date:", converted)

# from datetime import date

# today = date.today()
# print("Today's date:", today)

from datetime import datetime, timedelta

now = datetime.now()
future = now + timedelta(days=7)
past = now - timedelta(days=30)
print("Current date and time:", now)
print("Future date (7 days later):", future)
print("Past date (30 days earlier):", past)