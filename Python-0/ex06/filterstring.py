import sys
from ft_filter import ft_filter

def isInteger(i) -> bool:
    try:
        int(i)
        return True
    except ValueError:
        return False

def main():
    try:
        args = sys.argv[1:]
        if (args.__len__() != 2 or isInteger(args[1]) is False):
            raise Exception('AssertionError: the arguments are bad')
        split_list = args[0].split()
        new_list = ft_filter(lambda x: len(x) > int(args[1]), split_list)
        print(list(new_list))
    except Exception as error_msg:
        print(error_msg)

if __name__ == ("__main__"):
    main()