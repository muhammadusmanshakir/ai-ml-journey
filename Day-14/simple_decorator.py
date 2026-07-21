def decorator(func):

    def wrapper():
        print("Before function!")
        func()
        print("After function")

    return wrapper

def greet():
    print("Hello!")

greet=decorator(greet)
greet()
