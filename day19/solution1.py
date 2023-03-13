import numpy as np
from re import findall
from time import sleep
from math import inf

names = ('ore', 'clay', 'obsidian', 'geode')


# def distance_to_build(bots, resources, reqs):
#     s1 = set(bots.keys())
#     s2 = set(reqs.keys())
#     if not s2.issubset(s1):
#         return inf
#     for rsrc in names:
#         if 


def quickest_geode(bots, reqs, resources, time):
    pass
        


def find_best_val(reqs, resources={n: 0 for n in names}, time=0,
                  bots={'ore': 1, 'clay': 0, 'obsidian': 0, 'geode': 0}):
    # print(time)
    # sleep(0.1)
    geodes = resources['geode']
    if time == 12:
        return [] if not geodes else [geodes]

    # print(can_build)
    # ore = resources['ore']
    # clay = resources['clay']
    # obsidian = resources['obsidian']
    # if bots['obsidian'] == 0:
    #     if can_build['obsidian']:
    #         new_bots = bots.copy()
    #         new_bots['obsidian'] += 1
    if time >= 5 and bots['clay'] == 0:
        return []
    if bots['ore'] > 5:
        return []
    if bots['clay'] > 5:
        return []
    elif time > 13 and bots['obsidian'] == 0:
        return []
    
    for bot in bots:
        resources[bot] += bots[bot]
    can_build = {name: np.all([resources[r] > reqs[name][r] for r in reqs[name]]) for name in names}
    
    if can_build['geode']:
        resources['ore'] -= reqs['geode']['ore']
        resources['obsidian'] -= reqs['geode']['obsidian']
        bots['geode'] += 1
        return find_best_val(reqs, resources, time+1, bots)
    
    results = []
    for name in ('ore', 'clay', 'obsidian'):
        if can_build[name]:
            new_bots = bots.copy()
            new_bots[name] += 1
            new_resources = resources.copy()
            for rsrc, n in reqs[name].items():
                new_resources[rsrc] -= n
            results += find_best_val(reqs, new_resources, time+1, new_bots)
    # print(results)
    return results + find_best_val(reqs, resources, time+1, bots)

with open('day19/testinput1', 'r') as file_handle:
    lines = file_handle.read().strip().split('\n')
    

for bp in lines:
    reqs = dict()
    bp_nr = int(bp.split(':')[0].split(' ')[-1])
    bp = bp.split('costs ')[1:]
    for i in range(4):
        resources = findall("([0-9]+) ([a-z]+)", bp[i])
        reqs[names[i]] = {r[1]: int(r[0]) for r in resources}
    
    best_val = find_best_val(reqs)
    print(best_val)