from enum import Enum
from sys import stdin

lines = stdin.readlines()
RIGHT, WRONG, CONTINUE = range(3)


def is_right_order(lst1, lst2):
    for item1, item2 in zip(lst1, lst2):
        #  print("item1: {}, item2: {}".format(item1, item2))

        match item1, item2:

            case int(), int():
                if item1 < item2:
                    return RIGHT

                if item1 > item2:
                    #  print("Reprovu item 1 > item 2")
                    return WRONG

            case list(), list():
                ret = is_right_order(item1, item2)
                if ret != CONTINUE:
                    return ret

            case list(), int():
                ret = is_right_order(item1, [item2])
                #  print("lst, int")
                if ret != CONTINUE:
                    return ret

            case int(), list():
                ret = is_right_order([item1], item2)
                #  print("int, lst")
                if ret != CONTINUE:
                    return ret

    if len(lst1) < len(lst2):  # left runs out first
        return RIGHT

    if len(lst1) > len(lst2):  # right runs out first
        return WRONG

    # they're the same length - inconclusive
    return CONTINUE


count = 0

for idx, (line1, line2) in enumerate(zip(lines[::3], lines[1::3]), 1):
    line1 = eval(line1.strip())
    line2 = eval(line2.strip())
    #  print(idx)
    #  print(line1)
    #  print(line2)
    #  print("starting")

    if is_right_order(line1, line2) == RIGHT:
        count += idx

print(count)

