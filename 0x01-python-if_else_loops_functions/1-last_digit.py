#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_number = int(repr(number)[-1])
if last_number < 6 and last_number != 0:
    str = "and is less than 6 and not 0"
elif last_number > 5:
    str = "and is greater than 5"
else:
    str = "and is 0"
print(f"The last number of {number:d} is {last_number:d} {str}")
