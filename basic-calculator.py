# Basic Calculator Program

# Get the first number from the user
num1 = float(input("Enter the first number: "))

# Get the second number from the user
num2 = float(input("Enter the second number: "))

# Get the operation from the user
operator = input("Enter the operation (+, -, *, /): ")

# Perform the calculation based on the operator
if operator == '+':
    result = num1 + num2
    print(f"{num1} {operator} {num2} = {result}")
elif operator == '-':
    result = num1 - num2
    print(f"{num1} {operator} {num2} = {result}")
elif operator == '*':
    result = num1 * num2
    print(f"{num1} {operator} {num2} = {result}")
elif operator == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"{num1} {operator} {num2} = {result}")
else:
    print("Error: Invalid operator. Please use +, -, *, or /.")
