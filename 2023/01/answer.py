with open("input.txt") as f:
    calibrations = [line.strip() for line in f]

total = 0
for c in calibrations:
    for first_char in c:
        if first_char.isdigit():
            break
    for last_char in c[::-1]:
        if last_char.isdigit():
            break
    total += int(f"{first_char}{last_char}")

print(total)
