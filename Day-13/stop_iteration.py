numbers=[1,2]
iterator=iter(numbers)

try:
    while True:
        print(next(iterator))

except StopIteration:
    print("Iteration finished!")

    