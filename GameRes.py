import pygame
from pygame.mixer import Sound

from Classes import Sprite, Text


class GameResources:
    class Sprites:
        earth = Sprite('scr/img/earth.png', 150, 150, 250, 250)
        back = Sprite('scr/img/space.jpg', 600, 600, 0, 0)
        store = Sprite('scr/img/store.png', 64, 32, 510, 15)
        scroll = Sprite('scr/img/scroll.png', 350, 550, 130, 20)
        pickaxe = Sprite('scr/img/pickaxe.png', 40, 40, 220, 100)
        pickaxe2 = Sprite('scr/img/pickaxe.png', 40, 40, 480, 495)
        drill = Sprite('scr/img/drill.png', 40, 40, 330, 100)
        drill2 = Sprite('scr/img/drill.png', 40, 40, 480, 550)

        own_sprites = pygame.sprite.Group()
        store_sprites = pygame.sprite.Group()
        own_sprites.add(back, store, earth)
        store_sprites.add(scroll, pickaxe, drill)

    class Sounds:
        click_sound = Sound('scr/sound/bull.wav')
        bye_sound = Sound('scr/sound/kassa.mp3')
        bye_sound.set_volume(0.3)

    class Fonts:
        csr = 'scr/fonts/'
        money_show = Text('scr/fonts/Pixel.otf', 36)
        pickaxe_price = Text('scr/fonts/Pixel.otf', 20)
        drill_price = Text('scr/fonts/Pixel.otf', 20)
        pickaxe_count = Text('scr/fonts/Pixel.otf', 20)
        drill_count = Text('scr/fonts/Pixel.otf', 20)
