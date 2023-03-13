import numpy as np

with open('day20/input1', 'r') as file_handle:
    nums = [int(i) * 811589153 for i in file_handle.read().strip().split('\n')]
    
# linked_nums = [(nums[i], nums[i+1]) for i in range(len(nums)-1)]
# positions = {link: i for link, i in enumerate(linked_nums)}
nlen = len(nums)
positions = list(range(len(nums)))
mixed_nums = nums.copy()
print(nums)

for _ in range(10):
    for n in range(len(nums)):
        pos = positions.index(n)
        num = nums[n]
        new_pos = (pos + num)
        while new_pos >= nlen:
            new_pos = new_pos % (nlen - 1)
            # if new_pos > old_pos:
            #     new_pos -= 1
        while new_pos <= -nlen:
            new_pos = new_pos % (nlen -1)
            # if new_pos < old_pos:
            #     new_pos += 1
        old_pos = positions.pop(pos)
        positions.insert(new_pos, old_pos)
        mixed_nums.pop(pos)
        mixed_nums.insert(new_pos, num)
        # print(pos, old_pos, new_pos, num)
        # print(positions)
        # print(mixed_nums)

print(mixed_nums)
total = 0
zero_pos = mixed_nums.index(0)
print(zero_pos)
for i in range(1, 4):
    num = mixed_nums[(zero_pos + i * 1000) % nlen]
    print(num)
    total += num
print(total)
