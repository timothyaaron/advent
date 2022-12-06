priority = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("input.txt") as f:
    rucksacks = [list(line.strip()) for line in f]

# split the lists in half, set+intersection to find the unique character
items = [
    (set(r[:len(r)//2]) & set(r[len(r)//2:])).pop()
    for r in rucksacks
]
print(sum([priority.index(i) for i in items]))

# loop over every 3 rucksacks, set+intersection the unique character
items = [
    (set(rucksacks[3*i]) & set(rucksacks[3*i+1]) & set(rucksacks[3*i+2])).pop()
    for i in range(len(rucksacks)//3)
]
print(sum([priority.index(i) for i in items]))
