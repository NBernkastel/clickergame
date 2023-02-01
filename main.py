from util import *
import pygame.sprite
from Classes import *
from Constants import GameConstants as gk
from events import events
from main_logic import click_logic, store_logic, work
from GameRes import GameResources as res
from draw import store_draw, own_draw
import time

class Game:
    clock = pygame.time.Clock()
    start_time = time.time()
    current_time = start_time
    def run(self):
        while gk.running:
            self.current_time = round(time.time() - self.start_time,2)
            gk.ticks = round(self.current_time * 60)
            gk.mouse_position = tuple([0, 0])
            events()
        # Events
            screen.fill((255, 255, 255))
        # Body
            own_draw()
            if click_logic(res.Sprites.earth):
                gk.money += 1
                res.Sounds.click_sound.play()
            if click_logic(res.Sprites.store):
                if gk.store_check:
                    gk.store_check = False
                else:
                    gk.store_check = True
            if gk.store_check:
                store_logic()
                store_draw()
            work()
            print(gk.ticks)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
