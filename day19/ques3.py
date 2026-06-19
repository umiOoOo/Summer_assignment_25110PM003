# Q75: Write a program to Transpose matrix.

# Define a 3x2 matrix (3 rows, 2 columns)
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

# Initialize a result matrix with dimensions 2x3 (2 rows, 3 columns) filled with zeros
# Transposing swaps rows and columns
transpose = [
    [0, 0, 0],
    [0, 0, 0]
]

# Iterate through rows of the original matrix
for i in range(len(matrix)):
    # Iterate through columns of the original matrix
    for j in range(len(matrix[0])):
        transpose[j][i] = matrix[i][j]

# Display the transposed matrix
print("Transposed Matrix:")
for row in transpose:
    print(row)