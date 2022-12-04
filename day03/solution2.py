from collections import Counter

with open('day03/input1', 'r') as file_handle:
    lines = file_handle.read().strip().split('\n')
    
prio_dict = dict(zip(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'), range(1, 53)))

total = 0
for i in range(0, len(lines), 3):
    common_item = (set(lines[i]) & set(lines[i+1]) & set(lines[i+2])).pop()
    total += prio_dict[common_item]
    # print(common_item)
    
print(total)