import numpy as np
from queue import LifoQueue

crate_stacks = dict()
with open('day05/input1', 'r') as file_handle:
    stacks, instructions = file_handle.read().split('\n\n')
    stacks = stacks.split('\n')
    instructions = instructions.strip().split('\n')
    
for i in range(len(stacks[-1])):
    char = stacks[-1][i]
    if char.isdigit():    
        stack = LifoQueue()
        for level in range(len(stacks) - 2, -1, -1):
            obj = stacks[level][i:i+1]
            if obj.isalpha():
                stack.put(obj)
        crate_stacks[int(char)] = stack

helper_stack = LifoQueue()
for line in instructions:
    _, nr_items, _, frm, _, to = line.split()
    nr_items, frm, to = map(int, (nr_items, frm, to))
    for _ in range(nr_items):
        helper_stack.put(crate_stacks[frm].get())
    while not helper_stack.empty():
        crate_stacks[to].put(helper_stack.get())
        
for stack in crate_stacks.values():
    if not stack.empty():
        print(stack.get(), end='')
print()
    
