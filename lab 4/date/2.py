# Write a Python program to print yesterday, today, tomorrow.
import datetime
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)
print("Yesterday:", yesterday.strftime("%d"))
print("Today:", today.strftime("%d"))
print("Tomorrow:" , tomorrow.strftime("%d"))