# Factorial Example
num = int(input("Enter a number to find its factorial: "))
if num < 0:
    print("Factorial is not defined for negative numbers")
elif num == 0 or num == 1:
    print(f"The factorial of {num} is 1")    
else:
    factorial = 1
    for i in range(1, num + 1):
     factorial *= i          # factorial = factorial * i
    print(f"The factorial of {num} is {factorial}")

# Time Complexity: O(n) matlab loop n times chalega
# Space Complexity: O(1) matlab extra space nahi lagta hai

#dry run 
# num = 5
# factorial = 1
# i = 1 -> factorial = 1 * 1 = 1
# i = 2 -> factorial = 1 * 2 = 2
# i = 3 -> factorial = 2 * 3 = 6
# i = 4 -> factorial = 6 * 4 = 24
# i = 5 -> factorial = 24 * 5 = 120
# Output: The factorial of 5 is 120

#Recursive approach
num = int(input("Enter a number to find its factorial using recursion: "))
def factorial_recursive(n): 
    if n == 0 or n == 1:  # check karta hai ki passs kiya hua number 0 ya 1 hai
        return 1  #return 1 as factorial of 0 and 1 is 1
    else:
        return n * factorial_recursive(n - 1)  # Recursive case 
result = factorial_recursive(num)
print(f"The factorial of {num} using recursion is {result}")    

# Time Complexity: O(n) 
# Space Complexity: O(n) due to recursive call stack matlab har function call ke liye space lagta hai stack mai