with open("input.txt") as f:
    assignments = [line.strip().split(",") for line in f]  # list of ["2-4", "3-4"]

complete_overlaps = []
partial_overlaps = []
for a1, a2 in assignments:
    # turn each assignment ("2-4") into a set of integers ({2,3,4})
    a1_sections = {i for i in range(int(a1.split("-")[0]), int(a1.split("-")[1]) + 1)}
    a2_sections = {i for i in range(int(a2.split("-")[0]), int(a2.split("-")[1]) + 1)}

    # add to `complete` if either set is a subset of the other
    if a1_sections.issubset(a2_sections) or a2_sections.issubset(a1_sections):
        complete_overlaps.append([a1, a2])

    # add to `partial` if no sections appear in both sets
    if not a1_sections.isdisjoint(a2_sections):
        partial_overlaps.append([a1, a2])

print(f"Complete Overlays:\n {len(complete_overlaps)}\n")
print(f"Partial Overlays:\n {len(partial_overlaps)}\n")
