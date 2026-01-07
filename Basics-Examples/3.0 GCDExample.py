#GCD matlab koi do number common divisor jo dono number ko divide kar sake aur divisor sabse bada ho.
# Example: 12 and 8 ka GCD 4 hai kyuki 4 dono ko divide kar sakta hai aur 4 se bada koi bhi number dono ko divide nahi kar sakta.

# aur gcd har baar 8 sai kam ya barabar hota hai. uper jo exapmle diya hai usmai 12 aur 8 ka gcd 8 se chota hi hoga.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))      
smallest = min(num1, num2)                    # dono mai se chota number le lo min() function se
gcd = 1                                       # gcd ko initialize kar do 1 se
for i in range(1, smallest + 1):             #smallest+1 matlab 
    if num1 % i == 0 and num2 % i == 0:       # agar dono number i se divide ho rahe hain
        gcd = i                               # to gcd ko update kar do
print("GCD of", num1, "and", num2, "is", gcd)


#i divide kar raha hai dono numbers ko common divisor ke roop mai aur gcd ko update kar raha hai jab bhi ek naya common divisor milta hai.
# Iska time complexity O(min(num1, num2)) hai kyuki loop chota number tak chalta hai.


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
original_num1 = num1    # Store original values for final output
original_num2 = num2
while num2 != 0:        # Jab tak num2 0 nahi ho jata ,# Euclidean algorithm
    num1, num2 = num2, num1 % num2  # Swap: num1 becomes num2, num2 becomes num1 % num2
print("GCD of", original_num1, "and", original_num2, "is", num1)

#Using math module
import math
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
gcd = math.gcd(num1, num2)                    # math module ka gcd function use kar rahe hain
print("GCD of", num1, "and", num2, "is", gcd)
# math.gcd() function efficient algorithm use karta hai jise Euclidean algorithm kehte hain jiska time complexity O(log(min(num1, num2))) hota hai.
# Iska matlab hai ki ye bahut hi speed se bada numbers ka bhi gcd nikal lega

#using function
def compute_gcd(a, b):
    while b:          # Same as: while b != 0: 
        a, b = b, a % b  # Swap: a becomes b, b becomes a % b
    return a    
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
gcd = compute_gcd(num1, num2)
print("GCD of", num1, "and", num2, "is", gcd)



# Simple function to find GCD by checking all divisors
def gcd_simple_loop(a, b):
    """
    Find GCD by checking all divisors up to smaller number
    """
    smaller = min(a, b)
    for i in range(smaller, 0, -1): # range(start, stop, step) -1 means decrementing
        
        if a % i == 0 and b % i == 0:
            return i  # Found GCD, return immediately
    
    return 1  # Fallback (should not reach here)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = gcd_simple_loop(num1, num2)
print(f"GCD of {num1} and {num2} is {result}")



# Another implementation using Euclidean algorithm
def compute_gcd(a, b):
    while b:                    # Loop while b is not 0
        a, b = b, a % b         # Swap: a becomes b, b becomes a % b
    return a                    # When b becomes 0, return a (the GCD)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
gcd = compute_gcd(num1, num2)
print("GCD of", num1, "and", num2, "is", gcd)