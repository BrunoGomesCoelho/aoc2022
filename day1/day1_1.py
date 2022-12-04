import sys

carrying, max_carrying = 0, 0

for line in sys.stdin:
    if line == '\n':
        if carrying > max_carrying:
            max_carrying = carrying
        carrying = 0
    else:
        carrying += int(line)

print(max_carrying)
