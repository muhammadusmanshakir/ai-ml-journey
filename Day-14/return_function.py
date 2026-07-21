def  outer():
    def inner():
        print("Hello from inner function")
    return inner

message=outer()
message()

