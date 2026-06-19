# Q74: Write a program to Subtract matrices.

# Define two 3x3 matrices
matrix_A = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

matrix_B = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
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
        result[i][j] = matrix_A[i][j] - matrix_B[i][j]

# Display the result
print("Difference of the matrices:")
for row in result:
    print(row)