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


