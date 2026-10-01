# Random Password Generator (Python Task 3 - Beginner Tier)

A simple command-line random password generator written in Python 3.

## Project Objective

The program asks the user for a password length and which character types to
include, then generates a random password that satisfies all of those rules.
The user can generate as many passwords as they like without restarting the
program. Invalid input is handled with helpful messages instead of crashing.

## Features

- Asks for the desired password length (minimum 8 characters).
- Shows a menu of character types and reads the user's choice.
- Requires at least 2 different character types.
- Generates a password with exactly the requested length.
- Guarantees at least one character from every selected type.
- Fills the remaining positions from the combined selected character pool.
- Shuffles the result so the characters are not in predictable positions.
- Validates input: non-numeric length, length below 8, invalid options,
  duplicate options, and only one character type.
- Re-asks the question until valid input is given.
- Generates another password on request without restarting the program.
- Exits gracefully when the user answers `n`.

## Technologies Used

- Python 3
- `random` for random choices and shuffling
- `string` for the built-in character sets
- `input()` for user input
- `try` / `except` for handling non-numeric input
- `while` loops for re-asking after invalid input
- `if` / `elif` / `else` conditional statements

No external libraries are used.

## How the Generator Works

1. The user enters a password length of at least 8.
2. The user selects 2, 3, or 4 character types from the menu.
3. The program picks **one random character from each selected type**. This
   guarantees the password contains every type the user asked for.
4. The remaining positions are filled with random characters taken from the
   combined pool of all selected types.
5. `random.shuffle()` shuffles the characters so the guaranteed characters
   are not always in the same positions.
6. The characters are joined into one string and displayed.

## Supported Character Types

| Option | Character Type  | Python Constant          |
| ------ | --------------- | ------------------------ |
| 1      | Uppercase (A-Z) | `string.ascii_uppercase` |
| 2      | Lowercase (a-z) | `string.ascii_lowercase` |
| 3      | Numbers (0-9)   | `string.digits`          |
| 4      | Symbols         | `string.punctuation`     |

## Input Validation Rules

| Situation                    | Message                                                | Action |
| ---------------------------- | ------------------------------------------------------ | ------ |
| Length is not a number       | `Invalid input. Please enter a valid number.`           | Ask again |
| Length is below 8            | `Invalid length. Password length must be at least 8 characters.` | Ask again |
| Choice is not 1, 2, 3 or 4   | `Invalid selection. Please choose only options 1, 2, 3, or 4.` | Ask again |
| Fewer than 2 unique types    | `Please select at least 2 character types.`             | Ask again |
| Answer is not `y` or `n`     | `Invalid input. Please enter y or n.`                   | Ask again |

Duplicate choices are ignored before counting types, so `1 1 2 2` is treated
the same as `1 2` and correctly counts as 2 different character types.

## How to Run

Python 3 is required. Open a terminal in the project directory
(`OIBSIP/Python-Task3-RandomPasswordGenerator`) and run:

```bash
python password_generator.py
```

On some systems the command may be:

```bash
python3 password_generator.py
```

## Example Usage / Output

```text
========================================
     RANDOM PASSWORD GENERATOR
========================================
Enter password length (minimum 8): 12

Select the character types you want to include:

1. Uppercase letters (A-Z)
2. Lowercase letters (a-z)
3. Numbers (0-9)
4. Symbols (!@#$%^&*...)

Enter your choices separated by spaces. Example: 1 2 3 4
Enter your choices separated by spaces: 1 2 3 4

Character types used:
- Uppercase letters
- Lowercase letters
- Numbers
- Symbols
Length: 12 characters
Generated Password: K8@pL2#xQ7$m

Do you want to generate another password? (y/n): y
```

## Validation Examples

```text
Enter password length (minimum 8): 7
Invalid length. Password length must be at least 8 characters.
Enter password length (minimum 8): abc
Invalid input. Please enter a valid number.
Enter your choices separated by spaces: 1
Please select at least 2 character types.
Enter your choices separated by spaces: 1 5
Invalid selection. Please choose only options 1, 2, 3, or 4.
```

## Project Structure

```text
OIBSIP/
└── Python-Task3-RandomPasswordGenerator/
    ├── password_generator.py
    └── README.md
```

## Functions in `password_generator.py`

| Function                    | Purpose |
| --------------------------- | ------- |
| `get_password_length()`     | Asks for the length until a valid number of at least 8 is entered. |
| `get_character_types()`     | Asks for the character types until a valid selection of 2 or more is entered. |
| `generate_password()`       | Returns a random password that meets the selected rules. |
| `main()`                    | Runs the program flow and handles generate-again / exit. |

## Note

This is the Beginner Tier. Tkinter / PyQt5 GUI, `pyperclip` clipboard support,
databases, CSV storage, password history, strength meters, web apps, APIs,
login systems, and `secrets`-based cryptographic generation are intentionally
not included.

This project is for educational purposes only.