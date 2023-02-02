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

    def __init__(self):
        self.__money_dec = 1000000
        self.__money = ''

    def __add__(self, other):
        self.__money_dec += other
        self.trans()

    def __iadd__(self, other):
        self.__money_dec += other
        self.trans()
        return self

    def __ge__(self, other):
        if other <= self.__money_dec:
            return True
        else:
            return False

    def __isub__(self, other):
        self.__money_dec -= other
        self.trans()
        return self

    def trans(self):
        if self.__money_dec / 1000000000 >= 1:
            self.__money = str(round(self.__money_dec / 1000000000, 2)) + 'G'
        elif self.__money_dec / 1000000 >= 1:
            self.__money = str(round(self.__money_dec/1000000,2)) + 'M'
        elif self.__money_dec / 1000 >= 1:
            self.__money = str(round(self.__money_dec/1000,2)) + 'K'
        else:
            self.__money = str(self.__money_dec)

    @property
    def money(self):
        return self.__money

