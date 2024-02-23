import pygame
from constants import *
from random import randint

# Worker1
worker1_ready = pygame.image.load('images/player1/worker/ready.png')

worker1_run_left = [
    pygame.transform.flip(pygame.image.load('images/player1/worker/run-0.png'), True, False),
    pygame.transform.flip(pygame.image.load('images/player1/worker/run-1.png'), True, False),
    pygame.transform.flip(pygame.image.load('images/player1/worker/run-2.png'), True, False),
    pygame.transform.flip(pygame.image.load('images/player1/worker/run-3.png'), True, False),
    pygame.transform.flip(pygame.image.load('images/player1/worker/run-4.png'), True, False),
    pygame.transform.flip(pygame.image.load('images/player1/worker/run-5.png'), True, False)]

worker1_run_right = [
    pygame.image.load('images/player1/worker/run-0.png'),
    pygame.image.load('images/player1/worker/run-1.png'),
    pygame.image.load('images/player1/worker/run-2.png'),
    pygame.image.load('images/player1/worker/run-3.png'),
    pygame.image.load('images/player1/worker/run-4.png'),
    pygame.image.load('images/player1/worker/run-5.png')]

worker1_dig = [
    pygame.transform.flip(pygame.image.load('images/player1/worker/dig-0.png'), True, False),
    pygame.transform.flip(pygame.image.load('images/player1/worker/dig-1.png'), True, False),
    pygame.transform.flip(pygame.image.load('images/player1/worker/dig-2.png'), True, False),
    pygame.transform.flip(pygame.image.load('images/player1/worker/dig-3.png'), True, False),
    pygame.transform.flip(pygame.image.load('images/player1/worker/dig-4.png'), True, False),
    pygame.transform.flip(pygame.image.load('images/player1/worker/dig-5.png'), True, False),
    pygame.transform.flip(pygame.image.load('images/player1/worker/dig-6.png'), True, False),
    pygame.transform.flip(pygame.image.load('images/player1/worker/dig-7.png'), True, False),
    pygame.transform.flip(pygame.image.load('images/player1/worker/dig-8.png'), True, False)]

worker1_repair = [
    pygame.image.load('images/player1/worker/repair-0.png'),
    pygame.image.load('images/player1/worker/repair-1.png'),
    pygame.image.load('images/player1/worker/repair-2.png'),
    pygame.image.load('images/player1/worker/repair-3.png')]

# Worker2
worker2_ready = pygame.image.load('images/player2/worker/ready.png')

worker2_run_left = [
    pygame.transform.flip(pygame.image.load('images/player2/worker/run-0.png'), True, False),
    pygame.transform.flip(pygame.image.load('images/player2/worker/run-1.png'), True, False),
    pygame.transform.flip(pygame.image.load('images/player2/worker/run-2.png'), True, False),
    pygame.transform.flip(pygame.image.load('images/player2/worker/run-3.png'), True, False),
    pygame.transform.flip(pygame.image.load('images/player2/worker/run-4.png'), True, False),
    pygame.transform.flip(pygame.image.load('images/player2/worker/run-5.png'), True, False)]

worker2_run_right = [
    pygame.image.load('images/player2/worker/run-0.png'),
    pygame.image.load('images/player2/worker/run-1.png'),
    pygame.image.load('images/player2/worker/run-2.png'),
    pygame.image.load('images/player2/worker/run-3.png'),
    pygame.image.load('images/player2/worker/run-4.png'),
    pygame.image.load('images/player2/worker/run-5.png')]

worker2_dig = [
    pygame.transform.flip(pygame.image.load('images/player2/worker/dig-0.png'), True, False),
    pygame.transform.flip(pygame.image.load('images/player2/worker/dig-1.png'), True, False),
    pygame.transform.flip(pygame.image.load('images/player2/worker/dig-2.png'), True, False),
    pygame.transform.flip(pygame.image.load('images/player2/worker/dig-3.png'), True, False),
    pygame.transform.flip(pygame.image.load('images/player2/worker/dig-4.png'), True, False),
    pygame.transform.flip(pygame.image.load('images/player2/worker/dig-5.png'), True, False),
    pygame.transform.flip(pygame.image.load('images/player2/worker/dig-6.png'), True, False),
    pygame.transform.flip(pygame.image.load('images/player2/worker/dig-7.png'), True, False),
    pygame.transform.flip(pygame.image.load('images/player2/worker/dig-8.png'), True, False)]

worker2_repair = [
    pygame.image.load('images/player2/worker/repair-0.png'),
    pygame.image.load('images/player2/worker/repair-1.png'),
    pygame.image.load('images/player2/worker/repair-2.png'),
    pygame.image.load('images/player2/worker/repair-3.png')]


class Worker(pygame.sprite.Sprite):
    def __init__(self, ready, run_left, run_right, dig, repair, x):
        super().__init__()

        # Attributes
        self.ready = ready
        self.run_left_sprites = run_left
        self.run_right_sprites = run_right
        self.dig_sprites = dig
        self.repair_sprites = repair
        self.x = x
        self.image = self.ready
        self.rect = self.image.get_rect(midbottom=(self.x, 250 - GROUND_HEIGHT))
        # Phase
        self.run_left = False
        self.run_right = False
        self.dig = False
        self.repair = False
        self.tic = 0
        self.index = 0
        self.time = 0

    def update(self):
        self.time += 1

        # Animation running to mine
        if self.time > WORKER_TRAIN and self.dig == False and self.run_left == True and self.repair == False:
            self.tic += 1
            if self.tic == 6:
                self.index += 1
                self.tic = 0
            if self.index >= len(self.run_left_sprites):
                self.index = 0

            self.rect.x -= WORKER_SPEED
            self.image = self.run_left_sprites[self.index]

        # Animation running to wall
        elif self.time > 100 and self.dig == False and self.run_right == True and self.repair == False:
            self.tic += 1
            if self.tic == 6:
                self.index += 1
                self.tic = 0
            if self.index >= len(self.run_right_sprites):
                self.index = 0

            self.rect.x += WORKER_SPEED
            self.image = self.run_right_sprites[self.index]

        # Animation for Digging
        if self.dig == True:
            self.repair = False
            self.run_right = False
            self.run_left = False
            self.tic += 1
            if self.tic == 6:
                self.index += 1
                self.tic = 0
            if self.index >= len(self.dig_sprites):
                self.index = 0
            self.image = self.dig_sprites[self.index]

        # Animation for Repairing
        elif self.repair == True:
            self.dig = False
            self.run_left = False
            self.run_right = False
            self.tic += 1
            if self.tic == 6:
                self.index += 1
                self.tic = 0
            if self.index >= len(self.repair_sprites):
                self.index = 0
            self.image = self.repair_sprites[self.index]
