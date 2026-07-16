fruits = ("Apple", "Banana", "Mango")
try:
    fruits[1]="Orange"
except TypeError:
    print("Tuples cannot be modified.")