from re import findall


def merge_intervals(ivs):
    new_arr = []
    start, end = ivs[0]
    i = 1
    for iv in ivs[1:]:
        if iv[0] <= end:
            end = max(end, iv[1])
        else:
            new_arr.append((start, end))
            start, end = iv
    return(new_arr + [(start, end)])
        

with open('day15/input1', 'r') as file_handle:
    lines = file_handle.read().strip().split('\n')
    
signals = []
for line in lines:
    grid = dict()
    nums = findall("(\-?[0-9]+)", line)
    xs, ys, xb, yb = map(int, nums)
    diffx, diffy = abs(xs - xb), abs(ys - yb)
    dist = diffx + diffy
    signals.append((xs, ys, dist))

signals.sort(key=lambda l: l[2], reverse=True)


blocksize = 4000000
for y in range(blocksize):
    row_ivs = []
    for signal in signals:
        xs, ys, dist = signal
        ydiff = abs(ys - y)
        if ydiff <= dist:
            extend = dist - ydiff
            row_ivs.append((xs-extend, xs+extend+1))
    row_ivs = sorted(row_ivs)
    row_ivs = merge_intervals(row_ivs)
    if len(row_ivs) > 1:
        print(row_ivs[0][1] * blocksize + y)
                
            
# for y in range(-2, 23):
#     print(' ' if y % 5 != 0 else str(y)[-1], end='')
#     for x in range(-2, 26):
#         print(grid.get((x, y), '.'), end='')
    # print()
# print()

# print()
# total = 0
# merged_covers = merge_intervals(sorted(covered))
# for cover in merged_covers:
#     total += cover[1] - cover[0] - 1
# print(total)
# leftmin = min(covered)[0]
# leftmin = abs(leftmin) if leftmin < 0 else 0
# rightmax = max(covered, key=lambda l: l[1])[1]
# cover_arr = [0] * (rightmax + leftmin + 1)
# print(leftmin, rightmax)
# for r in covered:
#     for x in range(r[0]+leftmin, r[1]+leftmin):
#         cover_arr[x] = 1

# print(sum(cover_arr))
# # for i in range(len(signals)):
# #     xs, xy = 
    
# # print(min(min(signals, key=lambda l: l[0]), min(beacons, key=lambda l: l[0]))[0])
# # print(max(max(signals, key=lambda l: l[1]), max(beacons, key=lambda l: l[1]))[1])