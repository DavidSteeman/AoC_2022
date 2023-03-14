import numpy as np
from grid_part1 import Grid

with open('day23/input1', 'r') as file_handle:
    raw_input = file_handle.read().strip()
    grid = Grid(raw_input)

dirs = ['N', 'S', 'W', 'E']
num_elves = len(grid.elves)
free_elves = 0
num_rounds = 0

while True:
# for _ in range(10):
    num_rounds += 1
    free_elves = 0
    proposals = {}
    grid.minimize_grid_shape()
    
    # print(grid.elves)
    for elf_nr, loc in enumerate(grid.elves):
        blocked_sides = grid.check_around(loc)
        
        if not blocked_sides:
            free_elves += 1
            continue
        
        for side in dirs:
            if side in blocked_sides:
                continue
            direction = Grid.face_offsets[side][1]
            destination = (loc[0] + direction[0], loc[1] + direction[1])
            if destination in proposals:
                del proposals[destination]
                break
            proposals[destination] = (elf_nr, direction)
            break

    # print(proposals)
    for elf_nr, direction in proposals.values():
        # print(elf_nr, direction)
        grid.move_elf(elf_nr, direction)
    dirs.append(dirs.pop(0))
    if len(proposals) == 0:
        break
    # print(grid.grid)

grid.minimize_grid_shape()
print(grid.count_zeros())
print(num_rounds)