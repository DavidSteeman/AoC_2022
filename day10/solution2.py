

with open('day10/input1', 'r') as file_handle:
    lines = file_handle.read().strip().split('\n')

def print_pixel(cycle, sprite):
    hpos = (cycle-1) % 40
    print('#' if hpos in range(sprite-1, sprite+2) else '.', end='')
    if hpos == 39:
        print()

cycle = 1
x = 1

for line in lines:
    match line.split():
        case ['addx', n]:
            print_pixel(cycle, x)
            cycle += 1
            print_pixel(cycle, x)
            cycle += 1
            x += int(n) 
        case ['noop']:
            print_pixel(cycle, x) 
            cycle += 1 
