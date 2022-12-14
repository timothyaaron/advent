from dataclasses import dataclass

import numpy


@dataclass
class Point:
    x: int = 0
    y: int = 0

    def __init__(self, coord, kind="."):
        self.x, self.y = map(int, coord.split(','))
        self.kind = kind

    def __repr__(self):
        return self.kind


with open("input.txt") as f:
    paths = numpy.array([
        [Point(coord, "#") for coord in line.split(" -> ")]
        for line in f.read().splitlines()
    ])
    import pdb; pdb.set_trace()
    min_x = min([min([p.x for p in ps]) for ps in paths.flatten()])
    max_x = max([max([p.x for p in ps]) for ps in paths.flatten()])
    min_y = min([min([p.y for p in ps]) for ps in paths.flatten()])
    max_y = max([max([p.y for p in ps]) for ps in paths.flatten()])

    scan = numpy.array([
        [Point(f"{x},{y}") for x in range(max_x - min_x)]
        for y in range(max_y - min_y)
    ])

    for path in enumerate(paths):
        for i, point in enumerate(path[:-1]):
            if point.x > path[i + 1].x:
                pass
            elif point.x < path[i + 1].x:
                pass
            else:
                pass

# output
print(scan)