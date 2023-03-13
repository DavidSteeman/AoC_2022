import numpy as np

monkey_dict = dict()
with open('day21/input1', 'r') as file_handle:
    for line in file_handle.read().strip().split('\n'):
        name, op = line.split(': ')
        monkey_dict[name] = op
        
            
while not monkey_dict['root'].isdigit():
    for name, val in monkey_dict.items():
        if not val.isdigit():
            # print(val)
            mky1, op, mky2 = val.split(' ')
            val1 = monkey_dict[mky1]
            val2 = monkey_dict[mky2]
            if val1.isdigit() and val2.isdigit():
                result = int(eval(f'{val1} {op} {val2}'))
                monkey_dict[name] = str(result)

print(monkey_dict['root'])