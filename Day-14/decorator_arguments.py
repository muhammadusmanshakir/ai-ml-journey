def decorator(func):
    def wrapper(name):
        print("Starting-----")
        func(name)
        print("Ending---")

    return wrapper

@decorator
def greet(name):
    print("Hello!",name)

greet("Usman")

