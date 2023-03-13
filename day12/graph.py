dirs = tuple(zip((1,-1,0,0), (0, 0, 1, -1)))


class Graph:
    def __init__(self, mapstr):
        self.starts = []
        self.map = self.__set_start_end(mapstr)
        self.ybound = len(mapstr)
        self.xbound = len(mapstr[0]) if self.ybound else 0
        self.neighbors = self.__make_graph()
        
    def __set_start_end(self, mapstr):
        map = mapstr.copy()
        for y in range(len(map)):
            row = map[y]
            if 'E' in row:
                self.end = (row.index('E'), y)
                map[y] = row.replace('E', 'z')
        return map
        
    def __make_graph(self):
        nodes = dict()
        for y in range(len(self.map)):
            row = self.map[y]
            for x in range(len(row)):
                nodes[(x, y)] = []
                height = self.map[y][x]
                if height == 'a':
                    self.starts.append((x, y))
                for dir in dirs:
                    newx, newy = x+dir[0], y+dir[1]
                    if (0 <= newx < self.xbound and 
                        0 <= newy < self.ybound and
                        ord(height) - ord(self.map[newy][newx]) >= -1):
                            nodes[(x, y)].append((newx, newy))
        return nodes    
                        
                        
                        
                    