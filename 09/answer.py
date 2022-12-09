import math

import numpy
from dataclasses import dataclass


@dataclass
class Point:
    x: str
    y: str


class Step:
    def __init__(self, x, y, head, tail):
        self.x = x
        self.y = y
        self.value = 0
        self.head = head
        self.tail = tail

    def __repr__(self):
        return str(self.value)

    def start_here(self):
        self.head.x = self.tail.x = self.x
        self.head.y = self.tail.y = self.y
        self.value = 1

    def step_here(self):
        dist = math.sqrt((self.x - self.tail.x)**2 + (self.y - self.tail.y)**2)
        if dist >= 2:
            self.tail.x = self.head.x
            self.tail.y = self.head.y
            bridge[self.tail.y][self.tail.x].value = 1

        self.head.x = self.x
        self.head.y = self.y

        # bridge[tail[1]][tail[0]].val = 1


with open("input.txt") as f:
    steps = [row.split() for row in f.read().splitlines()]

# calculate array size
h = v = left = right = top = bottom = 0
for s in steps:
    match s:
        case "U", val:
            v += int(val)
            top = max(v, top)
        case "D", val:
            v -= int(val)
            bottom = min(v, bottom)
        case "R", val:
            h += int(val)
            right = max(h, right)
        case "L", val:
            h -= int(val)
            left = min(h, left)

width = right - left + 1
height = top - bottom + 1
head = Point(-left, -bottom)
tail = Point(-left, -bottom)
bridge = numpy.array([
    [Step(x, y, head, tail) for x in range(width)] for y in range(height)
])


# calculate starting position
hx = tx = -left
hy = ty = -bottom
bridge[ty][tx].start_here()

# process input
for s in steps:
    match s[0], int(s[1]):
        case "U", val:
            for b in bridge[hy + 1:hy + val + 1, hx]:
                b.step_here()
            hy += int(val)
        case "D", val:
            for b in bridge[hy - val:hy, hx][::-1]:
                b.step_here()
            hy -= int(val)
        case "R", val:
            for b in bridge[hy, hx + 1:hx + val + 1]:
                b.step_here()
            hx += int(val)
        case "L", val:
            for b in bridge[hy, hx - val:hx][::-1]:
                b.step_here()
            hx -= int(val)

print(bridge)
print(sum([s.value for row in bridge for s in row]))