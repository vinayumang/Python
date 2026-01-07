import math
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Two roots: {root1}, {root2}"
    elif discriminant == 0:
        root = -b / (2*a)
        return f"One root: {root}"
    else:
        return "No real roots"

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))   
result = solve_quadratic(a, b, c)
print(result)