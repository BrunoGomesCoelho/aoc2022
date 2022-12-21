from sys import stdin
import numpy as np
from heapq import heappush, heappop

board, heap = [], []
visited = set()

def is_valid_pos(cur_pos, next_pos):
    if next_pos[0] < 0 or next_pos[0] >= board.shape[0] \
            or next_pos[1] < 0 or next_pos[1] >= board.shape[1]:
        return False

    if ord(board[next_pos[0], next_pos[1]]) > ord(board[cur_pos[0], cur_pos[1]])+1:
        return False

    return True


def push_adj(pos, cost):
    directions = np.array([
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    ])

    for inc in directions:
        next_pos = pos + np.array(inc)
        if is_valid_pos(pos, next_pos):
            heappush(heap, (cost+1, tuple(next_pos)))


def find_shortest_path(start, end):
    heappush(heap, (0, start))

    cur_cost, cur_pos = heappop(heap)
    if (cur_pos[0], cur_pos[1]) not in visited:
        visited.add((cur_pos[0], cur_pos[1]))
        push_adj(cur_pos, cur_cost)

    while (cur_pos != end).any():
        cur_cost, cur_pos = heappop(heap)
        if (cur_pos[0], cur_pos[1]) not in visited:
            visited.add((cur_pos[0], cur_pos[1]))
            push_adj(cur_pos, cur_cost)

    return cur_cost



for line in stdin:
    board.append(list(line.strip()))

board = np.array(board)

start_pos = np.argwhere(board=='S')[0]
end_pos = np.argwhere(board=='E')[0]

board[start_pos[0], start_pos[1]] = 'a'
board[end_pos[0], end_pos[1]] = 'z'

print(find_shortest_path(start_pos, end_pos))
