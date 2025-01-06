import sys


def check_args(args: list):
    """
    Check and ensure there is a valid argument provided.
    If no argument is given, prompt the user to input a text.

    Args:
        args (list): A list of command line arguments.

    Raises:
        Exception: If there are more than one argument provided, it raises an
        assertion error.
    """
    while (args.__len__() < 1 or args[0] is None):
        args_input = ""
        try:
            print("What is the text to count?\n")
            args_input = input()
            args.append(args_input + " ")
        except EOFError:
            break
    if (args.__len__() > 1):
        raise Exception("AssertionError: argument length invalid")


def print_features(features: dict):
    """
    Print the statistical features of the provided text.

    Args:
        features (dict): A dictionary containing the counts of various
        character types in the text.
    """
    print(f"\nThe text contains { sum(features.values()) } characters:")
    print(f"{ features['upper_cases'] } upper letters")
    print(f"{ features['lower_cases'] } lower letters")
    print(f"{ features['punctuation_marks'] } punctuation marks")
    print(f"{ features['spaces'] } spaces")
    print(f"{ features['digits'] } digits")


def take_features(arg: str) -> dict:
    """
    Analyze the text and count the occurrences of different types of
    characters:
    uppercase, lowercase, punctuation marks, spaces, and digits.

    Args:
        arg (str): The input string to analyze.

    Returns:
        dict: A dictionary with the counts of different types of characters.
    """
    string_features = {
        'upper_cases': 0,
        'lower_cases': 0,
        'punctuation_marks': 0,
        'spaces': 0,
        'digits': 0
    }
    for letter in arg:
        if letter.isupper() is True:
            string_features['upper_cases'] += 1
        elif letter.islower() is True:
            string_features['lower_cases'] += 1
        elif letter in '!”#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
            string_features['punctuation_marks'] += 1
        elif letter.isdigit() is True:
            string_features['digits'] += 1
        elif letter == " ":
            string_features['spaces'] += 1
    return string_features


def main():
    """
    Main function that orchestrates the argument checking, feature extraction,
    and output of results.
    """
    try:
        args = sys.argv[1:]
        check_args(args)
        taken_features = take_features(args[0])
        print_features(taken_features)
    except Exception as msg:
        print(msg)


if __name__ == ("__main__"):
    main()
