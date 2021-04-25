import pygame

from pygame.locals import *
from display import Display
from player import Player
from god_gamer import Master

if __name__ == "__main__":
    pygame.init()

    time = pygame.time.Clock()
    window = Display((900,900))
    master = Master(2)

    for player in master.get_players():
        window.add_drawable(player)

    while not master.get_win():
        time.tick(60)
        window.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                master.set_win(True)
            if event.type == pygame.KEYDOWN:
                master.event(event.key)

