# Better than previous example time thoda kam lagega Time Complexity  O(n/2)
#simple logic hai ki ek number ka half tak hi check karna hai kyuki usse zyada ke factors nahi hoga re

num = int(input("Enter a number: "))
if num < 2:
    print(num, "is not a prime number")
else:
    for i in range(2, (num//2)+1):   # yaha pe num//2 +1 isliye kiya taki num/2 bhi include ho jaye aur floor division use kiya taki float na aaye
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")