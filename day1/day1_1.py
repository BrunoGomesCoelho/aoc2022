import sys

max_carrying = 0
carrying = 0


for line in sys.stdin:
    print(f'line: {line}')
    if line == '\n':
        if carrying > max_carrying:
            max_carrying = carrying
        carrying = 0
    else:
        carrying += int(line)

print(max_carrying)
