import json
import operator
import sys

import numpy

sys.set_int_max_str_digits(1000000)

ROUNDS = 20
OPS = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}


def operate(operation, i):
    *_, x, op, y = operation.strip().split()
    x = i if x == "old" else x
    y = i if y == "old" else y
    return OPS[op](int(x), int(y)) // 3


def perform(instruction, round, monkeys, current):
    match instruction:
        case [monkey, ""]:
            id = int(monkey.split()[-1])
            monkeys[id] = current = monkeys.get(id, {"items": [], "counter": 0})

        case ["Starting items", items]:
            if round == 0:
                current["items"] = [int(i) for i in items.strip().split(", ")] + current["items"]

        case ["Operation", operation]:
            current["post_op"] = [operate(operation, i) for i in current["items"]]
            current["counter"] += len(current["items"])

        case ["Test", test]:
            current["dividend"] = int(test.split()[-1])
            current["results"] = [int(i) % current["dividend"] == 0 for i in current["post_op"]]

        case ["If true", true_string]:
            true_id = int(true_string.split()[-1])
            monkeys[true_id] = monkeys.get(true_id, {"items": [], "counter": 0})
            lcm = numpy.prod([monkeys.get(i, {}).get("dividend", 0) for i in range(8)])
            monkeys[true_id]["items"] += [
                current["post_op"][i] if not lcm or current["post_op"][i] % lcm != 0 else current["post_op"][i] // lcm
                for i, r in enumerate(current["results"]) if r
            ]

        case ["If false", false_string]:
            false_id = int(false_string.split()[-1])
            monkeys[false_id] = monkeys.get(false_id, {"items": [], "counter": 0})
            monkeys[false_id]["items"] += [
                current["post_op"][i]
                for i, r in enumerate(current["results"]) if not r
            ]

            current["items"] = []
            current["post_op"] = []
            current["results"] = []

    return current


with open("input.txt") as f:
    instructions = [row.strip().split(":") for row in f.read().splitlines()]

monkeys = {}
current = None

for round in range(ROUNDS):
    for instruction in instructions:
        current = perform(instruction, round, monkeys, current)

    print(f"Round {round}")

    # for m in monkeys.values():
    #     print(m["items"])
    # input()

print(operator.mul(*sorted([m["counter"] for m in monkeys.values()])[-2:]))
# print(json.dumps(monkeys, indent=4))

# 122758 too low
# 14635822550 too low
# 15123279330 too high