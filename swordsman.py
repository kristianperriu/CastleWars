import pygame
from constants import *
from random import randint

swordsman1_ready = pygame.image.load('images/player1/sword/ready.png')

swordsman1_run = [
    pygame.image.load('images/player1/sword/run-0.png'),
    pygame.image.load('images/player1/sword/run-1.png'),
    pygame.image.load('images/player1/sword/run-2.png'),
    pygame.image.load('images/player1/sword/run-3.png'),
    pygame.image.load('images/player1/sword/run-4.png'),
    pygame.image.load('images/player1/sword/run-5.png'),
    pygame.image.load('images/player1/sword/run-6.png'),
    pygame.image.load('images/player1/sword/run-7.png'),
    pygame.image.load('images/player1/sword/run-8.png'),
    pygame.image.load('images/player1/sword/run-9.png'),
    pygame.image.load('images/player1/sword/run-10.png'),
    pygame.image.load('images/player1/sword/run-11.png')]

swordsman1_attack = [
    pygame.image.load('images/player1/sword/attack-0.png'),
    pygame.image.load('images/player1/sword/attack-1.png'),
    pygame.image.load('images/player1/sword/attack-2.png'),
    pygame.image.load('images/player1/sword/attack-3.png'),
    pygame.image.load('images/player1/sword/attack-4.png'),
    pygame.image.load('images/player1/sword/attack-5.png'),
    pygame.image.load('images/player1/sword/attack-6.png'),
    pygame.image.load('images/player1/sword/attack-7.png')]

swordsmasn1_dead = [
    pygame.image.load('images/player1/sword/fallen-0.png'),
    pygame.image.load('images/player1/sword/fallen-1.png'),
    pygame.image.load('images/player1/sword/fallen-2.png'),
    pygame.image.load('images/player1/sword/fallen-3.png'),
    pygame.image.load('images/player1/sword/fallen-4.png'),
    pygame.image.load('images/player1/sword/fallen-5.png')]

swordsman2_ready = pygame.image.load('images/player2/sword/ready.png')

swordsman2_run = [
    pygame.image.load('images/player2/sword/run-0.png'),
    pygame.image.load('images/player2/sword/run-1.png'),
    pygame.image.load('images/player2/sword/run-2.png'),
    pygame.image.load('images/player2/sword/run-3.png'),
    pygame.image.load('images/player2/sword/run-4.png'),
    pygame.image.load('images/player2/sword/run-5.png'),
    pygame.image.load('images/player2/sword/run-6.png'),
    pygame.image.load('images/player2/sword/run-7.png'),
    pygame.image.load('images/player2/sword/run-8.png'),
    pygame.image.load('images/player2/sword/run-9.png'),
    pygame.image.load('images/player2/sword/run-10.png'),
    pygame.image.load('images/player2/sword/run-11.png')]

swordsman2_attack = [
    pygame.image.load('images/player2/sword/attack-0.png'),
    pygame.image.load('images/player2/sword/attack-1.png'),
    pygame.image.load('images/player2/sword/attack-2.png'),
    pygame.image.load('images/player2/sword/attack-3.png'),
    pygame.image.load('images/player2/sword/attack-4.png'),
    pygame.image.load('images/player2/sword/attack-5.png'),
    pygame.image.load('images/player2/sword/attack-6.png'),
    pygame.image.load('images/player2/sword/attack-7.png')]

swordsman2_dead = [
    pygame.image.load('images/player2/sword/fallen-0.png'),
    pygame.image.load('images/player2/sword/fallen-1.png'),
    pygame.image.load('images/player2/sword/fallen-2.png'),
    pygame.image.load('images/player2/sword/fallen-3.png'),
    pygame.image.load('images/player2/sword/fallen-4.png'),
    pygame.image.load('images/player2/sword/fallen-5.png')]


class Swordsman(pygame.sprite.Sprite):

    def __init__(self, ready, run, attack, dead, x, player):
        super().__init__()

        # Attributes
        self.ready = ready
        self.run_sprites = run
        self.attack_sprites = attack
        self.dead_sprites = dead
        self.player = player
        self.image = self.ready
        self.x = x
        self.rect = self.image.get_rect(midbottom=(self.x, 250 - GROUND_HEIGHT))
        self.health = SWORD_HEALTH
        # Phase
        self.unleash = False
        self.attacking = False
        self.tic = 0
        self.index = 0
        self.time = 0

    def update(self):
        if self.health <= 0:
            self.tic += 1
            if self.tic >= 6:
                self.index += 0.5
                self.tic = 0
            if self.index >= len(self.dead_sprites):
                self.index = 0
                self.kill()
            self.image = self.dead_sprites[int(self.index)]

        elif self.time < SWORD_TRAIN:
            self.time += 1
        else:
            # do running Animation
            if self.unleash == True:
                self.tic += 1
                if self.tic >= 6:
                    self.index += 1
                    self.tic = 0
                if self.index >= len(self.run_sprites):
                    self.index = 0
                self.image = self.run_sprites[self.index]
                if self.player == 1:
                    self.rect.x += SWORD_SPEED
                else:
                    self.rect.x -= SWORD_SPEED

                # do attacking animation
            elif self.attacking == True:
                self.tic += 1
                if self.tic >= 6:
                    self.index += 1
                    self.tic = 0
                if self.index >= len(self.attack_sprites):
                    self.index = 0
                self.image = self.attack_sprites[self.index]
