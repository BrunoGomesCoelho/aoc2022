from sys import stdin
import numpy as np


matrix = np.genfromtxt(stdin, delimiter=1, dtype=int)
visible = set()
for i in range(1, matrix.shape[0]-1):
    for j in range(1, matrix.shape[1]-1):
        # right > left
        if all(matrix[i,:j] < matrix[i,j]):
            print(f"{(i, j)} is visible by left")
            visible.add((i, j))
        # left > right
        if all(matrix[i,j] > matrix[i,j+1:]):
            print(f"{(i, j)} is visible by right")
            visible.add((i, j))
        # up > down
        if all(matrix[:i,j] < matrix[i,j]):
            print(f"{(i, j)} is visible by up")
            visible.add((i, j))
        # down > up
        if all(matrix[i,j] > matrix[i+1:,j]):
            print(f"{(i, j)} is visible by down")
            visible.add((i, j))


# dont forget to sum edge
cols = matrix.shape[1]
rows = matrix.shape[0]
edges = cols + cols + 2*rows-4
print(visible, edges)
print(len(visible) + edges)
