hidden_tree_coords = []
scenic_scores = []

with open("input.txt") as f:
    forest = [[tree for tree in row] for row in f.read().splitlines()]


def check_hidden(x, y):
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
    north = south = east = west = 0
    height = forest[y][x]

    for tree in forest[y][0:x][::-1]:
        west += 1
        if tree >= height:
            break

    for tree in forest[y][x + 1:len(forest[0])]:
        east += 1
        if tree >= height:
            break

    for j in range(y)[::-1]:
        north += 1
        if forest[j][x] >= height:
            break

    for j in range(y + 1, len(forest)):
        south += 1
        if forest[j][x] >= height:
            break

    scenic_scores.append(west * east * south * north)


# for every tree inside the border…
for x in range(1, len(forest[0]) - 1):
    for y in range(1, len(forest) - 1):
        check_hidden(x, y)
        score_scenicality(x, y)

print((len(forest) * len(forest[0])) - len(hidden_tree_coords))
print(max(scenic_scores))
