def to_set(assignment):
    """e.g., turn the string "2-4" into the set {2,3,4}"""
    start, end = [int(x) for x in assignment.split("-")]
    return set(range(start, end + 1))

with open("input.txt") as f:
    """e.g., turn each "2-4,4-5" into a pair of sets [{2,3,4},{4,5}]"""
    assignments = [[to_set(a) for a in line.strip().split(",")] for line in f]

complete_overlaps = [(a1, a2) for a1, a2 in assignments if a1 <= a2 or a2 <= a1]
partial_overlaps = [(a1, a2) for a1, a2 in assignments if not a1.isdisjoint(a2)]

print(f"Complete Overlays:\n {len(complete_overlaps)}\n")
print(f"Partial Overlays:\n {len(partial_overlaps)}\n")
