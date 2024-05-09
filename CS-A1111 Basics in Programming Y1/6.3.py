CHARACTER_TO_MORSE_STRING = {'0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                             '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                             'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
                             'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                             'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
                             'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'}


def plaintext_to_morse(text):
    """
    Converts 'text' to morse code. Replaces unknown characters with '???' silently.

    Parameter text: str

    returns: str of morse codes separated by spaces

    E.g.
    > plaintext_to_morse("ABC0")
    > .- -... -.-. -----

    > plaintext_to_morse("A&C%")
    > .- ??? -.-. ???
    """
    # write your code here
    teksti = text.upper()
    code = ''
    for x in teksti:
        if x in CHARACTER_TO_MORSE_STRING:
            code += CHARACTER_TO_MORSE_STRING[x]
        else:
            code += '???'
        code += ' '

    return code.strip()


def morse_to_plaintext(morsecode):
    """
    Converts 'morsecode' to plaintext. Replaces unknown morse strings with '?' silently.

    Parameter text: str of morse code strings separated by spaces

    returns: str

    E.g.
    > morse_to_plaintext(".- -... -.-. -----")
    > ABC0

    > morse_to_plaintext(".- .-.-. -.-. ---.--")
    > A?C?
    """
    # write your code here
    koodi = morsecode.split(' ')
    ret = ''

    for o in koodi:
        if o != ' ':
            if o in CHARACTER_TO_MORSE_STRING.values():
                for c in CHARACTER_TO_MORSE_STRING.items():
                    if c[1] == o:
                        ret += c[0]
            else:
                ret += '?'

    return ret


def main():
    print("This program converts text to international morse code and vice versa")
    print("Type\n'mt' to convert morse code to plaintext\n'tm' to convert plaintext to morse code")

    i = input()
    if i == 'mt':
        text = input("Enter the morse code to convert:\n")
        print("Your morse code as plaintext:")
        print(morse_to_plaintext(text))
    elif i == 'tm':
        text = input("Enter the text to convert:\n")
        print("Your text as morse code:")
        print(plaintext_to_morse(text))
    else:
        print("Unknown choice. The program ends.")


main()
