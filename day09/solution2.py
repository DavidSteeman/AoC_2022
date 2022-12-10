def print_grid(posdict):
    print(posdict)
    for y in range(-10, 20):
        for x in range(-15, 20):
            empty_square = True
            for i in range(10):
                if empty_square:
                    knot_loc = posdict[i]
                    if x == knot_loc[0] and y == 4 - knot_loc[1]:
                        print('H' if i == 0 else str(i), end='')
                        empty_square = False
            if empty_square:
                print('.', end='')
        print()
    print()
        
            

with open('day09/input1', 'r') as file_handle:
    lines = file_handle.read().strip().split('\n')
    
mpos = (0,0)
ttrail = [(0,0)]
posdict = {n: (0, 0) for n in range(10)}

moves = {'U': lambda x: (x[0], x[1]+1),
         'D': lambda x: (x[0], x[1]-1),
         'L': lambda x: (x[0]-1, x[1]),
         'R': lambda x: (x[0]+1, x[1])}

for hmove in lines:
    drn, dist = hmove.split()
    dist = int(dist)
    for _ in range(dist):
        # print_grid(posdict)
        posdict[0] = moves[drn](posdict[0])
        for i in range(1, 10):
            hpos = posdict[i-1]
            tpos = posdict[i]
            diff = (tpos[0] - hpos[0], tpos[1] - hpos[1])
            if diff[1] == 0:
                if diff[0] > 1: tpos = moves['L'](tpos)
                elif diff[0] < -1: tpos = moves['R'](tpos)
            elif diff[0] == 0:
                if diff[1] > 1: tpos = moves['D'](tpos)
                elif diff[1] < -1: tpos = moves['U'](tpos)
            elif ((diff[0] > 1 and diff[1] > 0) or
                  (diff[0] > 0 and diff[1] > 1)):
                tpos = moves['D'](moves['L'](tpos))
            elif ((diff[0] < -1 and diff[1] > 0) or
                  (diff[0] < 0 and diff[1] > 1)):
                tpos = moves['D'](moves['R'](tpos))
            elif ((diff[0] > 0 and diff[1] < -1) or 
                  (diff[0] > 1 and diff[1] < 0)):
                tpos = moves['U'](moves['L'](tpos))
            elif ((diff[0] < 0 and diff[1] < -1) or
                  (diff[0] < -1 and diff[1] < 0)):
                tpos = moves['U'](moves['R'](tpos))
            posdict[i] = tpos
        ttrail.append(posdict[9])
            
        
# print_grid(hpos, tpos)

for y in range(5):
    for x in range(6):
        if (x, 4-y) in ttrail:
            print('#', end='')
        else:
            print('.', end='')
    print()
print()
    
print(len(set(ttrail)))