from sys import stdin

total = 0
common = set()

for iteration, line in enumerate(stdin, 1):
    line = line.strip()

    if common:
        common &= set(line)
    else:
        common = set(line)

    if iteration % 3 == 0:
        assert len(common) == 1
        char = common.pop()

        if char.isupper():
            total += ord(char) - 64 + 26
        else:
            total += ord(char) - 96

print(total)
