#!/usr/bin/python3
for letr in range(97, 123):
    if letr == 101 or letr == 113:
        continue
    print("{:c}".format(letr), end="")
