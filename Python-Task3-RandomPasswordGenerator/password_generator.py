# Random Password Generator - Beginner Tier (Command-Line Version)

import random
import string

MINIMUM_LENGTH = 8

# Maps the menu number to a short name and its characters.
CHARACTER_SETS = {
    "1": ("Uppercase letters", string.ascii_uppercase),
    "2": ("Lowercase letters", string.ascii_lowercase),
    "3": ("Numbers", string.digits),
    "4": ("Symbols", string.punctuation),
}

VALID_OPTIONS = ("1", "2", "3", "4")


def get_password_length():
    """Ask for the password length until a valid number is entered.

    The length must be a whole number of at least 8 characters.
    """
    while True:
        user_input = input("Enter password length (minimum 8): ")

        try:
            # int() turns the text into a whole number.
            # If the text is not a number, Python raises a ValueError.
            length = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if length < MINIMUM_LENGTH:
            print("Invalid length. Password length must be at least 8 characters.")
        else:
            return length


def get_character_types():
    """Ask which character types to include until the selection is valid.

    Returns the selected menu options as a list, for example ["1", "3"].
    Duplicates are ignored and at least 2 different types are required.
    """
    while True:
        print()
        print("Select the character types you want to include:")
        print()
        print("1. Uppercase letters (A-Z)")
        print("2. Lowercase letters (a-z)")
        print("3. Numbers (0-9)")
        print("4. Symbols (!@#$%^&*...)")
        print()
        print("Enter your choices separated by spaces. Example: 1 2 3 4")

        user_input = input("Enter your choices separated by spaces: ")

        # split() breaks the text into separate words, so "1 2 3" becomes
        # ["1", "2", "3"].
        choices = user_input.split()
        selected_types = []
        has_invalid_option = False

        for choice in choices:
            if choice not in VALID_OPTIONS:
                has_invalid_option = True
                break
            if choice not in selected_types:
                # Ignore duplicates, so "1 1 2 2" becomes ["1", "2"].
                selected_types.append(choice)

        if has_invalid_option:
            print("Invalid selection. Please choose only options 1, 2, 3, or 4.")
        elif len(selected_types) < 2:
            print("Please select at least 2 character types.")
        else:
            return selected_types


def generate_password(length, selected_types):
    """Build a random password using only the selected character types.

    Every selected type is placed in the password first, so the password
    always contains at least one character of each type. The remaining
    positions are filled from the combined pool of selected characters.
    The result is shuffled so the characters are not predictable.
    """
    password_characters = []

    # One character from every selected type guarantees the rules are met.
    for option in selected_types:
        characters = CHARACTER_SETS[option][1]
        password_characters.append(random.choice(characters))

    # Join the selected sets into one pool for the remaining positions.
    all_characters = "".join(CHARACTER_SETS[option][1] for option in selected_types)

    for _ in range(length - len(password_characters)):
        password_characters.append(random.choice(all_characters))

    # Shuffle so the required characters are not always in the same places.
    random.shuffle(password_characters)

    return "".join(password_characters)


def main():
    print("========================================")
    print("     RANDOM PASSWORD GENERATOR")
    print("========================================")

    length = get_password_length()
    selected_types = get_character_types()

    while True:
        password = generate_password(length, selected_types)

        print()
        print("Character types used:")
        for option in selected_types:
            print("- {}".format(CHARACTER_SETS[option][0]))
        print("Length: {} characters".format(len(password)))
        print("Generated Password: {}".format(password))

        # Keep asking until the answer is clearly yes or no.
        while True:
            answer = input("Do you want to generate another password? (y/n): ").strip().lower()

            if answer == "y":
                # Generate another password without restarting the program.
                break
            elif answer == "n":
                print()
                print("Thank you for using the Random Password Generator!")
                return
            else:
                print("Invalid input. Please enter y or n.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        # The program still ends cleanly if input ends or Ctrl+C is pressed.
        print()
        print("Thank you for using the Random Password Generator!")