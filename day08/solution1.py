

with open('day08/input1', 'r') as file_handle:
    lines = file_handle.read().strip().split('\n')


def get_max(line):
    if len(line) == 0:
        return []
    elif len(line) == 1:
        return [0]
    else:
        max_val = max(line)
        max_pos = line.index(max_val)
        return [max_pos] + get_max(line[:max_pos])

visible_locs = []
lr = [[int(i) for i in list(line)] for line in lines]
ud = list(zip(*lr))
for idx in range(len(lr)):
    line = lr[idx]
    cur_max = line[0]
    result_lr = [0]
    for i, v in enumerate(line):
        if v > cur_max:
            result_lr.append(i)
            cur_max = v
    result_rl = []
    cur_max = line[-1]
    result_rl = [len(line)-1]
    for i in range(len(line)-1, -1, -1):
        if i > result_lr[-1]:
            v = line[i]
            if v > cur_max:
                result_rl.append(i)
                cur_max = v
    visible_locs.extend([(idx, yp) for yp in result_lr + result_rl])
    
for idx in range(len(ud)):
    line = ud[idx]
    result_ud = []
    cur_max = line[0]
    result_ud = [0]
    for i, v in enumerate(line):
        if v > cur_max:
            result_ud.append(i)
            cur_max = v
    cur_max = line[-1]
    result_du = [len(line)-1]
    for i in range(len(line)-1, -1, -1):
        if i > result_ud[-1]:
            v = line[i]
            if v > cur_max:
                result_du.append(i)
                cur_max = v
    visible_locs.extend([(xp, idx) for xp in result_ud + result_du])

# print(set(visible_locs))
print(len(set(visible_locs)))