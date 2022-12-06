from sys import stdin

start = 4

# do multiple so we can test all the sample inputs at once
for line in stdin:
    line = line.strip()

    for i in range(start-1, len(line)):
        if len(set(line[i-(start-1):i+1])) == start:
            print(i+1)
            break
