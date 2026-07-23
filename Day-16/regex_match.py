import re
text="Python programming is fun."
word=input("Enter a word:")
match=re.match(word,text,re.I)
if match:
    print("Match Found!")
    print("Matched Word:", match.group())
    print("Starts at:", match.start())
    print("Ends at:", match.end())
else:
    print("No Match!")
