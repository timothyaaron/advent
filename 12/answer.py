import string
from dataclasses import dataclass

import numpy

TOPO = string.ascii_lowercase


@dataclass
class Step:
    x: int
    y: int
    z: str
    visited = False
    start = False
    end = False

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        if z in TOPO:
            self.z = z
        elif z == "S":
            self.z = "a"
            self.start = True
        elif z == "E":
            self.z = "z"
            self.end = True

    def __repr__(self):
        return self.z

    def get_reachable_neighbors(self):
        neighbors = []
        if self.x > 0:
            neighbors.append(heightmap[self.y][self.x - 1])
        if self.x < len(heightmap[0]) - 1:
            neighbors.append(heightmap[self.y][self.x + 1])
        if self.y > 0:
            neighbors.append(heightmap[self.y - 1][self.x])
        if self.y < len(heightmap) - 1:
            neighbors.append(heightmap[self.y + 1][self.x])

        reachable = [
            n for n in neighbors
            if TOPO.index(n.z) <= TOPO.index(self.z) + 1 and not n.visited
        ]

        return [r for r in reachable if not r.visited]


    def hike(self):
        self.visited = True

        if not (neighbors := self.get_reachable_neighbors()):
            return [self]

        if end := next((n for n in neighbors if n.end), None):
            return [self, end]

        return [[self] + n.hike() for n in neighbors]



with open("input.txt") as f:
    heightmap = numpy.array([
        [Step(i, j, z) for i, z in enumerate(row)]
        for j, row in enumerate(f.read().splitlines())
    ])
start = next(s for s in heightmap.flatten() if s.start)
start.z = "a"
import pdb; pdb.set_trace()
trail_trees = start.hike()
complete_trails = [t for t in trail_trees if t[-1].end]

# output
print(heightmap)
print(start)