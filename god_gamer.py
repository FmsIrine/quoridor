import random
import pygame
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

    def event(self, key):
        player = self.players[self.turn]
        if key == pygame.K_UP and not self.collide_player(player, 0, -30):
            player.move(0, -30)
        if key == pygame.K_RIGHT and not self.collide_player(player, +30, 0):
            player.move(+30, 0)
        if key == pygame.K_LEFT and not self.collide_player(player, -30, 0):
            player.move(-30, 0)
        if key == pygame.K_DOWN and not self.collide_player(player, 0, +30):
            player.move(0, +30)
        
        self.turn = 0 if self.turn + 1 == len(self.players) else self.turn + 1
    
    def collide_player(self, player, x , y):
        other_rect = [other.get_rect() for other in self.players if other != player]
        futur_player = player.get_rect().move(x, y)
        return futur_player.collidelist(other_rect) != -1

    def collide_display(self, )
