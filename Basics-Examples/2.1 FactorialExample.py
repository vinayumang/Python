#Using while loop to calculate factorial of a number
num = int(input("Enter a number : "))
factorial = 1
i = 1
while i <= num:
    factorial *= i          # factorial = factorial * i
    i += 1
print(f"The factorial of {num} is {factorial}")    


