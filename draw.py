from util import *
from GameRes import GameResources as res
from Constants import GameConstants as gk


def own_draw():
    res.Sprites.own_sprites.draw(screen)
    res.Fonts.money_show.render(f"{str(round(gk.money,2))}$", True, (0, 255, 0), screen, 10, 10)
    res.Fonts.pickaxe_count.render(str(gk.pickaxe_counter), True, (255, 0, 0), screen, 500, 500)
    res.Fonts.drill_count.render(str(gk.drill_counter), True, (255, 0, 0), screen, 500, 560)
    res.Sprites.pickaxe2.render(screen)
    res.Sprites.drill2.render(screen)


def store_draw():
    res.Sprites.store_sprites.draw(screen)
    res.Fonts.pickaxe_price.render('price 10', True, (255, 0, 255), screen, 200, 140)
    res.Fonts.drill_price.render('price 100', True, (255, 0, 255), screen, 300, 140)
