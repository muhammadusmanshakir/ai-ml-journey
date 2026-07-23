import re
text=input("Enter a sentence: ")
result=re.findall(r"\s+",text)
print(result)
