def calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2 if num2 != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
op=input("Enter operation (+, -, *, /): ")
result = calculator(a, b, op)
print(f"Result: {result}")


