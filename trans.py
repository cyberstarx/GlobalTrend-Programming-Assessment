def transpose_matrix(matrix):
    
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    
    return transposed
    
    #example usage: 
    
original_matrix = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

print("Original matrix:")
for row in original_matrix:
    print(row)

transposed_matrix = transpose_matrix(original_matrix)

print("\nTransposed matrix:")
for row in transposed_matrix:
    print(row)

