import random
import pygame
from player import Player
from wall import Wall

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
        player = self.players[int(self.turn*0.5)]
        
        if str(self.turn * 0.5)[-1] == '5':
            if key == pygame.K_UP and not self.collide(player, 0, -30):
                player.move(0, -30)
            elif key == pygame.K_RIGHT and not self.collide(player, +30, 0):
                player.move(+30, 0)
            elif key == pygame.K_LEFT and not self.collide(player, -30, 0):
                player.move(-30, 0)
            elif key == pygame.K_DOWN and not self.collide(player, 0, +30):
                player.move(0, +30)
            else:
                return

            self.turn = 0 if self.turn + 1 == len(self.players) * 2 else self.turn + 1

        elif key == 0xdeadbeef or key == 0xcafebabe:
            wall = Wall(player.get_color(), key == 0xcafebabe)

            if not self.collide(wall, 0, 0):
                player.add_wall(wall)
                self.turn = 0 if self.turn + 1 == len(self.players) * 2 else self.turn + 1

    def collide_player(self, drawable, x , y):
        if type(drawable) == Player:
            other_rect = [other.get_rect() for other in self.players if other != drawable]
        else:
            other_rect = [other.get_rect() for other in self.players]

        futur_drawable = drawable.get_rect().move(x, y)
        return futur_drawable.collidelist(other_rect) != -1

    def collide_display(self, drawable, x, y):
        futur_drawable = drawable.get_rect().move(x, y)

        posY = drawable.get_surface().get_height() - 30
        posX = drawable.get_surface().get_width()

        display_surface = pygame.display.get_surface()
        width = display_surface.get_width() - 120
        height = display_surface.get_height() - 60

        display_rect = pygame.Rect((posX, posY), (width, height))
        return not display_rect.colliderect(futur_drawable)
    
    def collide_wall(self, drawable, x, y):
        other_rect = [other.get_rect() for player in self.players for other in player.get_wall()]
        futur_drawable = drawable.get_rect().move(x, y)
        return futur_drawable.collidelist(other_rect) != -1
    
    def collide(self, drawable, x, y):
        return self.collide_player(drawable, x, y) or self.collide_display(drawable, x, y) or self.collide_wall(drawable, x, y)