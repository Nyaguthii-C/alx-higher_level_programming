#!/usr/bin/python3

def fizzbuzz():
    for fizzbuzz in range(1, 101):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print(f"FizzBuzz", end=" ")
        elif fizzbuzz % 3 == 0:
            print(f"Fizz", end=" ")
        elif fizzbuzz % 5 == 0:
            print(f"Buzz", end=" ")
        else:
            print("{}".format(fizzbuzz), end=" ")


fizzbuzz()
