import re
text=input("Enter a sentence: ")
result=re.findall(r"\S+",text)
print(result)
