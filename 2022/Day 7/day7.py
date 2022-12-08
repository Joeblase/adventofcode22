def get_input(puzzle_input):
    with open(puzzle_input) as input_file:
        input_list = input_file.read().splitlines()
    return input_list


class Folder:
    def __init__(self, name, index):
        self.name = name
        self.items = []
        self.index = index
        self.size = 0


class File:
    def __init__(self, name, size, index):
        self.name = name
        self.size = size
        self.index = index


def create_filesystem(puzzle_input):
    terminal_output = get_input(puzzle_input)
    cd = Folder('/', 0)
    location = [cd]
    for line in terminal_output:
        if line[:4] == '$ cd':
            if line[:6] == '$ cd /':
                pass
            elif line[:7] == '$ cd ..':
                location.pop()
                location[-1].items[cd.index] = cd
                cd = location[-1]
            else:
                for item in cd.items:
                    if item.name == line[5:]:
                        cd = item
                        break
                location.append(cd)
        if line[:4] == '$ ls':
            index = 0
        if line[0] in '1234567890':
            size = ''
            file_name = ''
            for char in line:
                if char.isdigit():
                    size += char
                elif char != '':
                    file_name += char
            cd.items.append(File(file_name, int(size), index))
            index += 1
        if line[:3] == 'dir':
            cd.items.append(Folder(line[4:], index))
            index += 1
    while len(location) > 1:
        location.pop()
        location[-1].items[cd.index] = cd
        cd = location[-1]

    def directory_sizes(folder):
        for item in folder.items:
            if isinstance(item, Folder) and item.size == 0:
                directory_sizes(item)
        for item in folder.items:
            folder.size += item.size
        if folder.size != 0:
            return folder
        directory_sizes(folder)

    return directory_sizes(cd)


def list_directory_sizes(puzzle_input):
    root = create_filesystem(puzzle_input)
    directory_sizes = []

    def directory_sizes_recursive(folder):
        for item in folder.items:
            if isinstance(item, Folder):
                directory_sizes.append(item.size)
                directory_sizes_recursive(item)

    directory_sizes_recursive(root)
    return directory_sizes


def max_100000(list_):
    new_list = []
    for num in list_:
        if num <= 100000:
            new_list.append(num)
    return new_list


def determine_deletion(puzzle_input):
    remaining_space = (70000000 - create_filesystem(puzzle_input).size)
    directory_sizes = list_directory_sizes(puzzle_input)
    possible_folders = []
    for size in directory_sizes:
        if remaining_space + size >= 30000000:
            possible_folders.append(size)
    return min(possible_folders)


print(f"The sum of the sizes of directories that are at most 100000 is: "
      f"{sum(max_100000(list_directory_sizes('input.txt')))}")
# The sum of the sizes of directories that are at most 100000 is: 1391690

print(f"The smallest directory that would free up enough space is size: {determine_deletion('input.txt')}")
# The smallest directory that would free up enough space is size: 5469168
