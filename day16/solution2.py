import numpy as np

with open('day16/input1', 'r') as file_handle:
    lines = file_handle.read().strip().split('\n')
    
lines = sorted(lines, key=lambda l: l[6:8])
for line in lines:
    print(line)