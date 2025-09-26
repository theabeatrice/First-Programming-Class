# Owner Statement: Thea Labuntog thl1733@rit.edu
'''
Assignment 2: Menu-Driven Program with Input Checking
This program presents a menu of options (1, 2, or 3) to the user and allows them to select an option until they decide to quit.
'''

def is_valid_choice(choice):
    # Check if the user's choice is valid (1, 2, or 3)
    return choice in ['1', '2', '3']

def main():
    # Main function to run the menu program: greeting, usage message, and menu loop
    print("Hello! Welcome to Thea's Program!")
    print("This program will present you with a menu of options (1, 2, or 3).")
    print("You can repeat as many times as you like. To exit, enter 'q'.")

    # Menu Loop
    while True:
        print("\nMenu:")
        print("1. Option 1")
        print("2. Option 2")
        print("3. Option 3")
        print("q. Quit")

        choice = input("Please enter your choice (1, 2, 3, or q to quit): ")

        # Process the user's choice and Input Checking for valid input
        if choice == 'q':
            print("Exiting the program. Goodbye!")
            break
        elif is_valid_choice(choice):
            print(f"You selected option {choice}.")
            if choice == "1":
                print("You chose Option 1.")
            elif choice == "2":
                print("You chose Option 2.")
            elif choice == "3":
                print("You chose Option 3.")
        else:
            print("Invalid choice. Please enter 1, 2, 3, or q.")

if __name__ == "__main__":
    main()

'''GenAI Tool Analysis: I used Microsoft CoPilot and Google Gemini to provide me with examples of menu code and for input checking.
I analyzed the code provided by both and selected CoPilot's code as it made more sense to me and was easier to understand.
Analysis of each tool's code is provided below.

#Microsoft CoPilot Example Code
def display_menu():
    print("\n=== Main Menu ===")
    print("1. Say Hello")
    print("2. Add Two Numbers")
    print("3. Exit")

def get_valid_choice():
    while True:
        choice = input("Enter your choice (1-3): ")
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("❌ Invalid input. Please enter a number between 1 and 3.")

def say_hello():
    name = input("What's your name? ")
    print(f"👋 Hello, {name}!")

def add_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"✅ Result: {num1} + {num2} = {num1 + num2}")
    except ValueError:
        print("❌ Invalid number. Please enter numeric values.")

def main():
    while True:
        display_menu()
        choice = get_valid_choice()

        if choice == 1:
            say_hello()
        elif choice == 2:
            add_numbers()
        elif choice == 3:
            print("👋 Goodbye!")
            break

if __name__ == "__main__":
    main()

Microsoft CoPilot Tool Analysis:
I found CoPilot's code to be very user-friendly and easy to follow! The use of emojis made the interaction more engaging and visually appealing.
The functions were well-defined, making it easy to understand the flow of the program. The input validation was straightforward, making sure that users could only enter valid choices.
Overall, I appreciated the clarity and simplicity of CoPilot's example in creating a menu-driven program with input checking.

#Google Gemini Example Code
#Menu Code Example
def main_menu():
    """Displays the main menu options."""
    print("\n--- Welcome to My Program! ---")
    print("1. View your profile")
    print("2. Change your password")
    print("3. Log out")

def handle_user_choice():
    """Handles the user's choice."""
    while True:
        main_menu()
        choice = input("Please enter your choice (1-3): ")
        
        if choice == '1':
            print("Accessing profile...")
            # Code to view profile
            break  # Exit the loop after a valid choice
        elif choice == '2':
            print("Redirecting to password change screen...")
            # Code to change password
            break
        elif choice == '3':
            print("Logging out...")
            # Code to log out
            break
        else:
            print("Invalid choice. Please try again.")

# Call the function to run the menu
handle_user_choice()

#Input Checking Example: Checking for Valid Integer
def get_user_age():
    """Prompts the user for their age and validates the input."""
    while True:
        try:
            age = int(input("Please enter your age: "))
            if age > 0 and age < 120:  # Check for a reasonable age range
                return age
            else:
                print("Age must be between 1 and 120. Please try again.")
        except ValueError:
            print("That's not a valid number. Please enter a number for your age.")

# Call the function
user_age = get_user_age()
print(f"You entered the age: {user_age}")

#Input Checking Example: Checking for Specific Format
def confirm_action():
    """Confirms an action with a yes/no response."""
    while True:
        response = input("Are you sure you want to proceed? (yes/no): ").lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Please answer with 'yes' or 'no'.")

# Call the function
if confirm_action():
    print("Proceeding with the action...")
else:
    print("Action cancelled.")

Google Gemini Tool Analysis:
While Gemini's code was functional and I appreciated the clarity its comments brought, I found it to be less engaging compared to CoPilot's version.
It provided more of an explanation, like providing input checking examples for valid integers and checking for specific formats, but it got overly complicated for a simple menu program.

GenAI Statement: My code and answers are not a production of GenAI.''' 