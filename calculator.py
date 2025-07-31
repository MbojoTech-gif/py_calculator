# Basic Calculator Program
# This program performs basic arithmetic operations: addition, subtraction, multiplication, and division.

# Ask for two numbers and an operation....
print("Welcome to the Basic Calculator!")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /, //, %): ")

# Perform the calculation based on the operation
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
elif operation == '//':
    if num2 != 0:
        result = num1 // num2
        print(f"{num1} // {num2} = {result}")
    else:
        print("Error: Floor division by zero is not allowed.")
elif operation == '%':
    if num2 != 0:
        result = num1 % num2
        print(f"{num1} % {num2} = {result}")
    else:
        print("Error: Modulo by zero is not allowed.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")
