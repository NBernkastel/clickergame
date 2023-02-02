import pygame.transform

from GameRes import GameResources as res
from Classes import Sprite
from util import *


def click_logic(sprite: Sprite, colide = True):
    if sprite.rect.collidepoint(gk.mouse_position) or colide == False:
        sprite.image = pygame.transform.scale(sprite.image, (sprite.width - 5, sprite.height - 5))
        sprite.rect.x += 3
        sprite.rect.y += 3
        return True
    else:
        sprite.image = pygame.image.load(sprite.src)
        sprite.image = pygame.transform.scale(sprite.image, (sprite.width, sprite.height))
        sprite.rect.x = sprite.x_start
        sprite.rect.y = sprite.y_start
        return False


def store_logic():
    if click_logic(res.Sprites.pickaxe):
        if gk.money >= 1000:
            gk.money -= 1000
            gk.pickaxe_counter += 1
            res.Sounds.bye_sound.play()
    if click_logic(res.Sprites.drill):
        if gk.money >= 10000:
            gk.money -= 10000
            gk.drill_counter += 1
            res.Sounds.bye_sound.play()
    if click_logic(res.Sprites.click):
        if gk.money >= 10**gk.click_counter:
            gk.money -= 10**gk.click_counter
            gk.click_counter += 1
            res.Sounds.bye_sound.play()
    if click_logic(res.Sprites.bomb):
        if gk.money >= 1000000:
            gk.money -= 1000000
            gk.bomb_counter += 1
            res.Sounds.bye_sound.play()

@Timer(1000)
def work():
    gk.money += gk.pickaxe_counter*5
    gk.money += gk.drill_counter * 50
    gk.money += gk.bomb_counter * 5000
