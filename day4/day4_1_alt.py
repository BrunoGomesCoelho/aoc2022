from sys import stdin

total = 0

for line in stdin:
    (a, b), (c, d) = [a.split("-") for a in line.strip().split(",")]
    a, b, c, d = int(a), int(b), int(c), int(d)

    if (a <= c <= b and a <= d <= b) or (c <= a <= d and c <= b <= d):
        print(f"Overlap: {a}-{b} and {c}-{d}")
        total += 1

print(total)
