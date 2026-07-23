import re

text = input("Enter a sentence: ")

match = re.search(r"Python$", text, re.IGNORECASE)

if match:
    print("Sentence ends with Python")
else:
    print("Sentence does not end with Python")
    