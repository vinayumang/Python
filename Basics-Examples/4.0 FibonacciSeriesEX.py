#Fibonacci series are a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1.
# Example: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
 
n = int(input("Enter number of terms: "))  
a, b = 0, 1                       #user 1 dala tab range mai 1 ayega sirf a ka value print ho jayega 0
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b   
    
# The statement a, b = b, a + b uses Python's simultaneous assignment (also called tuple unpacking or parallel assignment) 
# to update both variables at once using their original values.

# Think of a, b = b, a + b as a two-step update done in one line.
# You are doing this in Fibonacci:
# * a = current term
# * b = next term
# And you want to move one step forward:
# * new a should become old b (next term becomes current term)
# * new b should become old a + b (next term = sum of previous two terms)
# So conceptually you want:

# python
# new_a = old_b
# new_b = old_a + old_b
# Python does exactly this with:

# python
# a, b = b, a + b
# What happens internally
# Python evaluates the right side first and makes a pair (tuple):

# python
# (b, a + b)
# using the old values of a and b.Then it unpacks:

# python
# a = old b
# b = old (a + b)
# So both updates happen simultaneously, and old a is still available when computing a + b.


# Using while loop    
n = int(input("Enter number of terms: "))
a, b = 0, 1
count = 0

while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
print()