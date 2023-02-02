from util import *
from GameRes import GameResources as res
from Constants import GameConstants as gk


def own_draw():
    res.Sprites.own_sprites.draw(screen)
    res.Fonts.money_show.render(f"{str(gk.money.money)}$", True, (0, 255, 0), screen, 10, 10)
    res.Fonts.pickaxe_count.render(str(gk.pickaxe_counter), True, (255, 0, 0), screen, 500, 400)
    res.Fonts.drill_count.render(str(gk.drill_counter), True, (255, 0, 0), screen, 500, 460)
    res.Fonts.click_count.render(str(gk.click_counter), True, (255, 0, 0), screen, 500, 350)
    res.Fonts.bomb_count.render(str(gk.bomb_counter), True, (255, 0, 0), screen, 500, 510)
    res.Sprites.pickaxe2.render(screen)
    res.Sprites.drill2.render(screen)
    res.Sprites.click2.render(screen)
    res.Sprites.bomb2.render(screen)


def store_draw():
    res.Sprites.store_sprites.draw(screen)
    res.Fonts.pickaxe_price.render('price 1000', True, (255, 0, 255), screen, 300, 140)
    res.Fonts.drill_price.render('price 10000', True, (255, 0, 255), screen, 200, 220)
    res.Fonts.click_prise.render('price X^10', True, (255, 0, 255), screen, 200, 140)
    res.Fonts.bomb_prise.render('price 1M', True, (255, 0, 255), screen, 300, 220)
