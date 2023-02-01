import pygame
from Constants import GameConstants as gk
pygame.init()
screen = pygame.display.set_mode([600, 600])


def timer(x):
    def par(fun):
        def wrapper():
            if gk.ticks % x == 0:
                fun()
        return wrapper
    return par