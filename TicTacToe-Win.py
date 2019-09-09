from itertools import cycle
from board import Board
from player import Player
from win import Win
from graphics import Graphics
import pygame as pg


def main(board, players, win, game):
    game.create_game_board()
    game_over = game_tie = valid = False
    player_choice = cycle(players)
    while not game_over and not game_tie:
        current_player = next(player_choice)
        game.update_player(current_player)
        while not valid:
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    pg.quit()
                if event.type==pg.MOUSEBUTTONUP:
                    pos = pg.mouse.get_pos()
                
                    if 0 <= pos[0] <= 100 and 0 <= pos[1] <= 100:
                        row, col = 0, 0
                        x_center, y_center = 50, 50
                    if 100 <= pos[0] <= 200 and 0 <= pos[1] <= 100:
                        row, col = 0, 1
                        x_center, y_center = 150, 50
                    if 200 <= pos[0] <= 300 and  0 <= pos[1] <= 100:
                        row, col = 0, 2
                        x_center, y_center = 250, 50
                    if 0 <= pos[0] <= 100 and 100 <= pos[1] <= 200:
                        row, col = 1, 0
                        x_center, y_center = 50, 150
                    if 100 <= pos[0] <= 200 and 100 <= pos[1] <= 200:
                        row, col = 1, 1
                        x_center, y_center = 150, 150
                    if 200 <= pos[0] <= 300 and 100 <= pos[1] <= 200:
                        row, col = 1, 2
                        x_center, y_center = 250, 150
                    if 0 <= pos[0] <= 100 and 200 <= pos[1] <= 300:
                        row, col = 2, 0
                        x_center, y_center = 50, 250
                    if 100 <= pos[0] <= 200 and 200 <= pos[1] <= 300:
                        row, col = 2, 1
                        x_center, y_center = 150, 250
                    if 200 <= pos[0] <= 300 and 200 <= pos[1] <= 300:
                        row, col = 2, 2
                        x_center, y_center = 250, 250

                    try:
                        valid = board.check_space(row,col)
                        if not valid:
                            game.notice('Invalid',None)
                    except:
                        raise Exception("error")

        board.update(current_player.token,row,col)
        game.draw_token(current_player.token, x_center, y_center)
        game_over = win.check_win()
        game_tie = win.game_tie()
        valid = False
        game.clear_notice()
        
    if game_over:
        game.notice('Win', current_player)
    else:
        game.notice('Tie', None)
    input('wait')


if __name__ == "__main__":
    board = Board()
    win = Win(board._game_area)
    player1 = Player(1)
    player2 = Player(2)
    game = Graphics()
    main(board, [player1, player2], win, game)