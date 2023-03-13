from re import findall

with open('day15/testinput1', 'r') as file_handle:
    lines = file_handle.read().strip().split('\n')
    
target = 10
covered = []
for line in lines:
    grid = dict()
    nums = findall("(\-?[0-9]+)", line)
    xs, ys, xb, yb = map(int, nums)
    diffx, diffy = abs(xs - xb), abs(ys - yb)
    dist = diffx + diffy
    # print(f"Signal: {xs, ys} - Beacon: {xb, yb} - Top: {top}, Bot: {bot}, Left: {left}, Right: {right} - "
    #       f"Diffx: {diffx}, Diffy: {diffy}, Dist: {dist}")
    for yr in range(ys - dist, ys + dist + 1):
        extend = abs(abs(yr - ys) - dist)
        cover = (xs - extend, xs + extend + 1)
        if yr == target:
            covered.append(cover)
    # print('             1    1    2    2')
    # print('   0    5    0    5    0    5')
    # for y in range(-2, 23):
    #     print(' ' if y % 5 != 0 else str(y)[-1], end='')
    #     for x in range(-2, 26):
    #         print(grid.get((x, y), '.'), end='')
    #     print()
    # print()
    print(f"Line [{line}] processed")

# print()

def merge_intervals(ivs):
    print(ivs)
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
        
total = 0
merged_covers = merge_intervals(sorted(covered))
for cover in merged_covers:
    total += cover[1] - cover[0] - 1
print(total)
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