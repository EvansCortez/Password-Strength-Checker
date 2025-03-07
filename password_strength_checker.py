import re

def check_password_strength(password):
    # Define criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Check for common weak passwords
    common_passwords = ["123456", "password", "12345678", "qwerty", "12345", "123456789", "letmein", "1234567", "football", "iloveyou"]
    is_common = password.lower() in common_passwords

    # Calculate strength score
    strength_score = 0
    if length_criteria:
        strength_score += 1
    if uppercase_criteria:
        strength_score += 1
    if lowercase_criteria:
        strength_score += 1
    if digit_criteria:
        strength_score += 1
    if special_char_criteria:
        strength_score += 1
    if is_common:
        strength_score = 0  # If it's a common password, set strength to 0

    # Determine strength level
    if strength_score == 0:
        return "Very Weak (Common Password)"
    elif strength_score <= 2:
        return "Weak"
    elif strength_score == 3:
        return "Moderate"
    elif strength_score == 4:
        return "Strong"
    elif strength_score == 5:
        return "Very Strong"

def main():
    print("Password Strength Checker")
    while True:
        password = input("Enter a password to check its strength (or type 'exit' to quit): ")
        if password.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        strength = check_password_strength(password)
        print(f"Password Strength: {strength}")

if __name__ == "__main__":
    main()