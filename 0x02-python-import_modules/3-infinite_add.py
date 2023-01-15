#!/usr/bin/python3
""" print sum of all arguments """
if __name__ == "__main__":
    """ this enables running the script like a module """
    import sys
    """ importing sys enables calling of arguments passed on command line """
    arg_add = 0
    for i in range(len(sys.argv) - 1):
        """ for argv we -1 for the end byte """
        arg_add += int(sys.argv[i + 1])
    print("{:d}".format(arg_add))
