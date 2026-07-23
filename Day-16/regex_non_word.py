import re
text=input("Enter a sentence: ")
result=re.findall(r"\W+",text)
print(result)
