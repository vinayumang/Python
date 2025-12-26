#Finding all prime numbers in a given range
#Time Complexity: O(n)


"""Ismai ye dikkat hai ki start aur end dono mai input 1 hua to output kuch nahi aayega kyuki 1 prime number nahi hota."""


# Find all prime numbers between start and end range
start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

for num in range(start, end + 1):   # end +1 to include end number kyuki range function end ko include nahi karta
    if num <= 1:                  # Numbers less than or equal to 1 are not prime
        continue
    for i in range(2, num // 2 + 1):  # Check if num has any divisors from 2 to num/2
        if num % i == 0:               # Found a divisor, so not prime
            break
    else:                              # No divisors found, so it's prime
        print(num, end=" ")
print()
# Using square root method to improve efficiency
# This method can be inefficient for large ranges.  

import math
start =int(input("Enter start range: "))
end =int(input("Enter end range: "))    
for num in range(start, end + 1):
    if num <= 1:
        continue
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")