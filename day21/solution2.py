

monkey_dict = dict()
with open('day21/input1', 'r') as file_handle:
    for line in file_handle.read().strip().split('\n'):
        name, op = line.split(': ')
        if name == 'humn':
            op = '111111111'
        monkey_dict[name] = op

# monkey_paths = dict()
# for monkey in monkey_dict:
#     if not monkey_dict[monkey].isdigit():
        

v2 = 40608253763172

m1, op, m2 = monkey_dict['root'].split(' ')
monkey_paths = {m1: [], m2: []}
for name in [m1, m2]:
    monkey_queue = [name]
    while not len(monkey_queue) == 0:
        monkey = monkey_queue.pop(0)
        val = monkey_dict[monkey]
        if not val.isdigit():
            mky1, op, mky2 = val.split(' ')
            monkey_queue.extend([mky1, mky2])
        monkey_paths[name].append(monkey)
        
fixed_path = m1 if 'humn' in monkey_paths[m2] else m2
target_path = m1 if fixed_path == m2 else m2
print(fixed_path)
print('humn' in monkey_paths[fixed_path])


def resolve_path(path, mky):
    while not monkey_dict[mky].isdigit():
        for name in path:
            val = monkey_dict[name]
            if not val.isdigit():
                mky1, op, mky2 = val.split(' ')
                val1 = monkey_dict[mky1]
                val2 = monkey_dict[mky2]
                if val1.isdigit() and val2.isdigit():
                    result = int(eval(f'{val1} {op} {val2}'))
                    monkey_dict[name] = str(result)
      
                
resolve_path(monkey_paths[fixed_path], fixed_path)                
target = float(monkey_dict[fixed_path])
print(target)
equation = ''
mq = [target_path]

def resolve(name):
    val = monkey_dict[name]
    if name == 'humn':
        return 'humn'
    elif val.isdigit():
        return val
    else:
        mky1, op, mky2 = val.split(' ')
        resolved_1 = resolve(mky1)
        resolved_2 = resolve(mky2)
        if 'humn' in resolved_1:
            return f'({resolved_1} {op} {resolved_2})'
        elif 'humn' in resolved_2:
            return f'({resolved_1} {op} {resolved_2})'
        else:
            return str(eval(resolved_1+op+resolved_2))
            

eq = resolve(target_path)
solution = 0
for i in range(3330805290000, 3330805300000):
    new_eq = eq[::].replace('humn', str(i))
    result = eval(new_eq)
    # print(result, i)
    if result == target:
        solution = i
print(target)
print(solution)

# while not monkey_dict['tjtt'].isdigit():
#     for name, val in monkey_dict.items():
#         if not (val.isdigit() or val[0] == '-'):
#             # print(val)
#             mky1, op, mky2 = val.split(' ')
#             if mky1 == 'humn' or mky2 == 'humn':
#                 continue
#             val1 = monkey_dict[mky1]
#             val2 = monkey_dict[mky2]
#             if (val1.isdigit() or val1[0] == '-') and (val2.isdigit() or val2[0] == '-'):
#                 if name == 'tjtt':
#                     print(val1, op, val2)
#                 result = int(eval(f'{val1} {op} {val2}'))
#                 monkey_dict[name] = str(result)

# print(monkey_dict['tjtt'])