import re
text="Python programming is fun and powerful."
word=input("Enter a word to search for: ")
match=re.search(word,text,re.IGNORECASE)

if match:
    print("word found!")
    print("Matched word:",match.group())
    print("Starts at:",match.start())
    print("Ends at: ",match.end())
else:
    print("word not found!")

