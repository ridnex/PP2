#Write a Python program to subtract five days from current date.
import datetime
now = datetime.datetime.now()
before_5days = now - datetime.timedelta(days=5)
print(before_5days)
