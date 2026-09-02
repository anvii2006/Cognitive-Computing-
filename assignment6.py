import numpy as np

# Q1. Sensor Readings

temperature = np.array([25, 28, 31, 35, 38, 27, 33, 40])

temperature_updated = temperature + 2

print("Q1(a) Temperature after adding 2°C:")
print(temperature_updated)

fahrenheit = (9 / 5) * temperature + 32

print("\nQ1(b) Temperature in Fahrenheit:")
print(fahrenheit)

readings_greater_32 = temperature[temperature > 32]

print("\nQ1(c) Readings greater than 32°C:")
print(readings_greater_32)

count = np.sum(temperature > 32)

print("\nQ1(d) Number of readings greater than 32°C:")
print(count)

print("\nQ1(e) Explanation:")
print("Vectorization performs operations on the entire array at once")
print("without using a for loop, making calculations faster and simpler.")
print("Boolean indexing allows us to select only the elements that")
print("satisfy a given condition efficiently.")

# Q2. Daily Steps

steps = np.array([
    [5000, 6200, 7100],
    [8000, 7500, 9000],
    [4500, 5100, 4800],
    [9000, 8500, 9500]
])

total_steps = np.sum(steps)

print("\n\nQ2(a) Total steps:")
print(total_steps)

mean_steps = np.mean(steps)

print("\nQ2(b) Mean number of steps:")
print(mean_steps)

maximum = np.max(steps)
minimum = np.min(steps)

print("\nQ2(c) Maximum:", maximum)
print("Minimum:", minimum)

total_each_day = np.sum(steps, axis=0)

print("\nQ2(d) Total steps for each day:")
print(total_each_day)

total_each_user = np.sum(steps, axis=1)

print("\nQ2(e) Total steps for each user:")
print(total_each_user)

max_position = np.argmax(steps)
max_position_2d = np.unravel_index(np.argmax(steps), steps.shape)

print("\nQ2(f) Position of maximum number of steps:")
print(max_position_2d)

# Q3. NumPy Slicing, Copying, Flatten and Ravel

# a. Create original array
original = np.array([1, 2, 3, 4, 5, 6])

print("\n\nQ3(a) Original array:")
print(original)

# b. Slice index 1 to 4
subset = original[1:5]

print("\nQ3(b) Subset:")
print(subset)

# c. Modify first element of subset
subset[0] = 999

print("\nQ3(c) After modifying subset:")
print("Original:", original)
print("Subset:", subset)

print("The original array is also changed because slicing creates a view.")

# d. Create a copy and modify it
copied_array = original[1:5].copy()

copied_array[0] = 500

print("\nQ3(d) After modifying copied array:")
print("Original:", original)
print("Copied array:", copied_array)

print("The original array is not affected because copy() creates a separate array.")

# e. Create numbers 1 to 12 and reshape to 3 x 4
matrix = np.arange(1, 13).reshape(3, 4)

print("\nQ3(e) 3 x 4 Matrix:")
print(matrix)

# f. NumPy indexing and slicing

first_row = matrix[0, :]
print("\nQ3(f) First row:")
print(first_row)

last_row = matrix[-1, :]
print("Last row:")
print(last_row)

second_column = matrix[:, 1]
print("Second column:")
print(second_column)

selected_elements = matrix[0:2, 1:3]
print("Rows 1-2 and columns 2-3:")
print(selected_elements)

# g. Flatten using flatten() and ravel()
flattened_array = matrix.flatten()
ravel_array = matrix.ravel()

print("\nQ3(g) Using flatten():")
print(flattened_array)

print("Using ravel():")
print(ravel_array)

# h. Modify ravel array
ravel_array[0] = 1000

print("\nQ3(h) After modifying ravel array:")
print("Ravel array:")
print(ravel_array)

print("Original matrix:")
print(matrix)

print("The original matrix is affected because ravel() usually returns a view.")

# i. Modify flatten array
flattened_array[1] = 2000

print("\nQ3(i) After modifying flatten array:")
print("Flattened array:")
print(flattened_array)

print("Original matrix:")
print(matrix)

print("The original matrix is not affected because flatten() returns a copy.")

# j. Display shape, ndim, size and dtype
print("\nQ3(j) Matrix information:")
print("Shape:", matrix.shape)
print("Dimensions:", matrix.ndim)
print("Size:", matrix.size)
print("Data type:", matrix.dtype)

# Q4. Cognitive Assistive System - OLS

X = np.array([
    [6, 70, 3],
    [5, 50, 6],
    [8, 80, 2],
    [4, 30, 8]
])

y = np.array([40, 65, 30, 85])

# a. Display shape and dimensions
print("\n\nQ4(a) Shape of X:")
print(X.shape)

print("Dimensions of X:")
print(X.ndim)

# b. Transpose
X_T = X.T

print("\nQ4(b) X Transpose:")
print(X_T)

print("The transpose changes rows into columns and columns into rows.")

# c. Matrix product X.T @ X
XTX = X_T @ X

print("\nQ4(c) X.T @ X:")
print(XTX)

# d. Matrix inverse
XTX_inverse = np.linalg.inv(XTX)

print("\nQ4(d) Inverse of X.T @ X:")
print(XTX_inverse)

# e. Ordinary Least Squares

beta = XTX_inverse @ X_T @ y

print("\nQ4(e) OLS coefficients:")
print(beta)

# f. Explanation of coefficients
print("\nQ4(f) Meaning of coefficients:")
print("Coefficient 1 represents the effect of Sleep Hours.")
print("Coefficient 2 represents the effect of Activity Level.")
print("Coefficient 3 represents the effect of Stress Level.")
print("Each coefficient shows how the predicted assistance score")
print("changes with that feature, while the other features are kept constant.")

# g. Predict assistance score for new user
new_user = np.array([5, 40, 7])

predicted_score = new_user @ beta

print("\nQ4(g) New user:")
print(new_user)

print("Predicted assistance score:")
print(predicted_score)