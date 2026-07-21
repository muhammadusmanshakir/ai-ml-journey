import time
def timer(func):
    def wrapper():
        start=time.time()
        func()
        end=time.time()

        print(f"Execution time: {end-start:.2f} seconds")
    return wrapper

@timer
def task():
    print("Processing---")
    time.sleep(2)
    print("Task completed!")

task()

