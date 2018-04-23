# TODO - did not works
from datetime import date

today = date.today()

cyr_weeknames = ["Понеделник", "Вторник","Сряда"]
daynum = today.weekday()


print(daynum)
# 2

print(cyr_weeknames[daynum])
