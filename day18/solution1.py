from collections import defaultdict

with open('day18/input1', 'r') as file_handle:
    cubes = file_handle.read().strip().split('\n')


xs = defaultdict(lambda: [])
ys = defaultdict(lambda: [])
zs = defaultdict(lambda: [])
exposed_sides = 0

for cube in cubes:
    exposed_sides += 6
    x, y, z = map(int, cube.split(','))
    x_line = xs[(y, z)]
    y_line = ys[(x, z)]
    z_line = zs[(x, y)]
    for xx in x_line:
        if abs(xx - x) == 1:
            exposed_sides -= 2
    for yy in y_line:
        if abs(yy - y) == 1:
            exposed_sides -= 2
    for zz in z_line:
        if abs(zz - z) == 1:
            exposed_sides -= 2
    
    x_line.append(x)
    y_line.append(y)
    z_line.append(z)
    
print(exposed_sides)