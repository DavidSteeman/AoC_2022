def print_grid(hloc, tloc):
    print()
    for y in range(5):
        for x in range(6):
            if x == hloc[0] and y == 4 - hloc[1]:
                print('H', end='')
                if hloc == tloc:
                    continue
            elif x == tloc[0] and y == 4 - tloc[1]:
                print('T', end='')
            else:
                print('.', end='')
        print()
    print()
        
            

with open('day09/input1', 'r') as file_handle:
    lines = file_handle.read().strip().split('\n')
    
hpos = (0,0)
tpos = (0,0)
ttrail = [tpos]

pmin = (0, 0)    
pmax = (0, 0)

moves = {'U': lambda x: (x[0], x[1]+1),
         'D': lambda x: (x[0], x[1]-1),
         'L': lambda x: (x[0]-1, x[1]),
         'R': lambda x: (x[0]+1, x[1])}

for hmove in lines:
    drn, dist = hmove.split()
    dist = int(dist)
    for _ in range(dist):
        # print_grid(hpos, tpos)
        hpos = moves[drn](hpos)
        pmin = (hpos[0], pmin[1]) if hpos[0] < pmin[0] else pmin
        pmin = (pmin[0], hpos[1]) if hpos[1] < pmin[1] else pmin
        pmax = (hpos[0], pmax[1]) if hpos[0] > pmax[0] else pmax
        pmax = (pmax[0], hpos[1]) if hpos[1] > pmax[1] else pmax
        match (tpos[0] - hpos[0], tpos[1] - hpos[1]):
            case (2, 0): tpos = moves['L'](tpos)
            case (2, 1) | (1, 2): tpos = moves['D'](moves['L'](tpos))
            case (2, -1) | (1, -2): tpos = moves['U'](moves['L'](tpos))
            case (-2, 0): tpos = moves['R'](tpos)
            case (-2, 1) | (-1, 2): tpos = moves['D'](moves['R'](tpos))
            case (-2, -1) | (-1, -2): tpos = moves['U'](moves['R'](tpos))
            case (0, 2): tpos = moves['D'](tpos)
            case (0, -2): tpos = moves['U'](tpos)
            case _: pass
        ttrail.append(tpos)
            
        
# print_grid(hpos, tpos)

for y in range(-67, 95):
    for x in range(-201, 137):
        if (x, 4-y) in ttrail:
            print('#', end='')
        else:
            print('.', end='')
    print()
print()
    
print(len(set(ttrail)))
print(pmin, pmax)