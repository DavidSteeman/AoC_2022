import numpy as np


class Grid:
    offsets = set([(y, x) 
                   for y in (-1, 0, 1) 
                   for x in (-1, 0, 1)]
                  ).difference({(0, 0)})
    face_offsets = {'N': ((-1, -1), (-1, 0), (-1, 1)),
                    'S': ((1, -1), (1, 0), (1, 1)),
                    'W': ((-1, -1), (0, -1), (1, -1)),
                    'E': ((-1, 1), (0, 1), (1, 1)),}
    offset_faces = {(-1, -1): {'N', 'W'},
                    (-1, 0): {'N'},
                    (-1, 1): {'N', 'E'},
                    (0, -1): {'W'},
                    (0, 1): {'E'},
                    (1, -1): {'S', 'W'},
                    (1, 0): {'S'},
                    (1, 1): {'S', 'E'}}
    
    def __init__(self, gridstr) -> None:
        self.elves = None
        self.shape = [gridstr.count('\n')+1, gridstr.index('\n')]
        self.grid = np.zeros([self.shape[0], self.shape[1]])
        self.__init_grid(gridstr)
        
    def __init_grid(self, gridstr):
        elves = []
        for y, line in enumerate(gridstr.split('\n')):
            for x, char in enumerate(line):
                if char == '#':
                    self.grid[y][x] = 1
                    elves.append((y, x))
        self.elves = np.array(elves)
        
    def check_around(self, loc):
        blocked_faces = set()
        for offset in Grid.offsets:
            y_offset = loc[0] + offset[0]
            x_offset = loc[1] + offset[1]
            # print(y_offset, x_offset, self.grid[y_offset][x_offset])
            if (0 <= y_offset < self.shape[0] and
                0 <= x_offset < self.shape[1]):
                if self.grid[y_offset][x_offset]:
                    blocked_faces.update(Grid.offset_faces[offset])
        return blocked_faces
    
    def __expand_grid(self, y, x):
        if y < 0:
            self.grid = np.pad(self.grid, ((1, 0), (0, 0)))
            self.elves[:, 0] += 1
        elif y >= self.shape[0]:
            self.grid = np.pad(self.grid, ((0, 1), (0, 0)))
            
        if x < 0:
            self.grid = np.pad(self.grid, ((0, 0), (1, 0)))
            self.elves[:, 1] += 1
        elif x >= self.shape[1]:
            self.grid = np.pad(self.grid, ((0, 0), (0, 1))) 
    
    def move_elf(self, elf_nr, dir):
        y, x = self.elves[elf_nr]
        self.grid[(y, x)] = 0
        y_dest = y + dir[0]
        x_dest = x + dir[1]
        self.elves[elf_nr] = (y_dest, x_dest)
        self.__expand_grid(y_dest, x_dest)
        adjusted_y_dest, adjusted_x_dest = self.elves[elf_nr]
        self.grid[adjusted_y_dest][adjusted_x_dest] = 1
            
    def minimize_grid_shape(self):
        while sum(self.grid[:, 0]) == 0:
            self.grid = np.delete(self.grid, 0, 1)
            self.elves[:, 1] -= 1
        while sum(self.grid[:, -1]) == 0:
            self.grid = np.delete(self.grid, -1, 1)
        while sum(self.grid[0, :]) == 0:
            self.grid = np.delete(self.grid, 0, 0)
            self.elves[:, 0] -= 1
        while sum(self.grid[-1, :]) == 0:
            self.grid = np.delete(self.grid, -1, 0)
        self.shape = self.grid.shape
        
    def count_zeros(self):
        return self.grid.size - np.count_nonzero(self.grid)
            