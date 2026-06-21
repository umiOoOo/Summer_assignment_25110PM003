# Q79: Write a program to Find row-wise sum.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Loop through each row index
for i in range(len(matrix)):
    row_sum = 0
    # Loop through elements of the current row
    for j in range(len(matrix[i])):
        row_sum += matrix[i][j]
        
    print(f"Sum of Row {i + 1}: {row_sum}")