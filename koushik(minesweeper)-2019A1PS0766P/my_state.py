import copy

from my_board import Board
from bomb import Bombs

class alreadyfilledbutton():
    pass

bomb = Bombs.createbomb()

class state:


    HUMAN = 1
    BOMB = 4

    def __init__(self):
        self.occupied = 0
        self.gameboard = Board.new()
        pass

    def __str__(self):
        return '\n'.join([ f'safe moves: {self.occupied}', self.gameboard.__str__()])


    def __repr__(self):
        return 'state()'

    def __deepcopy__(self,memo):
        temp = state()
        temp.occupied = self.occupied
        temp.board = self.board.__deepcopy__()
        pass

    @staticmethod

    def new():
        return state()

    def __contains__(self,key):
        return True if key in Bombs.createbomb else False


    def choices(self,row,col):
        return (row,col)


    def human_choice(self, row, col):
        choice = self.choices(row,col)
        if choice in bomb:

            print('gameover')
            quit()
        else:
            self.gameboard.select(row,col,1)
            self.occupied += 1
            if self.win():
                print('you are very lucky today')

    def bombcheck(self,row,col):
        choice = self.choices(row,col)
        if choice in bomb:
            return True

    def win(self):
        if self.occupied == 21:
            return True
