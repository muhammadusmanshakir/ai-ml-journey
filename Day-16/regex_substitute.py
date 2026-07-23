import re
text=input("Enter a sentence: ")
new_text=re.sub(r"\d","#",text)
print(new_text)

