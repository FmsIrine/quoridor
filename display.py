import pygame
from utils import hexcolor


class Display(object) :
    def __init__(self, size: tuple):
        self.size = size
        self.window = pygame.display.set_mode(self.size)
        self.drawables = []

    def update(self):
        pygame.display.set_caption("Quoridor")
        self.window.fill(hexcolor("#ffffff"))

        for drawable in self.drawables:
            self.window.blit(drawable.get_surface(), drawable.get_pos())
            
        pygame.display.update() 
    
    def add_drawable(self, drawable):
        self.drawables.append(drawable)
