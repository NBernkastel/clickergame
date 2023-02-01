import pygame
from Constants import GameConstants as gk

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gk.running = False
        if event.type == pygame.MOUSEBUTTONUP:
            gk.mouse_position = pygame.mouse.get_pos()