import sys

def parse_line(line):
    sub1, sub2 = line.split(',')
    start1, end1 = sub1.split('-')
    start2, end2 = sub2.split('-')
    return int(start1), int(end1), int(start2), int(end2)


num_contains = 0
for line in sys.stdin:
    start1, end1, start2, end2 = parse_line(line)
    if start1 <= start2 and end1 >= end2 or\
            start2 <= start1 and end2 >= end1:
        num_contains += 1
        print(line)

print(num_contains)


