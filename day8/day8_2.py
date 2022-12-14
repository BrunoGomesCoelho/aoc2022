from sys import stdin
import numpy as np


def get_visible_height(array, element):
    count = 0

    for num in array:
        count +=1
        if num >= element:
            break

    return count


matrix = np.genfromtxt(stdin, delimiter=1, dtype=int)
scenic_score = 0

for i in range(1, matrix.shape[0]-1):
    for j in range(1, matrix.shape[1]-1):
        right_to_left = get_visible_height(matrix[i, :j][::-1], matrix[i, j])
        left_to_right = get_visible_height(matrix[i, j+1:], matrix[i, j])
        up_to_down = get_visible_height(matrix[:i, j][::-1], matrix[i, j])
        down_to_up = get_visible_height(matrix[i+1:, j], matrix[i, j])

        scenic_score = max(scenic_score, right_to_left * left_to_right * up_to_down * down_to_up)

# foda-se edges
print(scenic_score)
