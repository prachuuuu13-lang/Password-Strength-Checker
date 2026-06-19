def has_sequential_characters(password):
    password_lower = password.lower()
    for i in range(len(password_lower) - 2):
        chunk = password_lower[i:i + 3]
        if (ord(chunk[2])-ord(chunk[1])) == 1 and (ord(chunk[1])-ord(chunk[0])) == 1:
            return True
    return False


def check_password(password):
    score = 0
    feedback = []
    if len(password) < 8:
        feedback.append(
            "Password is too short. It should be at least 8 characters long.")
    else:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append(
            "Password should contain at least one uppercase letter.")
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append(
            "Password should contain at least one lowercase letter.")
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Password should contain at least one digit.")
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    if any(c in special_characters for c in password):
        score += 1
    else:
        feedback.append(
            "Password should contain at least one special character.")
    if has_sequential_characters(password):
        score -= 1
        feedback.append("Password should not contain sequential characters.")
    return score, feedback


def rate_password(score):
    if score <= 1:
        return " very weak"
    elif score == 2:
        return "weak"
    elif score == 3:
        return "moderate"
    elif score == 4:
        return "strong"
    else:
        return "very strong"


while True:
    password = input("Enter password to check (or type 'exit' to quit): ")
    if password.lower() == 'exit':
        print("Exiting the password checker. Goodbye!")
        break

    score, feedback = check_password(password)
    rating = rate_password(score)
    print(f"\nPassword Rating: {rating}")
    print(f"The Score your password had got: {score}/5")
    print("\nFeedback:")
    if feedback:
        for tip in feedback:
            print(f"- {tip}")
    else:
        print("- No feedback. Your password is strong!")
        print("- Your password is strong! Keep it up!")
