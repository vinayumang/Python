# Creating 1D, 2D, and 3D NumPy arrays and printing their dimensions

#          ndim array ka dimesion batata hai

import numpy as np  

# Creating a 1D array
array_1d = np.array([10, 20, 30, 40, 50])  
print("1D Array:", array_1d)
print("Dimensions of 1D Array:", array_1d.ndim) # Output: 1 


# Creating a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Starting  aur Ending mai double brackets for 2D array
print("\n2D Array:\n", array_2d)                       # 3 rows and 3 columns 
print("Dimensions of 2D Array:", array_2d.ndim)         # Output: 2


# Creating a 3D array
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # Starting with triple brackets for 3D array
print("\n3D Array:\n", array_3d)                            # 2 blocks hai each containing 2 rows and 2 columns 
print("Dimensions of 3D Array:", array_3d.ndim)            # Output: 3

# Summarize karte hain dimensions
print("\nSummary of Dimensions:")
print("1D Array Dimension:", array_1d.ndim)  # 1
print("2D Array Dimension:", array_2d.ndim)  # 2
print("3D Array Dimension:", array_3d.ndim)  # 3    

#Higher Dimensional Arrays can also be created similarly by adding more brackets.
# 5 Dimensional array banane ke liye 5 brackets use karne padenge. Waise define bhi kar sakte hai 
# ndmin attribute se pata kar sakte hai kitne dimension hai  array ke

arr=np.array([1,2,3,4],ndmin=5)   #define karte waqt hi 5 dimension ka array ban jayega
print(arr)
print("Dimensions of the array with ndmin=5:",arr.ndim)  #ndim sai pata chal jayega kitne dimension ka array hai
