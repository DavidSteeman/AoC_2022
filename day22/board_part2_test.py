class Board:
    
    def __init__(self, board_str):
        board_list = [line.strip() for line in board_str.split('\n')]
        self.grids = {'left': [l[4:8] for l in board_list[4:8]], 
                      'right': [l[4:] for l in board_list[8:]], 
                      'back': [l[:4] for l in board_list[4:8]], 
                      'front': [l[8:] for l in board_list[4:8]], 
                      'top': board_list[:4], 
                      'bot': [l[:4] for l in board_list[8:]]}
        self.grid_len = len(self.grids['left'])
        self.gridsize = self.grid_len - 1
        self.pos = (0, 0, 'top')
        self.dir = (0, 1)
        print([len(g) for g in self.grids.values()])
        
    def __move_pos(self):
        new_y = self.pos[0] + self.dir[0]
        new_x = self.pos[1] + self.dir[1]
        new_grid = self.pos[2]
        new_dir = self.dir[::]
        if new_y > self.gridsize:
            match self.pos[2]:
                case 'top': new_grid = 'front'; new_y = 0;
                case 'front': new_grid = 'bot'; new_y = 0;
                case 'bot': new_grid = 'back'; new_y = self.gridsize; new_x = self.gridsize - new_x; new_dir = (-1, 0);
                case 'left': new_grid = 'bot'; new_y = new_x; new_x = 0; new_dir = (0, 1);
                case 'right': new_grid = 'back'; new_y = new_x; new_x = 0; new_dir = (0, 1);
                case 'back': new_grid = 'right'; new_y = self.gridsize; new_x = self.gridsize - new_x; new_dir = (-1, 0);
        elif new_y < 0:
            match self.pos[2]:
                case 'top': new_grid = 'back'; new_y = 0; new_x = self.gridsize - new_x; new_dir = (1, 0);
                case 'front': new_grid = 'top'; new_y = self.gridsize;
                case 'bot': new_grid = 'front'; new_y = self.gridsize;
                case 'left': new_grid = 'top'; new_y = new_x; new_x = 0; new_dir = (0, 1);
                case 'right': new_grid = 'front'; new_y = new_x; new_X = self.gridsize; new_dir = (0, -1);
                case 'back': new_grid = 'left'; new_y = 0; new_x = self.gridsize - new_x; new_dir = (1, 0);          
        elif new_x > self.gridsize:
            match self.pos[2]:
                case 'top': new_grid = 'right'; new_x = self.gridsize; new_y = self.gridsize - new_y; new_dir = (0, -1);
                case 'front': new_grid = 'right'; new_x = self.gridsize - new_y; new_y = 0; new_dir = (1, 0);
                case 'bot': new_grid = 'right'; new_x = 0;
                case 'left': new_grid = 'front'; new_x = 0;
                case 'right': new_grid = 'top'; new_y = self.gridsize - new_y; new_x = self.gridsize; new_dir = (0, -1);
                case 'back': new_grid = 'left'; new_x = 0;
        elif new_x < 0:
            match self.pos[2]:
                case 'top': new_grid = 'left'; new_x = self.gridsize - new_x; new_y = 0; new_dir = (1, 0);
                case 'front': new_grid = 'left'; new_x = self.gridsize;
                case 'bot': new_grid = 'left'; new_x = self.gridsize - new_y; new_y = self.gridsize; new_dir = (-1, 0);
                case 'left': new_grid = 'back'; new_x = self.gridsize;
                case 'right': new_grid = 'bot'; new_x = self.gridsize;
                case 'back': new_grid = 'top'; new_x = self.gridsize - new_y; new_y = self.gridsize; new_dir = (-1, 0);

        # print(self.pos, self.dir)
        # print(new_y, new_x, new_dir, new_grid)
        return new_y, new_x, new_grid, new_dir
                         
    def move(self, m_dist):
        moves = m_dist
        old_pos = None
        while moves > 0:
            new_y, new_x, new_grid, new_dir = self.__move_pos()
            print(self.pos, self.dir, new_y, new_x, new_grid, new_dir)
            if self.grids[new_grid][new_y][new_x] == '#':
                break
            elif self.grids[new_grid][new_y][new_x] == ' ':
                if not old_pos:
                    old_pos = self.pos[::]
            else:
                moves -= 1
            self.pos = (new_y, new_x, new_grid)
            self.dir = new_dir
        if self.grids[self.pos[2]][self.pos[0]][self.pos[1]] == ' ':
            self.pos = old_pos
            
            
    def turn(self, t_dir):
        match(t_dir, self.dir):
            case ('R', (0, 1)): self.dir = (1, 0)
            case ('R', (1, 0)): self.dir = (0, -1)
            case ('R', (0, -1)): self.dir = (-1, 0)
            case ('R', (-1, 0)): self.dir = (0, 1)
            case ('L', (0, 1)): self.dir = (-1, 0)
            case ('L', (-1, 0)): self.dir = (0, -1)
            case ('L', (0, -1)): self.dir = (1, 0)
            case ('L', (1, 0)): self.dir = (0, 1)
            case _: print("Something went wrong turning:", t_dir, self.dir)
            