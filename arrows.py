import pygame
from constants import *

# archer arrows
a_arrow1 = pygame.image.load('images/player1/bow/arrowhor-0.png')
a_arrow2 = pygame.image.load('images/player2/bow/arrowhor-0.png')

# tower arrows
t_arrow1 = pygame.image.load('images/player1/bow/arrowdiag-0.png')
t_arrow2 = pygame.image.load('images/player2/bow/arrowdiag-0.png')


class Archer_Arrow(pygame.sprite.Sprite):
    def __init__(self, arrow, position, player):
        super().__init__()
        self.position = position
        self.image = arrow
        self.player = player
        self.rect = self.image.get_rect(midbottom=(self.position, SCREEN_HEIGHT - 23))

    def update(self):
        if self.player == 1:
            self.rect.x += ARROW_SPEED
        else:
            self.rect.x -= ARROW_SPEED


class Tower_Arrow(pygame.sprite.Sprite):
    def __init__(self, arrow, x, y, x_speed, y_speed, player):
        super().__init__()
        self.image = arrow
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.player = player
        self.rect = self.image.get_rect(midbottom=(self.x, y))

    def update(self):
        if self.player == 1:
            self.rect.x += self.x_speed
            self.rect.y += self.y_speed
        elif self.player == 2:
            self.rect.x -= self.x_speed
            self.rect.y += self.y_speed
