import sys


def init_morse():
    """
    Initializes and returns a dictionary mapping letters, digits, and spaces
    to their Morse code equivalents.

    Returns:
        dict: A dictionary where keys are alphanumeric characters and space,
        and values are Morse code representations.
    """
    morse_dict = {
                    ' ': '/ ',
                    'A': '.-',
                    'B': '-...',
                    'C': '-.-.',
                    'D': '-..',
                    'E': '.',
                    'F': '..-.',
                    'G': '--.',
                    'H': '....',
                    'I': '..',
                    'J': '.---',
                    'K': '-.-',
                    'L': '.-..',
                    'M': '--',
                    'N': '-.',
                    'O': '---',
                    'P': '.--.',
                    'Q': '--.-',
                    'R': '.-.',
                    'S': '...',
                    'T': '-',
                    'U': '..-',
                    'V': '...-',
                    'W': '.--',
                    'X': '-..-',
                    'Y': '-.--',
                    'Z': '--..',
                    '1': '.----',
                    '2': '..---',
                    '3': '...--',
                    '4': '....-',
                    '5': '.....',
                    '6': '-....',
                    '7': '--...',
                    '8': '---..',
                    '9': '----.',
                    '0': '-----',
    }
    return morse_dict


def check_args(args: list):
    """
    Validates that the program receives exactly one argument and that all
    characters in the argument are either alphanumeric or a space. Raises
    an exception if any invalid argument is found.

    Args:
        args (list): List of command-line arguments.

    Raises:
        Exception: If the argument count is not 1 or if the argument contains
        non-alphanumeric characters.
    """
    if args.__len__() != 1:
        raise Exception('AssertionError: the arguments are bad')
    for letter in str(args[0]):
        if letter != ' ' and letter.isalnum() is False:
            raise Exception('AssertionError: the arguments are bad')


def print_encoded_morse(NESTED_MORSE: dict, argument: str):
    """
    Converts the given argument string to its corresponding Morse code and
    prints it.

    Args:
        NESTED_MORSE (dict): Dictionary containing Morse code mappings.
        argument (str): The string to be converted to Morse code.

    Example:
        >>> print_encoded_morse({'A': '.-', 'B': '-...'}, 'AB')
        .- -...
    """
    for letter in argument:
        if letter == ' ':
            print(' ', end='')
        else:
            print(f'{ NESTED_MORSE[letter.upper()] }', end='')
    print()


def main():
    """
    Main function that runs the program. It checks command-line arguments,
    initializes the Morse dictionary, and prints the encoded Morse code.
    """
    try:
        args = sys.argv[1:]
        check_args(args)
        NESTED_MORSE = init_morse()
        print_encoded_morse(NESTED_MORSE, args[0])
    except Exception as name:
        print(name)


if __name__ == ("__main__"):
    main()
