# LCM(Least Common Multiple) 

#Basic Method
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# LCM nikalne ke liye hum GCD ka use karenge
def compute_gcd(a, b):
    while b:
        a, b = b, a % b
    return a    
gcd = compute_gcd(num1, num2)
lcm = (num1 * num2) // gcd  # LCM ka formula hai
print("LCM of", num1, "and", num2, "is", lcm)

# Using math module
import math
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
lcm = (num1 * num2) // math.gcd(num1, num2)  # math.gcd function use kar rahe hain
print("LCM of", num1, "and", num2, "is", lcm)   

#Using GCD Formula (Mathematical)
import math
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
gcd = math.gcd(num1, num2)

# Calculate LCM using formula
lcm = (num1 * num2) // gcd  # Using // for integer division

print(f"GCD of {num1} and {num2} is {gcd}")
print(f"LCM of {num1} and {num2} is {lcm}")