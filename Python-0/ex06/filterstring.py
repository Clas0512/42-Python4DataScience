import sys
from ft_filter import ft_filter


def isInteger(i) -> bool:
    """
    Check if the given input is an integer.

    Args:
        i: The input value to check.

    Returns:
        bool: True if the input can be converted to an integer, False
        otherwise.
    """
    try:
        int(i)
        return True
    except ValueError:
        return False


def main():
    """
    Main function to filter words from a string based on a length constraint.

    This function takes two command line arguments:
    1. A string of words separated by spaces.
    2. An integer that acts as the minimum length for filtering the words.

    It splits the string into words, filters out words that are shorter than
    the given integer,
    and then prints the filtered list of words.

    Raises:
        Exception: If there are not exactly two arguments or if the second
        argument is not an integer.
    """
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
