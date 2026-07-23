import re
text=input("Enter names separated by comma,semicolon or spaces: ")
names=re.split(r"[,;\s]+",text)
print(names)

