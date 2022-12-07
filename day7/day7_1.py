from functools import cache


class Dir:
    def __init__(self, parent):
        self.parent = parent

        self.subdirs = {}
        self.files = {}


main, current = None, None
line = input()

while line:
    match line.strip().split():
        case ['$', 'cd', '/']:
            main = current = Dir(parent=None)
            line = input()

        case ["$", "cd", ".."]:
            current = current.parent
            line = input()

        case ["$", "cd", dir]:
            current = current.subdirs[dir]
            line = input()

        case ["$", "ls"]:
            line = input()

            while line:
                match line.strip().split():
                    case ["$", *rest]: break

                    case ["dir", dir]:
                        current.subdirs[dir] = Dir(current)
                        line = input()

                    case [size, filename]:
                        current.files[filename] = size
                        line = input()

sizes = {}

@cache
def total_valid_size(dir):
    size = 0

    for subdir in dir.subdirs.values():
        size += total_valid_size(subdir)

    for file in dir.files.values():
        size += int(file)

    sizes[dir] = size
    return size

total_valid_size(main)
print(sum(x for x in sizes.values() if x <= 1e5))
