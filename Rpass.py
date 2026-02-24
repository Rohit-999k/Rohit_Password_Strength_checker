#My First Project
import re

#Basic Passes List
basic_passwords = [
    "password", "123456", "12345678", "qwerty", 
    "abc123", "password123", "admin", "letmein"
]


def check_my_pass(password):
    score = 0
    feedback = []

    #1 Check length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Make password at least 8 characters long.")

    #2 Check uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter in password.")

    #3 Check lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter in password.")

    #4 Check numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    #5 Check special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    #6 Check common passwords
    if password.lower() in basic_passwords:
        feedback.append("This is a very common password.\nChoose better one.")
        score = 0

    #Strength Result
    if score >= 6:
        strength = " --- Very Strong ---"
    elif score >= 4:
        strength = "--- Strong ---"
    elif score >= 3:
        strength = "--- Medium ---"
    else:
        strength = "--- Weak ---"

    return strength, feedback


#my main program
if __name__ == "__main__":
    given_pass = input("Enter your password: ")
    strength, suggestions = check_my_pass(given_pass)

    print("\nPassword Strength:", strength)

    if suggestions:
        print("\nSuggestions to improve:")
        for val in suggestions:
            print("-", val)
        print()