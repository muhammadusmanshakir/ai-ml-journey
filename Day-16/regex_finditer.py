import re

text = """
Python is powerful.
Python is easy.
I love Python.
Python is everywhere.
"""
word = input("Enter word: ")
matches = re.finditer(word, text,re.I)
found=False
for match in matches:
    found=True
    print("Matched Word:", match.group())
    print("Starts at :", match.start())
    print("Ends at   :", match.end())
    print("-" * 30)

if not found:
    print("No match found")
    