import numpy as np

with open('day02/input1', 'r') as file_handle:
    lines = file_handle.readlines()
    
shape_scores = {'A': 1, 'B': 2, 'C': 3, 
                'X': lambda x: (x - 1) or 3, 
                'Y': lambda x: x, 
                'Z': lambda x: (x % 3) + 1}
result_scores = {'X': 0, 'Y': 3, 'Z': 6}


def get_result(opponent, player):
    shape_score = shape_scores[player](shape_scores[opponent])    
    return shape_score + result_scores[player]


score = 0
for line in lines:
    score += get_result(*line.split())
    
    
print(score)