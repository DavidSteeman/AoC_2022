import numpy as np
from queue import PriorityQueue
from graph import Graph
        
def heuristic(a, b):
       # Manhattan distance on a square grid
   return abs(a[0] - b[0]) + abs(a[1] - b[1])    


with open('day12/input1', 'r') as file_handle:
    lines = file_handle.read().strip().split('\n')

counts = []
graph = Graph(lines)
print(''.join(lines).count('a'))
goal = graph.end
for start in graph.starts:
    print(counts, start)
    frontier = PriorityQueue()
    frontier.put((0, start))
    goal = graph.end

    came_from = {start: None}
    cost_so_far = {start: 0}


    while not frontier.empty():
        cost, current = frontier.get()
        if current == goal:
            break
        for next in graph.neighbors[current]:
            new_cost = cost_so_far[current] + 1
            if next not in came_from or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put((new_cost, next))
                came_from[next] = current

    if graph.end in came_from:
        current = graph.end
        path = []
        while current != start:
            path.append(current)
            current = came_from[current]
            
        counts.append(len(path))
    
print(min(counts))