import sys

args = sys.argv[1:]

def isInteger(i) -> bool:
    try:
        int(i)
        return True
    except ValueError:
        return False

if (args.__len__() == 1):
    if (isInteger(args[0]) is False):
        print('AssertionError: argument is not an integer')
    elif (int(args[0]) % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")
elif (args.__len__() > 1):
    print('AssertionError: more than one argument is provided')