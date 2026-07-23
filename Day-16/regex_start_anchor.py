import re

text = input("Enter a sentence: ")

match = re.search(r"^Python", text, re.IGNORECASE)

if match:
    print("Sentence starts with Python")
else:
    print("Sentence does not start with Python")