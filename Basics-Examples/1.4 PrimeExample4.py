#using function to check prime number
import math 
def is_prime(num):
    if num <2:
        print(num, "is not a prime number")
        return
    for i in range(2, math.isqrt(num)+1):
        if num % i == 0:
            print(num, "is not a prime number")
            return
    print(num, "is a prime number")

#Bulao function ko
number = int(input("Enter a number: "))
is_prime(number)
