from sys import stdin


def update_tail(head, tail):
    row_diff = head[0] - tail[0]
    col_diff = head[1] - tail[1]

    if row_diff == 0 and abs(col_diff) == 2:
        if col_diff > 0:
            return (tail[0], tail[1]+1)
        return (tail[0], tail[1]-1)

    if abs(row_diff) == 2 and col_diff == 0:
        if row_diff > 0:
            return (tail[0]+1, tail[1])
        return (tail[0]-1, tail[1])

    # head bottom right
    if (row_diff == 1 and col_diff == 2) or (row_diff == 2 and col_diff == 1):
        return (tail[0]+1, tail[1]+1)

    # head up right
    if (row_diff == -1 and col_diff == 2) or (row_diff == -2 and col_diff == 1):
        return (tail[0]-1, tail[1]+1)

    # down left
    if (row_diff == 1 and col_diff == -2) or (row_diff == 2 and col_diff == -1):
        return (tail[0]+1, tail[1]-1)

    # up left
    if (row_diff == -1 and col_diff == -2) or (row_diff == -2 and col_diff == -1):
        return (tail[0]-1, tail[1]-1)

    return tail


s = 500_000
head, tail = (s, s), (s, s)

final = set()
final.add(tail)

for line in stdin:
    letter, num = line.strip().split()
    num = int(num)
    if letter == "R":
        delta = (0, 1)
    elif letter == "L":
        delta = (0, -1)
    elif letter == "U":
        delta = (-1, 0)
    elif letter == "D":
        delta = (1, 0)

    for _ in range(num):
        head =  (head[0] + delta[0], head[1] + delta[1])
        tail = update_tail(head, tail)
        final.add(tail)


print(len(final))
