import pygame
from constants import *

# archer arrows
a_arrow1 = pygame.image.load('images/player1/bow/arrowhor-0.png')
a_arrow2 = pygame.image.load('images/player2/bow/arrowhor-0.png')

# tower arrows
t_arrow1 = [pygame.image.load('images/player1/bow/arrowdiag-0.png')]
t_arrow2 = [pygame.image.load('images/player2/bow/arrowdiag-0.png')]

class Arrow(pygame.sprite.Sprite):
    def __init__(self, arrow, position, a_type, x, y):
        super().__init__()
        self.position = position
        self.image = arrow
        self.a_type = a_type
        self.x = x
        self.y = y
        if self.a_type == "archer":
            self.rect = self.image.get_rect(midbottom=(self.position, SCREEN_HEIGHT - 23))
        else:
            self.rect = self.image.get_rect(centre=(WALL_POS, TOWER_HEIGHT))

    def update(self):
        self.rect.x += self.x
        self.rect.y += self.y
