import datetime
from datetime import timedelta

today = datetime.date.today()

first_day_of_school = datetime.date(2019, 8, 23)

delta = (first_day_of_school - today).days

print("There are " + str(delta) + " left until school starts again.")