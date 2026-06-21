# Q77: Write a program to Multiply matrices.

# Define two 2x2 matrices to multiply
matrix_A = [
    [1, 2],
    [3, 4]
]

matrix_B = [
    [5, 6],
    [7, 8]
]

# Initialize a 2x2 result matrix with zeros
result = [
    [0, 0],
    [0, 0]
]

# Multiplying the matrices
# Loop through rows of matrix_A
for i in range(len(matrix_A)):
    # Loop through columns of matrix_B
    for j in range(len(matrix_B[0])):
        # Loop through rows of matrix_B to calculate the dot product
        for k in range(len(matrix_B)):
            result[i][j] += matrix_A[i][k] * matrix_B[k][j]

# Display the final multiplied matrix
print("Result of Matrix Multiplication:")
for row in result:
    print(row)