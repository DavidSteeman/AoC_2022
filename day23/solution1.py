import numpy as np
from grid_part1 import Grid

with open('day23/input1', 'r') as file_handle:
    raw_input = file_handle.read().strip()
    grid = Grid(raw_input)

dirs = ['N', 'S', 'W', 'E']
num_elves = len(grid.elves)
free_elves = 0

# while free_elves < num_elves:
for _ in range(10):
    free_elves = 0
    proposals = {}
    print(grid.count_zeros())
    
    print(grid.elves)
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

    print(proposals)
    for elf_nr, direction in proposals.values():
        print(elf_nr, direction)
        grid.move_elf(elf_nr, direction)
    dirs.append(dirs.pop(0))
    print(grid.grid)

print(grid.count_zeros())