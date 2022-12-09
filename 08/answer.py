import numpy


hidden_tree_coords = []
scenic_scores = []

with open("input.txt") as f:
    forest = numpy.array([[tree for tree in row] for row in f.read().splitlines()])

def append_if_hidden(x, y):
    # Look for a tree that will hide this one, from each direction
    # ... generator to prevent loading entire range
    # ... `next` bails at first find; `and` shortcuts if visible from one direction
    if (
        next((True for i in range(0, x) if forest[y][i] >= forest[y][x]), None) and
        next((True for i in range(x + 1, len(forest[0])) if forest[y][i] >= forest[y][x]), None) and
        next((True for j in range(0, y) if forest[j][x] >= forest[y][x]), None) and
        next((True for j in range(y + 1, len(forest)) if forest[j][x] >= forest[y][x]), None)
    ):
        hidden_tree_coords.append([x, y])


def score_scenicality(x, y):
    """In each direction, from the tree to the border, increment until blocked, multiply."""

    def count_trees(range):
        count = 0
        for tree in range:
            count += 1
            if tree >= forest[y][x]:
                break
        return count

    ranges = [
        forest[y, :x][::-1],  # west
        forest[y, x + 1:len(forest[0])],  # east
        forest[:y, x][::-1],  # north
        forest[y + 1:len(forest), x],  # south
    ]
    trees = [count_trees(range) for range in ranges]
    scenic_scores.append(numpy.prod(trees))


# for every tree inside the border…
for x in range(1, len(forest[0]) - 1):
    for y in range(1, len(forest) - 1):
        append_if_hidden(x, y)
        score_scenicality(x, y)

print((len(forest) * len(forest[0])) - len(hidden_tree_coords))
print(max(scenic_scores))
