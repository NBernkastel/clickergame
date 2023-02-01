import pygame


class Sprite(pygame.sprite.Sprite):
    def __init__(self, src: str, width: int, height: int, x: int, y: int):
        super().__init__()
        self.x_start = x
        self.y_start = y
        self.src = src
        self.width = width
        self.height = height
        self.image = pygame.image.load(src)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def render(self, screen):
        screen.blit(self.image, self.rect)


class Text(pygame.font.Font):
    def __init__(self, name, size: int):
        super().__init__(name, size)

    def render(self, text: str, antialias: bool, color, screen, x: int, y: int):
        text = super().render(text, antialias, color)
        screen.blit(text, (x, y))


class Money:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrsuvwxyz"

    def __init__(self):
        self.__moneydec = 0
        self.__money = ''

    def __add__(self, other):
        k = int(other) % 17
        self.__money += self.digits[k]

    def __iadd__(self, other):
        self.__money = self.trans(other)
        return self

    def __ge__(self, other):
        if other >= self.__moneydec:
            return True
        else:
            return False

    def __isub__(self, other):
        self.__money = self.trans(-other)
        return self

    def trans(self, other):
        n = other + self.__moneydec
        self.__moneydec = n
        if n == 0:
            return "0"
        r = ""
        while n > 0:
            k = n % 61  # очередная цифра
            r = self.digits[int(k)] + r  # приклеим к результату
            n = n // 61
        return r

    @property
    def money(self):
        return self.__moneydec


money = Money()
money += 1


class H:
    x = 5
