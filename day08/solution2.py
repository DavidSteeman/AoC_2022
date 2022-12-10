from math import prod

with open('day08/input1', 'r') as file_handle:
    lines = file_handle.read().strip().split('\n')


def get_scenic_score(lr, ud, x, y, hght):
    scores = []
    up = [] if y < 1 else ud[:y][::-1]
    down = [] if y > len(ud)-2 else ud[y+1:]
    left = [] if x < 1 else lr[:x][::-1]
    right = [] if x > len(lr)-2 else lr[x+1:]
    for dir in up, down, left, right:
        score = 0
        for h in dir:
            score += 1
            if h >= hght:
                break
        scores.append(score)     
    score = prod(scores)
    # print(x, y, scores, score, up, down, left, right, hght)
    return score
    
all_scores = []
lr = [[int(i) for i in list(line)] for line in lines]
ud = list(zip(*lr))
for y in range(len(lr)):
    for x in range(len(ud)):
        score = get_scenic_score(lr[y], ud[x], x, y, lr[y][x])
        all_scores.append(score)
        
print(max(all_scores))