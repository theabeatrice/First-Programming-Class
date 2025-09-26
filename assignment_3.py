'''
Thea Labuntog thl1733@rit.edu
ISCH-620 Assignment 3: Interactive Math Program
GenAI Statement: My code and answers are not a production of GenAI.
'''
import math


# --- input validation functions!

def is_valid_choice(choice):
    # check if the user's math program choice is valid (1-6 only since there's no 7th option)
    return choice in ['1', '2', '3', '4', '5', '6']

def is_valid_number(num):
    # check if the input is a valid number from 0 to 9
    return num in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# --- math functions!

# division 
def division():
    # get two numbers from the user and perform division
    num1 = (input("Enter a numerator from 0 to 9 (top number): "))
    num2 = (input("Enter a denominator from 0 to 9 (bottom number): "))
    if not is_valid_number(num1) or not is_valid_number(num2):
        print("Error: Invalid input. Try again!")
        return

    num1 = float(num1)
    num2 = float(num2)

    if num2 == 0:
        print("Error: Cannot divide by zero!")
    else: 
        result = float(num1) / float(num2)
        print(f"Result: {result}")

# minimum and maximum
def min_max():
    # get a list of numbers from the user and find the minimum and maximum
    num1 = input("Enter the first number (0-9): ")
    num2 = input("Enter the second number (0-9): ")
    num3 = input("Enter the third number (0-9): ")
    if not is_valid_number(num1) or not is_valid_number(num2) or not is_valid_number(num3):
        print("Error: Invalid input. Try again!")
        return

    num_list = [float(num) for num in (num1, num2, num3)]
    if not num_list:
        print("No numbers entered.")
    elif num1 == num2 == num3:
        print ("Only one number entered? Minimum and Maximum are the same.")
    else:
        minimum = min(num_list)
        maximum = max(num_list)
        print(f"Minimum: {minimum}, Maximum: {maximum}")

# modulo (remainder and quotient)
def modulo():
    # get two integers from the user and perform modulo operation
    num1 = (input("Enter the dividend (integer 0-9): "))
    num2 = (input("Enter the divisor (integer 0-9): "))
    if not is_valid_number(num1) or not is_valid_number(num2):
        print("Error: Invalid input. Try again!")
        return
    
    num1 = float(num1)
    num2 = float(num2)

    if num2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        remainder = num1 % num2
        quotient = num1 // num2
        print(f"Remainder: {remainder}, Quotient: {quotient}")

# floor and ceiling
def floor_ceiling():
    # get a number from the user and calculate floor and ceiling
    num1 = (input("Enter the numerator (top number 0-9): "))
    num2 = (input("Enter the denominator (bottom number 0-9): "))
    if not is_valid_number(num1) or not is_valid_number(num2):
        print("Error: Invalid input. Try again!")
        return
    
    num1 = float(num1)
    num2 = float(num2)

    if num2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        result = num1 / num2 
        floored = math.floor(result)
        ceiled = math.ceil(result)
        print(f"Floor: {floored}, Ceiling: {ceiled}")

# absolute value and rounding
def abs_round():
    # get a number from the user and calculate absolute value and rounded value
    num = (input("Enter a number (0-9): "))
    if not is_valid_number(num):
        print("Error: Invalid input. Try again!")
        return
    
    num = float(num)

    absolute = abs(num)
    rounded = round(num, 2) # rounding to 2 decimal places
    print(f"Absolute Value: {absolute}, Rounded Value to 2 decimals: {rounded}")

# math definitions based on python documentation
def math_definitions(): 
    print("Math Definitions:")
    print("Division (/) = Divides the number on the left by the number on the right.")
    print("Minimum (min) = The smallest value in a set of numbers.")
    print("Maximum (max) = The largest value in a set of numbers.")
    print("Modulo (%) = The remainder of a division operation.")
    print("Floor (math.floor) = The largest integer less than or equal to a given number.")
    print("Ceiling (math.ceil) = The smallest integer greater than or equal to a given number.")
    print("Absolute Value (abs) = The absolute value of a given number.")
    print("Rounding (round) = Rounds a number to a given precision.")


# --- main function to run the menu program: greeting, usage message, and menu loop!

def main():
    print("Hello! Welcome to the Math Program.")
    print("This program will present you with a menu of math options (1, 2, 3, 4, 5, 6).")
    print("You can repeat as many times as you like! To exit, enter 'Q/q'.")

    # menu Loop
    while True:
        print("\nMenu:")
        print("1. Division")
        print("2. Minimum and Maximum")
        print("3. Modulo (Remainder and Quotient)")
        print("4. Floor and Ceiling")
        print("5. Absolute Value and Rounding")
        print("6. Math Definitions")
        print("q. Quit")

        choice = input("Please enter your choice (1-6, or q to quit): ")

        # process user's choice
        if choice == 'q' or choice == 'Q':
            print("Exiting the math program. Goodbye!")
            break
        elif is_valid_choice(choice):
            print(f"You selected option {choice}.")
            if choice == "1":
                print("You chose Option 1: Division.")
                division()
            elif choice == "2":
                print("You chose Option 2: Minimum and Maximum.")
                min_max()
            elif choice == "3":
                print("You chose Option 3: Modulo (Remainder and Quotient).")
                modulo()
            elif choice == "4":
                print("You chose Option 4: Floor and Ceiling.")
                floor_ceiling()
            elif choice == "5":
                print("You chose Option 5: Absolute Value and Rounding.")
                abs_round()
            elif choice == "6":
                print("You chose Option 6: Math Definitions.")
                math_definitions()
        else:
            print("Don't have that option! Please try again, or Q/q to quit.")

if __name__ == "__main__":
    main()