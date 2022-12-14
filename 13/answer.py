from dataclasses import dataclass

import numpy


with open("input.txt") as f:
    packets = numpy.array([[l for l in line.split("[")] for line in f.read().splitlines()])

# output
import pdb; pdb.set_trace()
print(packets)