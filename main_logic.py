import pygame
from Constants import GameConstants as gk
from GameRes import GameResources as res
from Classes import Sprite


def click_logic(sprite: Sprite):
    if sprite.rect.collidepoint(gk.mouse_position):
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
        if gk.money >= 10:
            gk.money -= 10
            gk.pickaxe_counter += 1
            res.Sounds.bye_sound.play()
    if click_logic(res.Sprites.drill):
        if gk.money >= 100:
            gk.money -= 100
            gk.drill_counter += 1
            res.Sounds.bye_sound.play()
