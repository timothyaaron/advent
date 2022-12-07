with open("input.txt") as f:
    ds = f.read().strip()
    print(next(i for i in range(4, len(ds)) if len(set(ds[i-4:i])) == 4))
    print(next(i for i in range(14, len(ds)) if len(set(ds[i-14:i])) == 14))
