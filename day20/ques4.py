# Q80: Write a program to Find column-wise sum.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = len(matrix)
cols = len(matrix[0])

# Loop through each column index first
for j in range(cols):
    col_sum = 0
    # Loop through each row to pick elements from column j
    for i in range(rows):
        col_sum += matrix[i][j]
        
    print(f"Sum of Column {j + 1}: {col_sum}")