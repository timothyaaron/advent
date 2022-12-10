class Crt:
    def __init__(self, debug=False):
        self.x = 1
        self.cycle = 0
        self.sig_str = []
        self.output = [""]
        self.debug = False

    def process(self, instruction):
        self.cycle += 1
        self.add_pixel()
        self.check_strength()

        if instruction[0] == "addx":
            self.cycle += 1
            self.add_pixel()
            self.x += int(instruction[1])
            self.check_strength()

    def add_pixel(self):
        cursor = (self.x - 1, self.x, self.x + 1)
        self.output[-1] += "#" if (self.cycle-1) % 40 in cursor else "."

        # reset output line
        if len(self.output[-1]) == 40:
            self.output.append("")

        # enable line-by-line display
        if self.debug:
            (print(line) for line in self.output)
            print(("." * (self.x-1)) + ("#" * 3) + "\n")
            input()

    def check_strength(self):
        if (self.cycle + 20) % 40 == 0:
            self.sig_str.append((self.cycle * self.x))


with open("input.txt") as f:
    instructions = [row.split() for row in f.read().splitlines()]

crt = Crt()
for i in instructions:
    crt.process(i)

print(f"Signal Strength: {sum(crt.sig_str)}")
for line in crt.output:
    print(line)
