import pygame
from constants import *

archer1_ready = pygame.image.load('images/player1/bow/ready.png')

archer1_run = [pygame.image.load('images/player1/bow/run-0.png'),
               pygame.image.load('images/player1/bow/run-1.png'),
               pygame.image.load('images/player1/bow/run-2.png'),
               pygame.image.load('images/player1/bow/run-3.png'),
               pygame.image.load('images/player1/bow/run-4.png'),
               pygame.image.load('images/player1/bow/run-5.png'),
               pygame.image.load('images/player1/bow/run-6.png'),
               pygame.image.load('images/player1/bow/run-7.png'),
               pygame.image.load('images/player1/bow/run-8.png'),
               pygame.image.load('images/player1/bow/run-9.png'),
               pygame.image.load('images/player1/bow/run-10.png'),
               pygame.image.load('images/player1/bow/run-11.png')]

archer1_shoot = [pygame.image.load('images/player1/bow/shoot-0.png'),
                 pygame.image.load('images/player1/bow/shoot-1.png')]

archer1_dead = [pygame.image.load('images/player1/bow/fallen-0.png'),
                pygame.image.load('images/player1/bow/fallen-1.png'),
                pygame.image.load('images/player1/bow/fallen-2.png'),
                pygame.image.load('images/player1/bow/fallen-3.png'),
                pygame.image.load('images/player1/bow/fallen-4.png'),
                pygame.image.load('images/player1/bow/fallen-5.png')]

archer2_ready = pygame.image.load('images/player2/bow/ready.png')

archer2_run = [pygame.image.load('images/player2/bow/run-0.png'),
               pygame.image.load('images/player2/bow/run-1.png'),
               pygame.image.load('images/player2/bow/run-2.png'),
               pygame.image.load('images/player2/bow/run-3.png'),
               pygame.image.load('images/player2/bow/run-4.png'),
               pygame.image.load('images/player2/bow/run-5.png'),
               pygame.image.load('images/player2/bow/run-6.png'),
               pygame.image.load('images/player2/bow/run-7.png'),
               pygame.image.load('images/player2/bow/run-8.png'),
               pygame.image.load('images/player2/bow/run-9.png'),
               pygame.image.load('images/player2/bow/run-10.png'),
               pygame.image.load('images/player2/bow/run-11.png')]

archer2_shoot = [pygame.image.load('images/player2/bow/shoot-0.png'),
                 pygame.image.load('images/player2/bow/shoot-1.png'),
                 pygame.image.load('images/player2/bow/shoot-0.png'),
                 pygame.image.load('images/player2/bow/shoot-1.png')
                 ]

archer2_dead = [pygame.image.load('images/player2/bow/fallen-0.png'),
                pygame.image.load('images/player2/bow/fallen-1.png'),
                pygame.image.load('images/player2/bow/fallen-2.png'),
                pygame.image.load('images/player2/bow/fallen-3.png'),
                pygame.image.load('images/player2/bow/fallen-4.png'),
                pygame.image.load('images/player2/bow/fallen-5.png')]


class Archer(pygame.sprite.Sprite):
    def __init__(self, ready, run, shoot, dead, x, player):
        super().__init__()

        # Attributes
        self.ready = ready
        self.run_sprites = run
        self.shoot_sprites = shoot
        self.dead_sprites = dead
        self.x = x
        self.player = player
        self.image = self.ready
        self.rect = self.image.get_rect(midbottom=(x - 10, 250 - GROUND_HEIGHT))
        self.health = ARCHER_HEALTH
        # Phase
        self.unleash = False
        self.shoot = False
        self.tic = 0
        self.index = 0
        self.time = 0

    def update(self):
        # archer dying
        if self.health <= 0:
            self.tic += 1
            if self.tic >= 6:
                self.index += 0.5
                self.tic = 0
            if self.index >= len(self.dead_sprites):
                self.index = 0
                self.kill()
            self.image = self.dead_sprites[int(self.index)]

        elif self.time < ARCHER_TRAIN:
            self.time += 1

        else:
            # running animation
            if self.unleash:
                self.tic += 1
                if self.tic >= 6:
                    self.index += 1
                    self.tic = 0
                if self.index >= len(self.run_sprites):
                    self.index = 0
                self.image = self.run_sprites[int(self.index)]
                if self.player == 1:
                    self.rect.x += ARCHER_SPEED
                else:
                    self.rect.x -= ARCHER_SPEED
            # shooting animation
            elif self.shoot:
                self.tic += 1
                if self.tic >= 6:
                    self.index += 0.2
                    self.tic = 0
                if self.index >= len(self.shoot_sprites):
                    self.index = 0
                self.image = self.shoot_sprites[int(self.index)]