class Board:
    
    def __init__(self, board_str):
        board_list = board_str.split('\n')
        self.board_width = max([len(line) for line in board_list])
        self.board = [list(line) + [' '] * (self.board_width - len(line)) 
                      for line in board_list]
        self.board_len = len(board_list)
        self.pos = (0, [i for i, c in enumerate(self.board[0]) if c == '.'][0])
        self.dir = (0, 1)
        
    def __move_pos(self):
        new_y = (self.pos[0] + self.dir[0]) % self.board_len
        new_x = (self.pos[1] + self.dir[1]) % self.board_width
        # print(self.pos, self.dir, new_y, new_x)
        return (new_y, new_x)
                         
    def move(self, m_dist):
        moves = m_dist
        old_pos = None
        while moves > 0:
            new_y, new_x = self.__move_pos()
            if self.board[new_y][new_x] == '#':
                break
            elif self.board[new_y][new_x] == ' ':
                if not old_pos:
                    old_pos = self.pos[::]
            else:
                moves -= 1
            self.pos = (new_y, new_x)
        if self.board[self.pos[0]][self.pos[1]] == ' ':
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
            