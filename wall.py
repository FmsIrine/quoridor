import pygame
from utils import hexcolor
from drawable import Drawable


class Wall(Drawable) :
    def __init__(self, color, reverse):
        pos = pygame.mouse.get_pos()
        size = (10, 60)

        if reverse:
            size = (60, 10)

        super().__init__(pos, size)
        self.surface.fill(color)