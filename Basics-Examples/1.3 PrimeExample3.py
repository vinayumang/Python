#Best Approach to check for prime number Time Complexity: O(sqrt(n)) or O(√n)
import math
num =  int (input("Enter any number :"))  
if num<2:
    print ("The number is not prime")
else:
    for i in range (2, math.isqrt(num)+1):  # math.isqrt(num) float return nahi karta hai normally math.sqrt(num) float return karta hai
        if num % i == 0:
            print ("The number is not prime")
            break
    else:
        print ("The number is prime")


#square root ka logic ye hai ki agar ek number composite hai to uske factors hamesha uske square root ke andar hi milenge. 
# For example 36 ke factors hain 1,2,3,4,6,9,12,18,36. Yaha pe 6 iska square root hai aur iske factors 6 ke andar hi mil rahe hain.
# Isliye hume sirf square root tak hi check karna hai. Isse time complexity bahut kam ho jati hai.