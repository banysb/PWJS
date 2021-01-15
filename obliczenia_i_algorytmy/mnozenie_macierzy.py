import random

rows, cols = 8, 8
matrix1 = [[random.randint(1, 100) for x in range(rows)] for y in range(cols)]
matrix2 = [[random.randint(1, 100) for i in range(rows)] for j in range(cols)]
matrix3 = [[0 for k in range(rows)] for l in range(cols)]
for i in range(rows):
    for j in range(cols):
        for k in range(len(matrix1)):
            matrix3[j][i] += matrix1[j][k] * matrix2[k][i]
print(matrix3)
