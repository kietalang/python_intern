# print calendar by given month and year
import calendar

month = int(input("Input month: "))
year = int(input("Input year: "))

print(calendar.month(year, month))