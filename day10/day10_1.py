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

interesting_signals =\
    fita[19]*20 +\
    fita[59]*60 +\
    fita[99]*100 +\
    fita[139]*140 +\
    fita[179]*180 +\
    fita[219]*220

print(interesting_signals)
