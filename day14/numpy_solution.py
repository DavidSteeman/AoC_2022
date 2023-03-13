import numpy as np
from re import findall
from numba import njit

@njit
def index(array, item):
    for idx, val in np.ndenumerate(array):
        if val == item:
            return idx


with open('day14/input1', 'r') as file_handle:
    all = file_handle.read().strip()
    all_x = [int(i) for i in findall("([0-9]+),", all)]
    all_y = [int(i) for i in  findall(",([0-9]+)", all)]
    linemin = (min(all_x), min(all_y))
    linemax = (max(all_x), max(all_y))
    grid = np.full((max(all_y)+5, max([linemax[0]+5, 505])), '.', str)
    for line in all.split('\n'):
        points = [tuple(map(int, pos.split(',')))
                  for pos in line.strip().split(' -> ')]
        xs, ys = points[0]
        for i in range(1, len(points)):
            xe, ye = points[i]
            if xs == xe:
                ymin, ymax = (ys, ye) if ys < ye else (ye, ys)
                grid[ymin:ymax+1,xs] = "#"
            else:
                xmin, xmax = (xs, xe) if xs < xe else (xe, xs)
                grid[ys,xmin:xmax+1] = "#"
            xs, ys = xe, ye
    grid[0, 500] = '+'



ymax, xmax = grid.shape


def drop_grain(x, y):
    if 0 <= x < xmax and 0 < y < ymax:
        if grid[y+1, x-1] == '.':
            drop_grain(x-1, y+1)
        elif grid[y+1, x+1]

while True:
    x = 500
    
    for y in range(25):#linemax[1]+3):
        print("".join(grid[y, linemin[0]-2:linemax[0]+3]))
