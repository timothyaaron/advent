with open("input.txt") as f:
    # list of each load (string)
    elves = f.read().strip().split('\n\n')

    # get the sum of those strings (split and cast to ints)
    calories = [sum(map(int, e.split('\n'))) for e in elves]

print(f"Most calories: {max(calories)}")
print(f"Top 3: {sum(sorted(calories)[-3:])}")
