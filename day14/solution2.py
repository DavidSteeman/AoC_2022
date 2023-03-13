from re import findall

with open('day14/input1', 'r') as file_handle:
    all = file_handle.read().strip()
    all_x = [int(i) for i in findall("([0-9]+),", all)]
    all_y = [int(i) for i in  findall(",([0-9]+)", all)]
    linemin = (min(all_x), min(all_y))
    linemax = (max(all_x), max(all_y))
    
    grid = {(x, y): '.' 
            for x in range(linemin[0]-200, linemax[0]+201)
            for y in range(0, linemax[1]+3)}
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
    for x in range(linemin[0]-200, linemax[0]+201):
        grid[(x, linemax[1]+2)] = '#'

xmax, ymax = linemax


def drop_grain(x, y):
    down =  grid.get((x, y), None)
    if not down:
        print("HWAT")
        return 0
    elif down == '.':
        return drop_grain(x, y+1)
    elif down in 'o#':
        if (x, y) == (500, 0):
            print("DONE!")
            return 0
        downleft = grid.get((x-1, y), None)
        downright = grid.get((x+1, y), None)
        if not downleft or not downright:
            print("HHHWAT?")
            return 0
        if downleft == '.' :
            return drop_grain(x-1, y+1)
        elif downright == '.':
            return drop_grain(x+1, y+1)
        else:
            grid[(x, y-1)] = 'o'
            return 1
    return 0

total_grains = 0
while True: 
    landed = drop_grain(500, 0)
    if not landed:
        break
    total_grains += landed
    # for y in range(12):#linemax[1]+3):
    #     for x in range(linemin[0]-10, linemax[0]+11):
    #         print(grid.get((x, y), '.'), end='')
    #     print()
    # print()

print(total_grains)
