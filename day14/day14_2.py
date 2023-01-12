from sys import stdin
import numpy as np

# forever == flows lower than lowest rock
# move straight (ugh) down
# elif move down to left
# elif move down to right
# else comes to rest


matrix = np.zeros((1000, 1000))

def construct_line(point1, point2):
    col1, line1 = [int(a) for a in point1.strip().split(',')]
    col2, line2 = [int(a) for a in point2.strip().split(',')]

    assert col1 == col2 or line1 == line2

    if col1 == col2:
        start_line = min(line1, line2)
        end_line = max(line1, line2)
        matrix[start_line:end_line+1,col1] = 1

    elif line1 == line2:
        start_col = min(col1, col2)
        end_col = max(col1, col2)
        matrix[line1, start_col:end_col+1] = 1

    return max(line1, line2)


def simulate(max_rock_line):
    coords = [0, 500]
    while True:

# move straight (ugh) down
        if matrix[coords[0]+1, coords[1]] == 0:
            coords[0] += 1
            continue
        elif matrix[coords[0]+1, coords[1]-1] == 0: #move down to left
            coords[0] += 1
            coords[1] -= 1
            continue
        elif matrix[coords[0]+1, coords[1]+1] == 0: #move down to right
            coords[0] += 1
            coords[1] += 1
            continue
        else: # return true if stopped and mark matrix
            matrix[coords[0], coords[1]] = 2
            return True

    # if sand goes further than max_rock_line return false
    return False


max_rock_line = -1
for line in stdin:
    points = line.strip().split(' -> ')
    for i in range(len(points)-1):
        max_rock_line = max(max_rock_line, construct_line(points[i], points[i+1]))

matrix[max_rock_line+2,:] = 1

while matrix[0,500] == 0:
    simulate(max_rock_line)

print(matrix[0:20, 490:510])
print(f'units of sand: {(matrix == 2).sum().sum()}')
