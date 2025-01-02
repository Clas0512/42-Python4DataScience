import sys

def init_morse():
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
                    'V': '-.--',
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
    if args.__len__() != 1:
        raise Exception('AssertionError: the arguments are bad')
    for letter in str(args[0]):
        if letter != ' ' and letter.isalnum() == False:
            raise Exception('AssertionError: the arguments are bad')

def print_encoded_morse(NESTED_MORSE: dict, argument: str):
    for letter in argument:
        if letter == ' ':
            print(' ', end='')
        else:
            print(f'{ NESTED_MORSE[letter.upper()] }',end='')
    print()

def main():
    try:
        args = sys.argv[1:]
        check_args(args)
        NESTED_MORSE = init_morse()
        print_encoded_morse(NESTED_MORSE, args[0])
    except Exception as name:
        print(name)

if __name__ == ("__main__"):
    main()