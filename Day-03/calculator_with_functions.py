def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b!=0:
        return a/b
    else:
        print("Cannot divide by zero.")

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))   
operator=input("Choose operator (+,-,*,/): ")

if operator=="+":
    sum=add(num1,num2)
    print(f"The sum is: {sum}")
elif operator=="-":
     difference=subtract(num1,num2)
     print(f"The difference is: {difference}")
elif operator=="*":
    product=multiply(num1,num2)
    print(f"The product is: {product}")
elif operator=="/":
    division=divide(num1,num2)
    if division is not None:
     print(f"The division is: {division}")
else:
    print("Please enter valid operator!")





