import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Scoring
    score = 5 - sum([length_error, digit_error, uppercase_error, lowercase_error, symbol_error])

    # Evaluate strength
    if score == 5:
        return "Strong"
    elif 3 <= score < 5:
        return "Okay"
    else:
        return "Weak"

# Example usage
password = input("Enter your password: ")
strength = check_password_strength(password)
print(f"Password Strength: {strength}")
