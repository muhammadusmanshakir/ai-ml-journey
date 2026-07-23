import re
text=input("Enter a sentence: ")
result=re.findall(r"\w+",text)
print(result)
