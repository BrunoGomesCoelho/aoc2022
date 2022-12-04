import sys

# gabriel's dumb solution
carrying, max_carrying, max2_carrying, max3_carrying = 0, 0, 0, 0

for line in sys.stdin:
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
