import sys

play_points = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

win_points = {
    ("A", "X"): 1 + 3,
    ("A", "Y"): 2 + 6,
    ("A", "Z"): 3 + 0,
    ("B", "X"): 1 + 0,
    ("B", "Y"): 2 + 3,
    ("B", "Z"): 3 + 6,
    ("C", "X"): 1 + 6,
    ("C", "Y"): 2 + 0,
    ("C", "Z"): 3 + 3,
}

total = 0
for line in sys.stdin:
    player1, player2 = line.strip().split(" ")
    total += win_points[(player1, player2)]

print(total)





