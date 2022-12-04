import numpy as np

with open('day04/input1', 'r') as file_handle:
    pairs = [[list(map(int, j.split('-'))) 
              for j in i.strip().split(',')] 
             for i in file_handle.readlines()]
    
full_overlaps = 0
for pair in pairs:
    sec1_start, sec1_end = pair[0]
    sec2_start, sec2_end = pair[1]
    if ((sec2_start >= sec1_start and sec2_end <= sec1_end) or
        (sec1_start >= sec2_start and sec1_end <= sec2_end)):
        full_overlaps += 1
        
print(full_overlaps)