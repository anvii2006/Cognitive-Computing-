import numpy as np

# Q1. NumPy 1-D Array - Basic Operations

arr = np.array([10, 20, 30, 40, 50])

print("Q1")
print("Original Array:", arr)

print("After adding 2:", arr + 2)

print("After multiplying by 3:", arr * 3)

print("After dividing by 2:", arr / 2)

# Q2. Basic NumPy Array

print("\nQ2")

arr = np.array([1, 2, 3, 6, 4, 5])

print("Original array:", arr)
print("Reversed array:", arr[::-1])

# i.
x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1])

values, counts = np.unique(x, return_counts=True)

max_count = counts.max()
most_frequent = values[counts == max_count]

print("\ni. Array:", x)
print("Most frequent value:", most_frequent)
print("Frequency:", max_count)

for value in most_frequent:
    print("Indices:", np.where(x == value)[0])


# ii.
y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3, 1])

values, counts = np.unique(y, return_counts=True)

max_count = counts.max()
most_frequent = values[counts == max_count]

print("\nii. Array:", y)
print("Most frequent value:", most_frequent)
print("Frequency:", max_count)

for value in most_frequent:
    print("Indices:", np.where(y == value)[0])

# Q3. Accessing Elements of a 2-D Array

print("\nQ3")

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Array:")
print(arr)

print("1st row, 2nd column:", arr[0, 1])

print("3rd row, 1st column:", arr[2, 0])

# Q4. 1-D Array using linspace()

print("\nQ4")

Anvi = np.linspace(10, 100, 25)

print("Array:")
print(Anvi)

print("Number of dimensions:", Anvi.ndim)

print("Shape:", Anvi.shape)

print("Total elements:", Anvi.size)

print("Data type:", Anvi.dtype)

print("Total bytes:", Anvi.nbytes)

transpose_Anvi = Anvi.reshape(1, -1)

print("Transpose using reshape():")
print(transpose_Anvi)

print("Transpose using T:")
print(Anvi.T)

print("For a 1-D NumPy array, T does not change its shape.")

# Q5. 2-D Array, Statistical Operations, Reshape and Resize

print("\nQ5")

ucs420_Anvi = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 15, 20, 35]
])

print("Original Array:")
print(ucs420_Anvi)

print("Mean:", np.mean(ucs420_Anvi))

print("Median:", np.median(ucs420_Anvi))

print("Maximum:", np.max(ucs420_Anvi))

print("Minimum:", np.min(ucs420_Anvi))

print("Unique elements:", np.unique(ucs420_Anvi))

reshaped_ucs420_Anvi = ucs420_Anvi.reshape(4, 3)

print("\nReshaped Array (4 x 3):")
print(reshaped_ucs420_Anvi)

resized_ucs420_Anvi = np.resize(ucs420_Anvi, (2, 3))

print("\nResized Array (2 x 3):")
print(resized_ucs420_Anvi)