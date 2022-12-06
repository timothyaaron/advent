import copy


with open("input.txt") as f:
    crappy_input = f.read().splitlines()

# parse the crappy stack input structure
stacks = [[] for _ in range(9)]
while level := crappy_input.pop(0):
    for i in range(len(level)//4+1):
        if crate := level[i*4+1].strip():
            stacks[i] = [crate] + stacks[i]
[stack.pop(0) for stack in stacks]  # get rid of the number row

# copy stacks and remaining crappy input structure (i.e., procedures) for part 2
same_stacks = copy.deepcopy(stacks)
same_crappy_input = copy.deepcopy(crappy_input)

# parse each crappy procedure input
for procedure in crappy_input:
    count, from_, to_ = map(int, filter(lambda x: x.isnumeric(), procedure.split()))
    stacks[to_ - 1] += [stacks[from_ - 1].pop() for _ in range(count)]

print("".join([stack[-1] for stack in stacks]))

# parse each crappy procedure input, reverse the stack
for procedure in same_crappy_input:
    count, from_, to_ = map(int, filter(lambda x: x.isnumeric(), procedure.split()))
    same_stacks[to_ - 1] += reversed([same_stacks[from_ - 1].pop() for _ in range(count)])

print("".join([stack[-1] for stack in same_stacks]))
