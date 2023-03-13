from queue import SimpleQueue
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from time import sleep

with open('day18/input1', 'r') as file_handle:
    cubes = file_handle.read().strip().split('\n')

# grid in dims x, y, z  ---  {cube faces x-1, x+2, y-1, y+1, z-1, z+1}
grid = np.zeros([24,24,24])
visible_faces = np.zeros([24,24,24,6])
sides = [(-1, 0, 0), (0, -1, 0), (0, 0, -1), 
         (1, 0, 0), (0, 1, 0), (0, 0, 1)]

sides_frontier = SimpleQueue()
sides_visited = list()

xmax, ymax, zmax = 0, 0, 0

for cube in cubes:
    x, y, z = map(int, cube.split(','))
    grid[x][y][z] = 1
    if x > xmax: xmax = x
    if y > ymax: ymax = y
    if z > zmax: zmax = z


for x in range(xmax+1):
    for y in range(ymax+1):
        hits = [z for z in range(zmax+1) if grid[x][y][z] == 1]
        if hits:
            sides_frontier.put((x, y, hits[0], 2))
            sides_frontier.put((x, y, hits[-1], 5))
            

for y in range(ymax+1):
    for z in range(zmax+1):
        hits = [x for x in range(xmax+1) if grid[x][y][z] == 1]
        if hits:
            sides_frontier.put((hits[0], y, z, 0))
            sides_frontier.put((hits[-1], y, z, 3))
            

for x in range(xmax+1):
    for z in range(zmax+1):
        hits = [y for y in range(ymax+1) if grid[x][y][z] == 1]
        if hits:
            sides_frontier.put((x, hits[0], z, 1))
            sides_frontier.put((x, hits[-1], z, 4))
            

while sides_frontier.qsize() > 0:
    # print(visible_faces)
    next = sides_frontier.get()
    x, y, z, face = next
    # visible_faces[x][y][z][face] = 1
    back = (face + 3) % 6
    face_axis = face % 3
    # print(next, back, face_axis, "reeeeeeeeeeeeeeeeee")
        
    for side in range(6):
        if side == back or side == face:
            continue
        opp = (side + 3) % 6
        mod = sides[side]
        nbd_coords = [x + mod[0], y + mod[1], z + mod[2]]
        nbd_coords[face_axis] += (1 if face > 2 else -1)
        xd, yd, zd = nbd_coords
        # print(f"({x}, {y}, {z})", face, side, opp, f"({xd}, {yd}, {zd})", "go: ", end='')
        if grid[xd][yd][zd] == 1:
            if visible_faces[xd][yd][zd][opp] == 0:
                # print("hurp", xd, yd, zd, end='')
                sides_frontier.put((xd, yd, zd, opp))
                visible_faces[xd][yd][zd][opp] = 1
        else: 
            nbd_coords[face_axis] -= (1 if face > 2 else -1)
            xn, yn, zn = nbd_coords
            # print(f" ({xn}, {yn}, {zn}) ", end="")
            if grid[xn][yn][zn] == 0:
                # print("ya... ", end="")
                if visible_faces[x][y][z][side] == 0:   
                    # print("durp", xn, yn, zn, end='')
                    sides_frontier.put((x, y, z, side))
                    visible_faces[x][y][z][side] = 1
            elif visible_faces[xn][yn][zn][face] == 0:
                # print("slurp", xn, yn, zn, end='')
                sides_frontier.put((xn, yn, zn, face))
                visible_faces[xn][yn][zn][face] = 1
        # print()
    # sleep(0.1)
    
# for x in range(7):
#     for y in range(7):
#         for z in range(7):
#             for s in range(6):
#                 if visible_faces[x][y][z][s] == 1:
#                     print(x, y, z, s)
      
print(np.count_nonzero(visible_faces))
        
# From outer faces of cube looking in at block structure, just check each point along each axis and see if you hit a block
# Problem: holes in the structure will be invisible from some or all sides


    
            
        
    


