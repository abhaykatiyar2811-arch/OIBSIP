# BMI Calculator - Beginner Tier (Command-Line Version)

def get_number(prompt):
    """Ask the user for a number and return it as a float.

    Keeps asking until a valid numeric value is entered.
    """
    while True:
        user_input = input(prompt)

        try:
            # float() turns the text into a number (for example "70.5").
            # If the text is not a number, Python raises a ValueError.
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_weight():
    """Ask for weight in kilograms. It must be greater than 0."""
    while True:
        weight = get_number("Enter your weight in kilograms (kg): ")

        if weight <= 0:
            print("Invalid input. Weight must be greater than 0.")
        else:
            return weight

def get_height():
    """Ask for height in meters. It must be greater than 0.

    A height of 0 is rejected so the program never divides by zero.
    """
    while True:
        height = get_number("Enter your height in meters (m): ")

        if height <= 0:
            print("Invalid input. Height must be greater than 0.")
        else:
            return height


def calculate_bmi(weight, height):
    """Calculate BMI using the formula: weight / (height ** 2)."""
    return weight / (height ** 2)


def classify_bmi(bmi):
    """Return the health category that matches the given BMI."""
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return category


def main():
    print("================================")
    print("      BMI CALCULATOR")
    print("================================")
    print()

    weight = get_weight()
    height = get_height()

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print()
    print("Your BMI is: {:.2f}".format(bmi))
    print("Category: {}".format(category))
    print()
    print("Thank you for using the BMI Calculator!")


if __name__ == "__main__":
    main()