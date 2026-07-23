import re
import json

print("=" * 50)
print("      User Information Validator")
print("=" * 50)

while True:

    while True:
        name = input("Enter your full name: ").strip()

        if re.match(r"^[A-Za-z ]+$", name):
            print("✅ Valid Name")
            break
        else:
            print("❌ Invalid Name. Please enter letters only.")

    while True:
        email = input("Enter your email: ").strip()

        if re.match(r"^[A-Za-z0-9._]+@[a-zA-Z]+\.[a-zA-Z]{2,}$", email):
            print("✅ Valid Email")
            break
        else:
            print("❌ Invalid Email. Try again.")

    while True:
        phone = input("Enter your phone number: ").strip()

        if re.match(r"^\d{11}$", phone):
            print("✅ Valid Phone Number")
            break
        else:
            print("❌ Invalid Phone Number. Enter exactly 11 digits.")

    while True:
        age = input("Enter your age: ").strip()

        if re.match(r"^\d+$", age):
            age = int(age)

            if 1 <= age <= 120:
                print("✅ Valid Age")
                break
            else:
                print("❌ Age must be between 1 and 120.")
        else:
            print("❌ Invalid Age. Enter numbers only.")

    print("\n" + "=" * 50)
    print("        User Information Summary")
    print("=" * 50)

    print(f"Name : {name}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    print(f"Age  : {age}")

    choice = input("\nDo you want to save the data? (y/n): ").strip().lower()

    if choice == "y":
        user_data = {
            "name": name,
            "email": email,
            "phone": phone,
            "age": age
        }

        with open("user_data.json", "w") as file:
            json.dump(user_data, file, indent=4)

        print("✅ Data saved successfully!")

    else:
        print("ℹ️ Data not saved.")

    again = input("\nDo you want to validate another user? (y/n): ").strip().lower()

    if again != "y":
        print("\nThank you for using User Information Validator!")
        print("Goodbye! 👋")
        break