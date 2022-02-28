#Write a Python program to calculate two date difference in seconds.
import datetime

date1 = input() # format 2020 02 28 14 10 34
date_1 = datetime.datetime.strptime(date1, "%Y %m %d %H %M %S")

date2 = input() # format 2020 02 28 14 10 34
date_2 = datetime.datetime.strptime(date2, "%Y %m %d %H %M %S")
print((date_2 - date_1).total_seconds()) # 1 way

difference = date_2 - date_1
print(difference.days * 24 * 3600 + difference.seconds) # 2 way