#Commnly jo sab use karte hain prime number check karne ke liye
num = int(input("Enter a number: "))
if num < 2:
    print(num, "is not a prime number")
else:
    for i in range(2,num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

# Ismai ye problem hai ki agar number bada hoga to loop bhi zyada chalega aur time bhi zyada lagega.
# Timw complexity: O(n)     