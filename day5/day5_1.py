from sys import stdin


# Use copilot to auto generate the correct stack code below :)
stacks = [
    ["Z", "N"],
    ["M", "C", "D"],
    ["P"],
]

stacks = [
    ["Q", "W", "P", "S", "Z", "R", "H", "D"],
    ["V", "B", "R", "W", "Q", "H", "F"],
    ["C", "V", "S", "H"],
    ["H", "F", "G"],
    ["P", "G", "J", "B", "Z"], 
    ["Q", "T", "J", "H", "W", "F", "L"],
    ["Z", "T", "W", "D", "L", "V", "J", "N"],
    ["D", "T", "Z", "C", "J", "G", "H", "F"],
    ["W", "P", "V", "M", "B", "H"],
]

for line in stdin:
    _move, amount, _from, origin, _to, dest = line.strip().split()
    amount, origin, dest = int(amount), int(origin) - 1, int(dest) - 1

    for _ in range(int(amount)):
        stacks[dest].append(stacks[origin].pop())

print("".join(x[-1] for x in stacks))
