import re
text=input("Enter a sentence: ")
result=re.findall(r"\D+",text)
print(result)