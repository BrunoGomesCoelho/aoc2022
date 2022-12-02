import sys

# gabriel's dumb solution
max_carrying = 0
max2_carrying = 0
max3_carrying = 0
carrying = 0


for line in sys.stdin:
    print(f'line: {line}')
    if line == '\n':
        if carrying > max_carrying:
            max3_carrying = max2_carrying
            max2_carrying = max_carrying
            max_carrying = carrying
        elif carrying > max2_carrying:
            max3_carrying = max2_carrying
            max2_carrying = carrying
        elif carrying > max3_carrying:
            max3_carrying = carrying
        carrying = 0
    else:
        carrying += int(line)

print(max_carrying+max2_carrying+max3_carrying)
print(max_carrying)
print(max2_carrying)
print(max3_carrying)
