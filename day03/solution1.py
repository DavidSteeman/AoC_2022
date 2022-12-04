from collections import Counter

with open('day03/input1', 'r') as file_handle:
    lines = file_handle.read().strip().split('\n')
    
prio_dict = dict(zip(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'), range(1, 53)))
print(prio_dict)
total = 0
for line in lines:
    comp_1 = line[:int(len(line) / 2)]
    comp_2 = line[int(len(line) / 2):]
    common_item = (set(comp_1) & set(comp_2)).pop()
    total += prio_dict[common_item]
    
print(total)