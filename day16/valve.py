def shortest_path(pos, target, visited):
        if target in pos.neighbors:
            return visited + [target]
        else:
            paths = []
            for nb in pos.neighbors:
                if nb not in visited:
                    nb_visited = shortest_path(nb, target, visited + [nb])
                    paths.append(nb_visited)
            paths = [path for path in paths if target in path]
            return (sorted(paths, key=lambda l: len(l)) or [[]])[0]
        

def highest_flowrate_path(pos, target, visited):
        if target in pos.neighbors:
            return visited + [target]
        else:
            paths = []
            for nb in pos.neighbors:
                if nb not in visited:
                    nb_visited = highest_flowrate_path(nb, target, visited + [nb])
                    paths.append(nb_visited)
            paths = [path for path in paths if target in path]
            return (sorted(paths, 
                           key=lambda valves: sum([v.flowrate for v in valves]), 
                                                  reverse=True) or [[]])[0]


def get_path_value(path, valves_open, nleft):
    n = 0
    i = 0
    while i < path and n < nleft:
        valve = path[i]
        if valve not in valves_open and (nleft - n) * valve.flowrate 

class Valve:
    def __init__(self, name, flowrate, links) -> None:
        self.name = name
        self.flowrate = flowrate
        self.neighbors = links[::1]
        
    def update_links(self, valves):
        new_links = []
        for link in self.neighbors:
            new_links.append(valves[link])
        self.neighbors = new_links
        
    def find_value_paths(self, targets):
        path_dict = dict()
        for target in targets:
            path_dict[target] = shortest_path(self, target, [self])
        self.value_paths = path_dict
        
        