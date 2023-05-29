#!/usr/bin/python3


def uniq_add(my_list=[]):
    set_0 = set()

    for i in my_list:
        set_0.add(i)
    sum_0 = sum(set_0)
    return sum_0
