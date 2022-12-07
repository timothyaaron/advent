DISKSPACE = 70000000
NEEDED = 30000000

with open("input.txt") as f:
    commands = f.read().splitlines()

class Dir:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = {}
        self.files = {}

    @property
    def size(self):
        """Total size of files + children directories"""
        return sum(
            list(self.files.values()) +
            [dir.size for dir in self.children.values()]
        )

    @property
    def descendants(self):
        children = list(self.children.values())
        return children + [grand for child in children for grand in child.descendants]

    def my_dirs_at_most_100k(self):
        children_total = sum(c.my_dirs_at_most_100k() for c in self.children.values())
        return children_total + (self.size if self.size <= 100000 else 0)

current = root = Dir("/")
while commands and (command := commands.pop(0)):
    x = command.split()
    match command.split():
        case ["$", "cd", "/"]:
            current = root
        case ["$", "cd", ".."]:
            current = current.parent
        case ["$", "cd", dir]:
            if dir not in current.children:
                current.children[dir] = Dir(dir, parent=current)
            current = current.children[dir]
        case ["$", "ls"]: pass  # ignore "$ ls"
        case ["dir", _]: pass  # ignore "dir"s `ls`-ed
        case [filesize, filename]:
            current.files[filename] = int(filesize)

print(root.my_dirs_at_most_100k())

# sort dirs by size, get first over needed space
sorted_dirs = sorted([root] + root.descendants, key=lambda dir: dir.size)
missing = NEEDED - (DISKSPACE - root.size)
print(next(d.size for d in sorted_dirs if d.size >= missing))
