from sys import stdin

# comeca com 1
# noop > print X na lista 1 vez
# adx3 > print X na lista 1 vezes e print X+add e atualiza x

fita = [1]
x = 1

for line in stdin:
    instruction = line.split()[0]

    if instruction == "addx":
        num = int(line.split()[1])
        fita.append(x)
        x += num
        fita.append(x)
    elif instruction == "noop":
        fita.append(x)
    else:
        print("error")
        sys.exit(1)

print(fita[:10])
# print(interesting_signals)

screen = []
for i in range(6):
    output_line = ""
    for pos in range(40):
        actual_pos = pos + 40*i
        if pos-1 <= fita[actual_pos] <= pos+1:
            output_line += "#"
        else:
            output_line += "."

    print(output_line)

