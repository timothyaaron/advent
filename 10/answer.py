DEBUG = False  # watch screen print

with open("input.txt") as f:
    instructions = [row.split() for row in f.read().splitlines()]

x = 1
cycle = 1
sig_str = []
output = [""]

for i in instructions:
    if DEBUG:
        print(i)

    # output, then close noop and addx (part 1) cycles
    output[-1] += "#" if (cycle-1) % 40 in (x - 1, x, x + 1) else "."
    cycle += 1
    if (cycle + 20) % 40 == 0:
        sig_str.append((cycle * x))
    if len(output[-1]) == 40:
        output.append("")

    if DEBUG:
        for line in output:
            print(line)

        print(("." * (x-1)) + ("#" * 3) + "\n")
        input()


    if i[0] == "addx":
        # addx, part2
        output[-1] += "#" if (cycle-1) % 40 in (x - 1, x, x + 1) else "."
        cycle += 1
        if len(output[-1]) == 40:
            output.append("")

        if DEBUG:
            for line in output:
                print(line)

            print(("." * (x-1)) + ("#" * 3))

        x += int(i[1])
        if (cycle + 20) % 40 == 0:
            sig_str.append((cycle * x))

        if DEBUG:
            print(("." * (x-1)) + ("#" * 3) + "\n")
            input()

print(sum(sig_str))

for line in output:
    print(line)
