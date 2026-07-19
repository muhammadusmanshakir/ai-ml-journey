try:
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    result=num1/num2

except ZeroDivisionError:
    print("Cannot be divided by zero!")

except ValueError:
    print("Enter valid numbers!")

else:
    print("Result: ",result)
finally:
    print("Calculator closed!")
    

