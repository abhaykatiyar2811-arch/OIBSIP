# BMI Calculator (Python Task 2 - Beginner Tier)

A simple command-line BMI (Body Mass Index) calculator written in Python 3.

## Project Objective

The program asks the user for their weight and height, calculates the BMI,
classifies the result into a standard health category, and displays the result
rounded to 2 decimal places. Invalid input is handled with helpful messages
instead of crashing.

## Features

- Prompts for weight in kilograms (kg).
- Prompts for height in meters (m).
- Calculates BMI with the standard formula.
- Shows the BMI to 2 decimal places.
- Shows the matching BMI category.
- Validates input: non-numeric text, negative values, and zero values.
- Re-asks the question until valid input is given.

## BMI Formula

```text
BMI = weight / (height ** 2)
```

Example: weight = 70 kg, height = 1.75 m

```text
BMI = 70 / (1.75 ** 2) = 22.86
```

## BMI Categories

| BMI Range      | Category    |
| -------------- | ----------- |
| Less than 18.5 | Underweight |
| 18.5 - 24.9    | Normal      |
| 25 - 29.9      | Overweight  |
| 30 or greater  | Obese       |

The code uses these conditions, so the boundaries work correctly:

```text
BMI < 18.5  -> Underweight
BMI < 25    -> Normal
BMI < 30    -> Overweight
BMI >= 30   -> Obese
```

## How to Run

Python 3 is required. Open a terminal in the project directory
(`OIBSIP/Python-Task2-BMICalculator`) and run:

```bash
python bmi_calculator.py
```

On some systems the command may be:

```bash
python3 bmi_calculator.py
```

## Example Output

```text
================================
      BMI CALCULATOR
================================

Enter your weight in kilograms (kg): 70
Enter your height in meters (m): 1.75

Your BMI is: 22.86
Category: Normal

Thank you for using the BMI Calculator!
```

## Validation Examples

```text
Enter your weight in kilograms (kg): abc
Invalid input. Please enter a numeric value.
Enter your weight in kilograms (kg): -70
Invalid input. Weight must be greater than 0.
Enter your height in meters (m): 0
Invalid input. Height must be greater than 0.
```

## Technologies Used

- Python 3
- `input()` for user input
- Basic arithmetic
- `if` / `elif` / `else` conditional statements
- `try` / `except` for handling non-numeric input

No external libraries are used.

## Project Structure

```text
OIBSIP/
└── Python-Task2-BMICalculator/
    ├── bmi_calculator.py
    └── README.md
```

## Note

This is the Beginner Tier. GUI (Tkinter / PyQt5), Matplotlib charts, SQLite, CSV
storage, trend graphs, login systems, web apps, and external APIs are
intentionally not included.

This calculator is for educational purposes and is not medical advice.