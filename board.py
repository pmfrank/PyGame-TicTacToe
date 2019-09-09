class Board():
    '''
    This class controls the game board and keeps track of 
    moves made. It also displays the board if played in the
    terminal
    '''

    def __init__(self):
        self._game_area =[[0,0,0],
                        [0,0,0],
                        [0,0,0]]
    
    def show_board(self):
        for row in self._game_area:
            print(row)
    
    def check_space(self,row : int, col : int):
        if self._game_area[row][col] == 0:
            return True
        return False

    def update(self, player, row : int, col : int):
        self._game_area[row][col] = player