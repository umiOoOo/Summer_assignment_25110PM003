# Q78: Write a program to Check symmetric matrix.

# Define a square matrix to check
matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

is_symmetric = True
n = len(matrix)

# Loop through rows and columns
for i in range(n):
    for j in range(n):
        # Compare element at (i, j) with element at (j, i)
        if matrix[i][j] != matrix[j][i]:
            is_symmetric = False
            break  # Exit inner loop if a mismatch is found

# Display the result
if is_symmetric:
    print("The matrix is symmetric.")
else:
    print("The matrix is not symmetric.")