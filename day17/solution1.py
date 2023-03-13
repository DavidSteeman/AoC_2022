import numpy as np
from time import sleep


SHAPES = [{'blocks': ((0,2), (0,3), (0,4), (0,5)), 'height': 1, 'highest_block': 0},
          {'blocks': ((1,2), (2,3), (1,3), (0,3), (1,4)), 'height': 3, 'highest_block': 3},
          {'blocks': ((2,2), (2,3), (2,4), (1,4), (0,4)), 'height': 3, 'highest_block': 4},
          {'blocks': ((3,2), (2,2), (1,2), (0,2)), 'height': 4, 'highest_block': 3},
          {'blocks': ((1,2), (0,2), (1,3), (0,3)), 'height': 2, 'highest_block': 1}]

field = np.zeros((10000,7))
jetmove = {'<': (0, -1), '>': (0, 1)} 


def pad_field(piece_height):
    global field
    empty_rows = sum([1 for r in np.all(field[0:3, 1:8] == 0, axis=1) if r])
    field = np.pad(field, ((piece_height + 3 - empty_rows, 0), (0,0)), 
                   mode='minimum')


def place_piece(piece, field):
    for block in piece:
        field[block] = 1
        

def unplace_piece(piece):
    for block in piece:
        field[block] = 0
        

def move(piece, offset):
    bot = field.shape[0]
    new_piece = []
    for block in piece:
        new_pos = (block[0]+offset[0], block[1]+offset[1])
        if (new_pos[0] >= bot or
            new_pos[1] < 0 or 
            new_pos[1] > 6 or 
            field[new_pos] == 1):
            return piece
        new_piece.append(new_pos)
    return new_piece
        

with open('day17/input1', 'r') as file_handle:
    jets = list(file_handle.read().strip())
    jetlen = len(jets)
    

rock_nr = 0
jet_nr = 0
top = 10000
cutbits = 0
while rock_nr < 1000000:
    rock = SHAPES[rock_nr % 5]
    topdiff = top - rock['height']
    piece = [(b[0]+topdiff-3, b[1]) for b in rock['blocks'][::]]
    while True:
        # print(jet_nr, jets[jet_nr], top)
        # for y in range(top-3-rock['height'], top+10):
        #     for x in range(7):
        #         print('#' if (y < field.shape[0] and field[y,x]) or (y,x) in piece else '.', end='')
        #     print()
        # print()
        hor_move = move(piece, jetmove[jets[jet_nr]])
        jet_nr = (jet_nr + 1) % jetlen
        down_move = move(hor_move, (1,0))
        # for y in range(top-3-rock['height'], top+10):
        #     for x in range(7):
        #         print('#' if (y < field.shape[0] and field[y,x]) or (y,x) in hor_move else '.', end='')
        #     print()
        # print()
        # print(hor_move, down_move, hor_move == down_move)
        piece = down_move
        # sleep(0.2)
        if down_move == hor_move:
            place_piece(down_move, field)
            block_top = down_move[rock['highest_block']][0] 
            row = block_top
            while row < block_top + rock['height']:
                # print(field[row, :])
                if field[row, :].all():
                    print(row, top, rock_nr)
                    cutlen = field.shape[0] - row
                    cutbits += cutlen
                    field = field[:row, :]
                    # print('closed row!')
                    row += 10
                row += 1
            break
    if field.shape[0] > 100000:
        print('uhhh')
    top = min(top, down_move[rock['highest_block']][0])
    if top < 10 or field.shape[0] < 1000:
        field = np.pad(field, ((10000, 0), (0, 0)))
        top += 1000
    rock_nr += 1
print()

print(field.shape, cutbits)
print(field.shape[0] - top + cutbits)
# print(cutbits)