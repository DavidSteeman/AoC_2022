import numpy as np

with open('day06/input1', 'r') as file_handle:
    line = file_handle.read().strip()
    
quad = line[:4]
i = 4
while i < len(line):
    if len(set(quad)) == 4:
        break
    else:
        quad = quad[1:] + line[i]
        i += 1
        
print(i)
    