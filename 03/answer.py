priority = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def unique(first, *the_rest):
    """turn 2+ lists in sets, intersect, and return the found character"""
    return set(first).intersection(*map(set, the_rest)).pop()

with open("input.txt") as f:
    sacks = [list(line.strip()) for line in f]

# split the lists in half, set+intersection to find the unique character
items = [unique(sack[:len(sack)//2], sack[len(sack)//2:]) for sack in sacks]
print(sum([priority.index(i) for i in items]))

# loop over every 3 sacks, set+intersection to find the unique character
items = [unique(sacks[3*i], sacks[3*i+1], sacks[3*i+2]) for i in range(len(sacks)//3)]
print(sum([priority.index(i) for i in items]))
