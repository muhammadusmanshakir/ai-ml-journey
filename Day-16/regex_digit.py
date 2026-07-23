import re
text=input("Enter a sentence: ")
numbers=re.findall(r"\d+",text)
if numbers:
    print("Numbers found:",numbers)

else:
    print("Numbers not found")
