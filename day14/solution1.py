from re import findall

with open('day14/input1', 'r') as file_handle:
    all = file_handle.read().strip()
    all_x = [int(i) for i in findall("([0-9]+),", all)]
    all_y = [int(i) for i in  findall(",([0-9]+)", all)]
    linemin = (min(all_x), min(all_y))
    linemax = (max(all_x), max(all_y))
    
    grid = {(x, y): '.' 
            for x in range(linemin[0], linemax[0]+1)
            for y in range(0, linemax[1]+1)}
    for line in all.split('\n'):
        points = [tuple(map(int, pos.split(',')))
                  for pos in line.strip().split(' -> ')]
        xs, ys = points[0]
        for i in range(1, len(points)):
            xe, ye = points[i]
            if xs == xe:
                ymin, ymax = (ys, ye) if ys < ye else (ye, ys)
                for y in range(ymin, ymax+1):
                    grid[(xs, y)] = "#"
            else:
                xmin, xmax = (xs, xe) if xs < xe else (xe, xs)
                for x in range(xmin, xmax+1):
                    grid[(x, ys)] = "#"
            xs, ys = xe, ye
    grid[500, 0] = '+'



xmax, ymax = linemax


def drop_grain(x, y):
    down =  grid.get((x, y+1), None)
    if not down:
        return 0
    elif down == '.':
        return drop_grain(x, y+1)
    elif down in 'o#':
        downleft = grid.get((x-1, y+1), '.')
        downright = grid.get((x+1, y+1), '.')
        if downleft == '.' :
            return drop_grain(x-1, y+1)
        elif downright == '.':
            return drop_grain(x+1, y+1)
        elif down:
            grid[(x, y)] = 'o'
            return 1
    return 0

total_grains = 0
while True:
    # for y in range(10):#linemax[1]+3):
    #     for x in range(linemin[0], linemax[0]+1):
    #         print(grid[(x, y)], end='')
    #     print()
    landed = drop_grain(500, 1)
    total_grains += landed
    if not landed:
        break

print(total_grains)
