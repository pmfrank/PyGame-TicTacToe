class Win():
    '''
    This class covers the Win or Tie conditions of the game.
    '''
    def __init__(self, board):
        self._board = board

    def _row_win(self):
        for row in self._board:
            if row.count(row[0]) == len(row) and row[0] != 0:
                return True
    
    def _col_win(self):
        for col in range(len(self._board)):
            check = []
            for row in self._board:
                check.append(row[col])
            if check.count(check[0]) == len(check) and check[0] != 0:
                return True

    def _diag_win(self):
        diags = []
        for ix in range(len(self._board)):
            diags.append(self._board[ix][ix])
        if diags.count(diags[0]) == len(diags) and diags[0] != 0:
            return True
        
        diags = []
        for col, row in enumerate(reversed(range(len(self._board)))):
            diags.append(self._board[row][col])
        if diags.count(diags[0]) == len(diags) and diags[0] != 0:
            return True

    def game_tie(self):
        if sum(row.count(0) for row in self._board) == 0:
            return True
    

    def check_win(self):
        if self._row_win() or self._col_win() or self._diag_win():
            return True
        return False