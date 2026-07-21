def even_numbers(limit):
    for num in range(2,limit+1,2):
        yield num

limit=int(input("Generate even numbers upto: "))

print("\nEven Numbers:")
print("="*20)

for number in even_numbers(limit):
    print(number)

