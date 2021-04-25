import random
from player import Player  

class Master(object) :
    def __init__(self, nbr_player = 2):
        self.players = []
        self.turn = 0
        self.win = False
     
        delta = 0
        for i in range(nbr_player):
            posX = 50 if i % 2 == 0 else 800
            posY = 450 - (30 * nbr_player) + (delta * 80)
            self.players.append(Player((posX, posY), f"#{random.randint(0, 0xffffff):06x}", i))
            
            if i % 2 == 1:
                delta += 1

    def get_players(self):
        return self.players

    def get_win(self):
        return self.win

    def set_win(self, win):
        self.win = win
    