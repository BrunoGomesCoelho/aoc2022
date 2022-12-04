from sys import stdin

total = 0

for line in stdin:
    halfway_point = len(line) // 2
    rucksack_a, rucksack_b = line[:halfway_point], line[halfway_point:]

    common = set(rucksack_a) & set(rucksack_b)
    assert len(common) == 1
    char = common.pop()

    if char.isupper():
        total += ord(char) - 64 + 26
    else:
        total += ord(char) - 96

print(total)
