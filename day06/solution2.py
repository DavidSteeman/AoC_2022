import numpy as np

with open('day06/input2', 'r') as file_handle:
    line = file_handle.read().strip()
    
quad = line[:14]
i = 14
while i < len(line):
    if len(set(quad)) == 14:
        break
    else:
        quad = quad[1:] + line[i]
        i += 1
        
print(i)
    