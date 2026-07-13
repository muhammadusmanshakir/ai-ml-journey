num1=int(input("Enter frst number: "))
num2=int(input("Enter second number: "))
operator=input("Choose operator (+,-,*,/): ").strip()
if operator=="+":
    print("Result = ",num1+num2)
elif operator == "-":
      print("Result = ",num1-num2)
elif operator == "*":
       print("Result = ",num1*num2)
elif operator == "/":
        if num2!=0:
         print("Result = ",num1/num2)
        else:
             print("Cannot divide by zero.")
else:
     print("Invalid operator")