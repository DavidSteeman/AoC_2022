from re import search

MONKEYS = dict()

class Monkey:
    def __init__(self, id, starting_items, operation, test, 
                 true_target, false_target) -> None:
        self.id = id
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.true_target = true_target
        self.false_target = false_target
        self.inspect_count = 0
        
    def add_item(self, item):
        self.items.append(item)
        
    def inspect(self, item):
        self.inspect_count += 1
        return self.operation(item)
    
    def turn(self):
        while self.items:
            old_item = self.items.pop(0)
            new_item = self.inspect(old_item)
            if self.test(new_item):
                target = self.true_target
            else:
                target = self.false_target
            # print(f"Monkey {self.id}, old item: {old_item}, "
            #       f"divby 19: {self.test(new_item)}, new_item: {new_item}, throwing to {target}")
        
            MONKEYS[target].add_item(new_item)


def get_opfunc(opstr):
    operation = lambda x: x
    ops = search('new = old (.) (.+)$', opstr)
    match ops.groups():
        case ('+', 'old'): operation = lambda x: x + x
        case ('*', 'old'): operation = lambda x: x * x
        case ('/', 'old'): operation = lambda x: int(x / x)
        case ('+', y): operation = lambda x: x + int(y)
        case ('*', y): operation = lambda x: x * int(y)
        case ('/', y): operation = lambda x: int(x / int(y))
    return operation
    

def get_testfunc(teststr):
    divby = int(teststr.strip().split()[-1])
    test = lambda x: x % int(divby) == 0
    return test


with open('day11/input1', 'r') as file_handle:
    monks = file_handle.read().strip().split('\n\n')


for monkey in monks:
    lines = monkey.split('\n')
    id = int(lines[0].strip(':').split()[-1])
    items = [int(i) for i in lines[1][18:].strip().split(', ')]
    operation = get_opfunc(lines[2])
    test = get_testfunc(lines[3])
    true_target = int(lines[4].strip().split()[-1])
    false_target = int(lines[5].strip().split()[-1])
    MONKEYS[id] = Monkey(id, items, operation, test, true_target, false_target)

# print(sorted(list(MONKEYS.keys())))
ids = sorted(list(MONKEYS.keys()))
for _ in range(20):
    for id in ids:
        MONKEYS[id].turn()
# for id in ids:
#     print(MONKEYS[id].items)
#     print(MONKEYS[id].inspect_count)
counts = sorted([MONKEYS[id].inspect_count for id in ids], reverse = True)
print(counts[0] * counts[1])