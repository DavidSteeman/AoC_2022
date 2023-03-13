from re import findall
from board import Board


with open('day22/input1', 'r') as file_handle:
    board_map, instructions = file_handle.read().rstrip().split('\n\n')

board = Board(board_map)
for ins in findall("[0-9]+[RL]?", instructions):
    if ins[-1] in 'RL':
        distance = int(ins[:-1])
        turn = ins[-1]
        board.move(distance)
        board.turn(turn)
    else:
        board.move(int(ins))

dirmap = {(0, 1): 0, (1, 0): 1, (0, -1): 2, (-1, 0): 3}
row = board.pos[0]+1
col = board.pos[1]+1
drc = dirmap[board.dir]
print(row, col, drc)
print(row*1000 + col*4 + drc)