import pygame
from pygame.mixer import Sound

from Classes import Sprite, Text


class GameResources:
    class Sprites:
        earth = Sprite('scr/img/earth.png', 150, 150, 200, 200)
        back = Sprite('scr/img/space.jpg', 600, 600, 0, 0)
        store = Sprite('scr/img/store.png', 64, 32, 510, 15)
        scroll = Sprite('scr/img/scroll.png', 350, 550, 130, 20)
        pickaxe = Sprite('scr/img/pickaxe.png', 40, 40, 330, 100)
        pickaxe2 = Sprite('scr/img/pickaxe.png', 40, 40, 450, 395)
        drill = Sprite('scr/img/drill.png', 40, 40, 220, 180)
        drill2 = Sprite('scr/img/drill.png', 40, 40, 450, 450)
        bomb = Sprite('scr/img/bomb.png', 40, 40, 330, 180)
        bomb2 = Sprite('scr/img/bomb.png', 40, 40, 450, 500)
        click = Sprite('scr/img/click.png',32,32,220,100)
        click2 = Sprite('scr/img/click.png', 32, 32, 450, 350)

        own_sprites = pygame.sprite.Group()
        store_sprites = pygame.sprite.Group()
        own_sprites.add(back, store, earth)
        store_sprites.add(scroll, pickaxe, drill,click,bomb)

    class Sounds:
        click_sound = Sound('scr/sound/bull.wav')
        bye_sound = Sound('scr/sound/kassa.mp3')
        bye_sound.set_volume(0.1)

    class Fonts:
        csr = 'scr/fonts/'
        money_show = Text('scr/fonts/Pixel.otf', 36)
        pickaxe_price = Text('scr/fonts/Pixel.otf', 20)
        drill_price = Text('scr/fonts/Pixel.otf', 20)
        click_prise = Text('scr/fonts/Pixel.otf', 20)
        bomb_prise = Text('scr/fonts/Pixel.otf', 20)
        pickaxe_count = Text('scr/fonts/Pixel.otf', 20)
        drill_count = Text('scr/fonts/Pixel.otf', 20)
        click_count = Text('scr/fonts/Pixel.otf', 20)
        bomb_count = Text('scr/fonts/Pixel.otf', 20)
