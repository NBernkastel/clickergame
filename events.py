import pygame
from Constants import GameConstants as gk

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gk.running = False
        if event.type == pygame.MOUSEBUTTONUP:
            gk.mouse_position = pygame.mouse.get_pos()
        if event.type == 10:
            gk.money += gk.pickaxe_counter * 0.001
        if event.type == 11:
            gk.money += gk.drill_counter * 0.05