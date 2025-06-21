
full_name = input("Enter your full name: ").strip().title()


while True:
    try:
        age = int(input("Enter your age: "))
        if 5 <= age <= 120:
            break
        else:
            print("Age must be between 5 and 120.")
    except ValueError:
        print("Please enter a valid number for age.")


while True:
    gender = input("Enter your gender (male/female): ").strip().lower()
    if gender in ["male", "female"]:
        break
    else:
        print("Gender must be 'male' or 'female'.")


while True:
    try:
        gpa = float(input("Enter your GPA (0.0 - 4.0): "))
        if 0.0 <= gpa <= 4.0:
            break
        else:
            print("GPA must be between 0.0 and 4.0.")
    except ValueError:
        print("Please enter a valid number for GPA.")


pronoun = "he" if gender == "male" else "she"

print("\n\n\tWelcome, " + full_name + "! 🎓\n")  # ترحيب باستخدام escape sequences و concatenation


print("Your name in lowercase:", full_name.lower())
print("Your name in UPPERCASE:", full_name.upper())
print("Your name in Title Case:", full_name.title())


if age <= 18:
    print("Age Category: Student")
else:
    print("Age Category: Adult")


if gpa >= 3.5:
    print(f"{pronoun.title()} is an excellent student.")
elif gpa >= 2.0:
    print(f"{pronoun.title()} is doing fine.")
else:
    print(f"{pronoun.title()} needs improvement.")
