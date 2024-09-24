import re

def check_password_strength(password):
    """Assess the strength of the provided password."""
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'\d', password) is not None
    special_character_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Count the number of criteria met
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_character_criteria])

    # Assess strength based on criteria met
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength

def main():
    """Main function to run the password complexity checker."""
    password = input("Enter a password to assess its strength: ").strip()
    strength = check_password_strength(password)
    print(f"Password Strength: {strength}")

if _name_ == "_main_":
    main()