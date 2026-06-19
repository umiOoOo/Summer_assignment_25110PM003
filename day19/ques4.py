# Q76: Write a program to Find diagonal sum.

# Define a square matrix (3x3)
matrix = [
    [2, 4, 6],
    [1, 5, 9],
    [3, 8, 7]
]

primary_diagonal_sum = 0
secondary_diagonal_sum = 0
n = len(matrix)

for i in range(n):
    # Primary diagonal elements have matching row and column indices (e.g., 00, 11, 22)
    primary_diagonal_sum += matrix[i][i]
    
    # Secondary diagonal elements go from top-right to bottom-left
    secondary_diagonal_sum += matrix[i][n - 1 - i]

# Display the sums
print(f"Matrix:")
for row in matrix:
    print(row)
    
print(f"\nSum of Primary Diagonal (2 + 5 + 7): {primary_diagonal_sum}")
print(f"Sum of Secondary Diagonal (6 + 5 + 3): {secondary_diagonal_sum}")