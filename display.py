import pygame
from utils import hexcolor
from player import Player

class Display(object) :
    def __init__(self, size):
        self.size = size
        self.window = pygame.display.set_mode(self.size)
        self.drawables = []

    def update(self):
        pygame.display.set_caption("Quoridor")
        self.window.fill(hexcolor("#ffffff"))

        for drawable in self.drawables:
            if type(drawable) == Player:
                for wall in drawable.get_wall():
                    self.window.blit(wall.get_surface(), wall.get_pos())

            self.window.blit(drawable.get_surface(), drawable.get_pos())
            
        pygame.display.update() 
    
    def add_drawable(self, drawable):
        self.drawables.append(drawable)
