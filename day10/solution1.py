

with open('day10/input1', 'r') as file_handle:
    lines = file_handle.read().strip().split('\n')
    
cycle = 1
x = 1
total = 0
for line in lines:
    if cycle in range(20, 221, 40):
        print(x, cycle, cycle * x)
        total += cycle * x
    # print(cycle, x, line)
    match line.split():
        case ['addx', n]:
            if cycle+1 in range(20, 221, 40):
                print(x, cycle, (cycle+1) * x)
                total += (cycle+1) * x 
            x += int(n) 
            cycle += 2
        case ['noop']: 
            cycle += 1
    
print(total)