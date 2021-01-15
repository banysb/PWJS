import random

rows, cols = 128, 128
matrix1 = [[random.randint(1, 1000) for x in range(rows)] for y in range(cols)]
matrix2 = [[random.randint(1, 1000) for i in range(rows)] for j in range(cols)]
matrix3 = [[0 for k in range(rows)] for l in range(cols)]

for i in range(rows):
    for j in range(cols):
        matrix3[i][j] = matrix1[i][j]+matrix2[i][j]
print(matrix1)
print(matrix2)
print(matrix3)