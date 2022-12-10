with open("input.txt") as f:
    instructions = [row.split() for row in f.read().splitlines()]

x = 1
cycle = 1
sig_str = []
for i in instructions:

    cycle += 1
    if (cycle + 20) % 40 == 0:
        sig_str.append((cycle, x))

    if i[0] == "addx":
        cycle += 1
        x += int(i[1])

        if (cycle + 20) % 40 == 0:
            sig_str.append((cycle, x))

print(sig_str)
print([x * c for x, c in sig_str])
print(sum([x * c for x, c in sig_str]))
