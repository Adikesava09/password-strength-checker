# Password Strength Checker
# Cyber Security Mini Project using Python

import re

def check_password_strength(password):
    score = 0
    remarks = []

    # Check minimum length
    if len(password) >= 8:
        score += 1
    else:
        remarks.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        remarks.append("Add at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        remarks.append("Add at least one lowercase letter.")

    # Check for digits
    if re.search(r"[0-9]", password):
        score += 1
    else:
        remarks.append("Add at least one number.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        remarks.append("Add at least one special character.")

    # Determine strength level
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Medium"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength, remarks


# Main Program
print("=== Password Strength Checker ===")
password = input("Enter a password to test: ")

strength, remarks = check_password_strength(password)

print(f"\nPassword Strength: {strength}")

if remarks:
    print("\nSuggestions to Improve:")
    for remark in remarks:
        print(f"- {remark}")
else:
    print("Excellent! Your password meets all recommended security rules.")
