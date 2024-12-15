import phonenumbers
import os

def is_valid_phone_number(number):
    try:
        parsed = phonenumbers.parse(number, None)
        return phonenumbers.is_valid_number(parsed)
    except phonenumbers.NumberParseException:
        return False

def print_colored(message, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "reset": "\033[0m"
    }
    return f"{colors.get(color, colors['reset'])}{message}{colors['reset']}"

def main():
    if not os.path.exists("number.txt"):
        print("The file 'number.txt' was not found. Make sure it is in the same folder as this script.")
        return

    with open("number.txt", "r") as file:
        numbers = file.readlines()

    numbers = [number.strip() for number in numbers if number.strip()]

    if not numbers:
        print("No phone numbers found in 'number.txt'.")
        return

    print("\n--- Starting phone number validation ---\n")

    for number in numbers:
        if is_valid_phone_number(number):
            print(print_colored(f"[VALID] The phone number is valid: {number}", "green"))
        else:
            print(print_colored(f"[INVALID] The phone number is invalid: {number}", "red"))

    print("\n--- Phone number validation completed ---")

if __name__ == "__main__":
    main()
