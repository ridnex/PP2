#Write a Python program to drop microseconds from datetime.

import datetime

now = datetime.datetime.now()
drop = now.replace(microsecond=0)
print(now)
print(drop)