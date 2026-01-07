

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
# Method 1: Using temp variable
temp = a
a = b
b = temp
print(f"After swap: a={a}, b={b}")



# Method 2: Python way (without temp)
x, y = 15, 25
x, y = y, x
print(f"After swap: x={x}, y={y}")
