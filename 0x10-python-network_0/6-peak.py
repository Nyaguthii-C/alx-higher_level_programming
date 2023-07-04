#!/usr/bin/python3
""" a function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    for (int i=0, i < size(list_of_integers); i++)
        for (int j=1, j <= size(list_of_integers); j++)
            if (list_of_integers[i] < list_of_integers[j])
                continue
            else:
                print(f'{i}')
