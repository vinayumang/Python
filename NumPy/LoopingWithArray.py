import numpy as np 


# Looping through a 1D NumPy array
array_1d = np.array([10, 20, 30, 40, 50])  
print("Looping through 1D Array:")
for element in array_1d:
    print(element)


# Calculate Sum of elements in a 1D array
numbers = np.array([5, 10, 15, 20])
total = 0
for num in numbers:
    total = total + num
    #print(f"Adding {num}, total now = {total}") # Ye intermediate sum dikhata hai har step pe bina iska final sum bhi  dikha sakte hai 

print(f"Final Sum: {total}")

# Looping through a 2D NumPy array
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  
print("\nLooping through 2D Array:")
for row in array_2d:
    for element in row:
        print(element)

# Calculate Sum of elements in a 2D array
matrix = np.array([[1, 2, 3], [4, 5, 6]])
total_2d = 0
for row in matrix:
    for num in row:
        total_2d += num
        
print(f"Final Sum of 2D Array: {total_2d}")        

# Looping through a 3D NumPy array
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  
print("\nLooping through 3D Array:")
for block in array_3d:
    for row in block:
        for element in row:
            print(element)      

# Calculate Sum of elements in a 3D array
cube = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
total_3d = 0
for block in cube:
    for row in block:
        for num in row:
            total_3d += num             
print(f"Final Sum of 3D Array: {total_3d}")