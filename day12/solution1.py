import numpy as np
from queue import PriorityQueue
from graph import Graph
        
        


with open('day12/input1', 'r') as file_handle:
    lines = file_handle.read().strip().split('\n')
    
graph = Graph(lines)
frontier = PriorityQueue()
frontier.put((0, graph.start))
goal = graph.end

came_from = {graph.start: None}
cost_so_far = {graph.start: 0}


while not frontier.empty():
    cost, current = frontier.get()
    if current == goal:
        break
    if current == (143,13):
        print("hi", graph.neighbors[current])
    for next in graph.neighbors[current]:
        new_cost = cost_so_far[current] + 1
        if next not in came_from or new_cost < cost_so_far[next]:
            cost_so_far[next] = new_cost
            priority = new_cost
            frontier.put((new_cost, next))
            came_from[next] = current

print(graph.neighbors[(137,20)])
current = graph.end
path = []
while current != graph.start:
    path.append(current)
    print(current, lines[current[1]][current[0]])
    current = came_from[current]
    
# path.append(graph.start)
path.reverse()
print(path)
print(len(path))