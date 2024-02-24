import pygame



class Building(pygame.sprite.Sprite):
    def __init__(self, picture, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = picture
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)