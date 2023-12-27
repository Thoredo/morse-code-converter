# fmt: off
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
# fmt: on

keep_going = True


def convert_to_morse_code(input):
    """
    Looks at users input and converts all characters it can to morse code.

    Args:
        input (str): The input we receive from the user

    Returns:
        str: Returns the converted input as more code string
    """
    result = ""
    for character in input:
        character = character.capitalize()
        if character != " " and character in MORSE_CODE_DICT:
            morse_char = MORSE_CODE_DICT[character]
            result += morse_char + " "
        # Adds extra space between words
        elif character == " ":
            result += " "
        else:
            unused_characters.add(character)
        return result


if __name__ == "__main__":
    while keep_going:
        unused_characters = set()

        user_input = input("What word or sentence do you want to convert? ")

        final_result = convert_to_morse_code(user_input)

        # Show user the results
        print(f"Your word or sentence in morse code is as follows: {final_result}")
        if len(unused_characters) > 0:
            print(
                "Some of your characters could not be translated, here is a "
                f"list: {unused_characters}"
            )

        repeat = input("Do you want to convert again? Type 'y' or 'n'\n")

        while repeat.lower() not in ("y", "n"):
            print("Invalid input. Please enter 'y' or 'no.")
            repeat = input("Do you want to convert again? Type 'y' or 'n'\n")

        # Stop program when user types 'n'
        if repeat.lower() == "n":
            keep_going = False
            print("Goodbye!")
