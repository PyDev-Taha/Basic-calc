num1=float(input("Enter First number:"))
op=input("Enter operator:")
num2=float(input("Enter second number:"))

if op== "+":
    print("Sum is", num1 + num2)
elif op== "-":
    print("Subtraction is", num1 - num2)
elif op=="*":
    print("Multiplication is", num1 * num2)
elif op== "/":
    print("Division is ", num1 / num2)
elif op=="%":
    print(num1 % num2)
elif op=="**":
    print(num1 ** num2)

else:
    print("Invalid Operator")
