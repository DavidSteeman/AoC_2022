import sys
sys.setrecursionlimit(3000)


class Path:
    def __init__(self, name, parent=None, size=0, type='dir') -> None:
        self.name = name
        self.size = size
        self.parent = parent
        self.children = dict()
        self.type = type
        
    def add_child(self, child):
        if child.name not in self.children:
            self.children[child.name] = child
    
    def goto_child(self, name):
        return self.children[name]
    
    def get_total_size(self):
        size = self.size
        for path in self.children.values():
            size += path.get_total_size()
        return size


with open('day07/input1', 'r') as file_handle:
    lines = file_handle.read().split('\n')


parent_dir = None
root = Path('/')
current_dir = root

for line in lines:
    match line.split():
        case ['$', 'cd', '/']:
            current_dir = root
        case ['$', 'cd', '..']:
            current_dir = current_dir.parent
        case ['$', 'cd', dirname]:
            current_dir.add_child(Path(dirname, current_dir))
            current_dir = current_dir.goto_child(dirname)
        case ['dir', dirname]:
            current_dir.add_child(Path(dirname, current_dir))
        case [size, name] if size.isdigit():
            current_dir.add_child(Path(name, current_dir, int(size), 'file'))
        case _:
            print(line)

sizes_under_100k = []


def traverse(dir):
    size = dir.get_total_size()
    if size < 100000:
        sizes_under_100k.append(size)
    for child in dir.children.values():
        if child.type == 'dir':
            traverse(child)

traverse(root)
print(sum(sizes_under_100k))
