# Q73: Write a program to Add matrices.

# Define two 3x3 matrices
matrix_A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Initialize a result matrix with zeros
result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Iterate through rows
for i in range(len(matrix_A)):
    # Iterate through columns
    for j in range(len(matrix_A[0])):
        result[i][j] = matrix_A[i][j] + matrix_B[i][j]

# Display the result
print("Sum of the matrices:")
for row in result:
    print(row)