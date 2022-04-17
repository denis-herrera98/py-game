# !/usr/bin/python3.9
import os
import pygame


class Character(pygame.sprite.Sprite):

    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        self._WIDTH = width
        self._HEIGHT = height
        # self.rect = pygame.Rect(300, 100, self._WIDTH, self._HEIGHT)

        self.image = pygame.transform.scale(pygame.image.load(os.path.join(
            'Assets', 'cuca.png')), (self._WIDTH, self._HEIGHT))
        self.rect = self.image.get_rect()

    def update (self):
        self.handle_movement()

    def handle_movement(self):

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_w]:
            self.rect.y -= 5

        if keys_pressed[pygame.K_s]:
            self.rect.y += 5

        if keys_pressed[pygame.K_a]:
            self.rect.x -= 5

        if keys_pressed[pygame.K_d]:
            self.rect.x += 5
