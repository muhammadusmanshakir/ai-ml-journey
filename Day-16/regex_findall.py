import re
text="""
Python is powerful.
Python is easy.
I love Python.
Python is everywhere.
"""
word = input("Enter word to search: ")
matches=re.findall(word,text,re.I)
if matches:
    print("Matches Found:")
    print(matches)

    print("Total Matches:", len(matches))
else:
    print("Match not found!")

    