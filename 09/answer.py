import math
from dataclasses import dataclass

import numpy

DEBUG = False


@dataclass
class Point:
    x: str
    y: str


class Step:
    def __init__(self, x, y, rope):
        self.x = x
        self.y = y
        self.value = " "
        self.rope = rope

    def __repr__(self):
        return str(self.value)

    def step_here(self):
        # move the head
        if DEBUG and bridge[rope[0].y][rope[0].x].value != len(rope) - 1:
            bridge[rope[0].y][rope[0].x].value = " "
        rope[0].x = self.x
        rope[0].y = self.y
        if DEBUG:
            bridge[self.y][self.x].value = 0

        # for each follower
        for i, follower in enumerate(self.rope[1:]):
            # is the follower 2 squares away from its leader?
            dist = math.sqrt(
                (follower.x - self.rope[i].x)**2 +
                (follower.y - self.rope[i].y)**2
            )
            if dist >= 2:
                if bridge[follower.y][follower.x].value != len(rope) - 1:
                    bridge[follower.y][follower.x].value = " "

                if rope[i].x > follower.x:
                    follower.x += 1
                elif rope[i].x < follower.x:
                    follower.x -= 1

                if rope[i].y > follower.y:
                    follower.y += 1
                elif rope[i].y < follower.y:
                    follower.y -= 1

                if DEBUG or i == len(rope) - 2:
                    bridge[follower.y][follower.x].value = i + 1

            else:
                break

        if DEBUG:
            # add in rope
            for i, r in enumerate(rope[::-1]):
                bridge[r.y][r.x].value = len(rope) - i - 1

            print(f"{bridge}\n")
            input()


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
rope = [Point(-left, -bottom) for _ in range(10)]
bridge = numpy.array([
    [Step(x, y, rope) for x in range(width)] for y in range(height)
])
bridge[rope[-1].y][rope[-1].x].value = 9

# process input
for s in steps:
    print(s)
    match s[0], int(s[1]):
        case "U", val:
            for b in bridge[rope[0].y + 1:rope[0].y + val + 1, rope[0].x]:
                b.step_here()
        case "D", val:
            for b in bridge[rope[0].y - val:rope[0].y, rope[0].x][::-1]:
                b.step_here()
        case "R", val:
            for b in bridge[rope[0].y, rope[0].x + 1:rope[0].x + val + 1]:
                b.step_here()
        case "L", val:
            for b in bridge[rope[0].y, rope[0].x - val:rope[0].x][::-1]:
                b.step_here()

print(bridge)
print(f"{len(bridge[0])} x {len(bridge)}")
print(sum([1 if s.value == (len(rope) - 1) else 0 for row in bridge for s in row]))
