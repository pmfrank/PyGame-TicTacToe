class Player():
    '''
    This class is used to create the player objects
    '''
    def __init__(self, token : int):
        self.token = token
        self.name = f'Player {token}'