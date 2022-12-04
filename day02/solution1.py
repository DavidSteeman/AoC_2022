import numpy as np

with open('day02/input1', 'r') as file_handle:
    lines = file_handle.readlines()
    
shape_table = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
result_table = {1: 6, -2: 6, 0: 3, -1: 0, 2: 0}


def get_result(opponent, player):
    player_shape = shape_table[player]     
    return player_shape + result_table[player_shape - shape_table[opponent]]


score = 0
for line in lines:
    score += get_result(*line.split())
    
    
print(score)