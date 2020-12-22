from datetime import date

first_day = date(2014, 7, 2)
last_day = date(2014, 7, 11)

sum_days = last_day - first_day

print(sum_days.days)