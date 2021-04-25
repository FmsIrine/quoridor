import pygame
from drawable import Drawable
from utils import hexcolor

class Player(Drawable) :
    def __init__(self, pos, color, ident):
        super().__init__(pos, (60, 60))
        pygame.draw.circle(self.surface, hexcolor(color), (30, 30), 30)
    
    