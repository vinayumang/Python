# 1. Using string slicing
s = input("Enter a string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Using a function
def is_palindrome(s):
    return s == s[::-1]

word = input("Enter a word: ")

if is_palindrome(word):
    print("Palindrome")
else:
    print("Not Palindrome")


# Palindrome for a number
n = int(input("Enter a number: "))

temp = n
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10

if temp == rev:
    print("Palindrome number")
else:
    print("Not Palindrome number")

# Without slicing (logic-based)
s = input("Enter a string: ")
rev = ""

for ch in s:
    rev = ch + rev

if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
