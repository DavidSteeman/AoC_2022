from re import findall
from board_part2 import Board


with open('day22/input1', 'r') as file_handle:
    board_map, instructions = file_handle.read().rstrip().split('\n\n')

board = Board(board_map)
i = 0
for ins in findall("[0-9]+[RL]?", instructions):
    # print(f"move - {ins} - ", board.pos, board.dir)
    if ins[-1] in 'RL':
        distance = int(ins[:-1])
        turn = ins[-1]
        board.move(distance)
        board.turn(turn)
    else:
        board.move(int(ins))
    i += 1
    # print("succeeded:", board.pos, board.dir)

dirmap = {(0, 1): 0, (1, 0): 1, (0, -1): 2, (-1, 0): 3}
grid = board.pos[2]
row = board.pos[0]+1
if grid == 'front':
    row += 50
elif grid in ['bot', 'left']:
    row += 100
elif row == 'back':
    row += 150
col = board.pos[1]+1
if grid in ['top', 'front', 'bot']:
    col += 50
elif grid == 'right':
    col += 100
drc = dirmap[board.dir]
print(row, col, drc)
print(row*1000 + col*4 + drc)