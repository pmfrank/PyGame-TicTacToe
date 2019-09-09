import pygame as pg

class Graphics():
    '''
    This class handles all the graphics for PyGame
    '''

    def __init__(self):
        pg.init()
        self._size = (400,400)
        self._BLACK = (0,0,0)
        self._WHITE = (255,255,255)
        self._BLUE = (0,0,255)
        self._GREEN = (0,255,0)
        self._RED = (255,0,0)
        self._screen = pg.display.set_mode(self._size)
        pg.display.set_caption('Tic-Tac-Toe')
        self.font = pg.font.Font('freesansbold.ttf', 30)

    def create_game_board(self):
        self._screen.fill(self._WHITE)
        pg.draw.rect(self._screen,self._BLUE,(0,0,300,300))
        pg.draw.line(self._screen,self._WHITE,(0,100),(300,100))
        pg.draw.line(self._screen,self._WHITE,(0,200),(300,200))
        pg.draw.line(self._screen,self._WHITE,(100,0),(100,300))
        pg.draw.line(self._screen,self._WHITE,(200,0),(200,300))
        pg.display.flip()


    def draw_token(self, player, x_center, y_center):
        if player == 1:
            pg.draw.line(self._screen,self._WHITE,(x_center-50,y_center-50),(x_center+50,y_center+50))
            pg.draw.line(self._screen,self._WHITE,(x_center+50,y_center-50),(x_center-50,y_center+50))
        if player == 2:
            pg.draw.circle(self._screen,self._WHITE,(x_center,y_center),50,1)
        pg.display.flip()

    def update_player(self, player):
        text = self.font.render(f"{player.name}'s Turn", True, self._BLACK)
        pg.draw.rect(self._screen,self._WHITE,(0,300,220,350))
        self._screen.blit(text,(0,300))
        pg.display.flip()
    
    def notice(self, reason, player):
        if reason == 'Tie':
            text = self.font.render("This game was a tie!", True, self._BLACK)
        if reason == 'Win':
            text = self.font.render(f"{player.name} won the game!", True, self._BLACK)
        if reason == 'Invalid':
            text = self.font.render("That is not a valid move!", True, self._RED)
        
        self._screen.blit(text,(0,350))
        pg.display.flip()

    def clear_notice(self):
        eraser = pg.draw.rect(self._screen,self._WHITE,(0,350,399,399))
        pg.display.update(eraser)