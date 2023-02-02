from functools import wraps

import pygame
from Constants import GameConstants as gk

pygame.init()
screen = pygame.display.set_mode([600, 600])
#
# last = {}
#
#
# def timer(x):
#     def par(fun):
#         def wrapper():
#             global last
#             last.setdefault(fun.__name__,0)
#             now = pygame.time.get_ticks()
#             if now - last[fun.__name__] > x:
#                 fun()
#                 last[fun.__name__] = now
#                 print(last)
#
#         return wrapper
#
#     return par


class Timer:
    def __init__(self, x):
        self.last = 0
        self.x = x

    def __call__(self, fun):
        def wrapper(*args, **kwargs):
            now = pygame.time.get_ticks()
            if now - self.last > self.x:
                fun()
                self.last = now
        return wrapper
