import numpy as np

SHAPES = [{'blocks': ((0,3), (0,4), (0,5), (0,6)), 'height': 1},
          {'blocks': ((1,3), (2,4), (1,4), (0,4), (1,5)), 'height': 3},
          {'blocks': ((2,3), (2,4), (2,5), (1,5), (0,5)), 'height': 3},
          {'blocks': ((3,3), (2,3), (1,3), (0,3)), 'height': 4},
          {'blocks': ((1,3), (0,3), (1,4), (0,4)), 'height': 2}]

field = np.pad(np.zeros((3,7)), ((0,1),(1,1)), 
               mode='constant', 
               constant_values=1)
field = np.pad(field, ((0,1), (0,0)), mode='minimum')

jetmove = {'<': (0, -1), '>': (0, 1)} 


def pad_field(field, piece_height):
    empty_rows = sum([1 for r in np.any(field[0:3, 1:7], axis=1) if not r])
    field = np.pad(field, ((piece_height + 3 - empty_rows, 0), (0,0)), 
                   mode='minimum')


def place_piece(piece):
    for block in piece:
        field[block] = 1
        

def unplace_piece(piece):
    for block in piece:
        field[block] = 0
        

def move(piece, offset):
    new_piece = []
    for block in piece:
        new_pos = (block[0]+offset[0], block[1]+offset[1])
        if field[new_pos] == 1:
            return piece
        new_piece.append(new_pos)
    return new_piece
        


with open('day17/testinput1', 'r') as file_handle:
    jets = list(file_handle.read().strip())
    jetlen = len(jets)
    

rock_nr = 0
jet_nr = 0
top = 0
topline = [1] * 7
while rock_nr < 4:
    rock = SHAPES[rock_nr % 5]
    field = pad_field(field, ((rock['height'], 0), (0,0)), mode='minimum')
    piece = rock['blocks'][::]
    place_piece(piece)
    print(field)
    unplace_piece(piece)
    while True:
        hor_move = move(piece, jetmove[jets[jet_nr]])
        place_piece(hor_move)
        print(field)
        unplace_piece(hor_move)
        jet_nr = (jet_nr + 1) % jetlen
        down_move = move(hor_move, (1,0))
        place_piece(down_move)
        print(field)
        piece = down_move
        if down_move != hor_move:
            unplace_piece(down_move)
        else:
            break
    rock_nr += 1