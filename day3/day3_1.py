from sys import stdin

total = 0
a, A = ord('a'), ord('A')

for line in stdin:
    halfway_point = len(line) // 2
    rucksack_a, rucksack_b = line[:halfway_point], line[halfway_point:]

    common = set(rucksack_a) & set(rucksack_b)
    assert len(common) == 1
    char = common.pop()

    total += ord(char) - A + 27 if char.isupper() else ord(char) - a + 1

print(total)
