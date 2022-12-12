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
    if (row_diff >= 1 and col_diff >= 2) or (row_diff >= 2 and col_diff >= 1):
        return (tail[0]+1, tail[1]+1)

    # head up right
    if (row_diff <= -1 and col_diff >= 2) or (row_diff <= -2 and col_diff >= 1):
        return (tail[0]-1, tail[1]+1)

    # down left
    if (row_diff >= 1 and col_diff <= -2) or (row_diff >= 2 and col_diff <= -1):
        return (tail[0]+1, tail[1]-1)

    # up left
    if (row_diff <= -1 and col_diff <= -2) or (row_diff <= -2 and col_diff <= -1):
        return (tail[0]-1, tail[1]-1)

    return tail


def get_next_tail_pos(lead_tail, follower_tail, final, update):
    updated_follower = update_tail(lead_tail, follower_tail)
    if update:
        final.add(updated_follower)

    return updated_follower


def get_next_head_pos(letter, head):
    if letter == "R":
        delta = (0, 1)
    elif letter == "L":
        delta = (0, -1)
    elif letter == "U":
        delta = (-1, 0)
    elif letter == "D":
        delta = (1, 0)

    head =  (head[0] + delta[0], head[1] + delta[1])
    return head

s = 500_000
tails = [(s, s)]*10

final = set()
final.add(tails[-1])

for line in stdin:
    letter, num = line.strip().split()
    num = int(num)

    for _ in range(num):
        tails[0] = get_next_head_pos(letter, tails[0])
        for head_idx in range(0, len(tails)-1):
            update = head_idx == len(tails)-2
            tails[head_idx+1] = get_next_tail_pos(tails[head_idx], tails[head_idx+1], final, update=update)

print(len(final))
