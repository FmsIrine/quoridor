import pygame

class Drawable(object) :
    def __init__(self, pos, size):
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.surface = pygame.Surface((size[0], size[1]), pygame.SRCALPHA)

    def get_surface(self):
        return self.surface
    
    def move(self, x, y):
        self.rect = self.rect.move(x, y)

    def get_rect(self):
        return self.rect

    def get_pos(self):
        return (self.rect[0], self.rect[1])

