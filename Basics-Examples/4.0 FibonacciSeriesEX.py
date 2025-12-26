#Fibonacci series are a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1.
# Example: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
num =int(input("Enter a number : "))
x,y=0,1
z=0
print("Fibonacci series:")
while z<=num:
    print(z,end=' ')
    x=y
    y=z
    z=x+y   

print()  #new line for better output formatting


#Alternative approach to generate Fibonacci series up to n terms

n = int(input("Enter the number : "))       
a, b = 0, 1
count = 0   
if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci series up to", n, ":")
    print(a)
else:
    print("Fibonacci series:")
    while count < n:
        print(a, end=' ')  #print karte hain current term ,iske baad space de dete hain ,a+b use karte hain next term nikalne ke liye
        a, b = b, a + b    # Update karte hain values of a and b aur b ko next term bana dete hain
        count += 1          # Increment karte hain count kyunki ek term print kar chuke hain
# Is code ka time complexity O(n) hai kyunki loop n times chalta hai.
# Is code ka space complexity O(1) hai kyunki humne constant space use kiya hai. 