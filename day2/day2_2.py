import sys

play_points = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

win_points = {
    ("A", "X"): 3 + 0,
    ("A", "Y"): 1 + 3,
    ("A", "Z"): 2 + 6,

    ("B", "X"): 1 + 0,
    ("B", "Y"): 2 + 3,
    ("B", "Z"): 3 + 6,

    ("C", "X"): 2 + 0,
    ("C", "Y"): 3 + 3,
    ("C", "Z"): 1 + 6,
}

total = 0
for line in sys.stdin:
    player1, player2 = line.strip().split(" ")
    total += win_points[(player1, player2)]

print(total)





