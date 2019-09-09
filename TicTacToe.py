from itertools import cycle
from board import Board
from player import Player
from win import Win

def main(board, players, win):

    board.show_board()
    game_over = game_tie = valid = False
    player_choice = cycle(players)
    while not game_over and not game_tie:
        current_player = next(player_choice)
        print(current_player.name)
        while not valid:
            try:
                row = int(input("row "))
                col = int(input("col "))
                valid = board.check_space(row,col)
                if not valid:
                    print('Try again')
            except:
                raise Exception("error")
        board.update(current_player.token,row,col)
        board.show_board()
        game_over = win.check_win()
        game_tie = win.game_tie()
        valid = False

if __name__ == "__main__":
    board = Board()
    win = Win(board._game_area)
    player1 = Player(1)
    player2 = Player(2)
    main(board, [player1, player2], win)
