def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(not c.isalnum() for c in password):
        score += 1

    levels = {
        1: "Very Weak",
        2: "Weak",
        3: "Medium",
        4: "Strong",
        5: "Very Strong"
    }

    return levels.get(score, "Very Weak")


if __name__ == "__main__":
    pw = input("Enter a password to test: ")
    print("Strength:", check_password_strength(pw))
