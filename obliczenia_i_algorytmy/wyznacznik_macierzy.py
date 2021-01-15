import numpy as np
import random
rows, cols = 10, 10
matrix = [[random.randint(1, 100) for x in range(rows)] for y in range(cols)]
matrix = np.asarray(matrix)
print("Macierz:\n", matrix)

print("Wyznacznik macierzy: ",np.linalg.det(matrix))