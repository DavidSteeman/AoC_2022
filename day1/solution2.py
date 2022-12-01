import numpy as np

with open('day1/input1', 'r') as file_handle:
    elves = [sum(map(int, i.split('\n'))) for i in 
             file_handle.read().split('\n\n')]
    
print(sum(sorted(elves)[-3:]))

