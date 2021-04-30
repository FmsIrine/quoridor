import pygame
from drawable import Drawable
from utils import hexcolor
from wall import Wall

class Player(Drawable) :
    def __init__(self, pos, color, ident):
        super().__init__(pos, (60, 60))
        self.wall = []
        self.color = color

        pygame.draw.circle(self.surface, hexcolor(color), (30, 30), 30)
        
    def get_wall(self):
        return self.wall

    def add_wall(self, wall):
        self.wall.append(wall)
    
    def get_color(self):
        return self.color