from sys import stdin

total = 0
common = set()
a, A = ord('a'), ord('A')

for iteration, line in enumerate(stdin, 1):
    line = line.strip()

    common = common & set(line) if common else set(line)

    if iteration % 3 == 0:
        assert len(common) == 1
        char = common.pop()

        total += ord(char) - A + 27 if char.isupper() else ord(char) - a + 1

print(total)
