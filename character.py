# !/usr/bin/python3.9
import os
import pygame


class Character(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self._WIDTH = 200
        self._HEIGHT = 200
        self._image = pygame.transform.scale(pygame.image.load(os.path.join(
            'Assets', 'cuca.png')), (self._WIDTH, self._HEIGHT))
        self._rect = pygame.Rect(300, 100, self._WIDTH, self._HEIGHT)

    def draw(self, surface):
        surface.blit(self._image, (self._rect.x, self._rect.y))

    def handle_movement(self, keys_pressed):
        if keys_pressed[pygame.K_w]:
            self._rect.y -= 5

        if keys_pressed[pygame.K_s]:
            self._rect.y += 5

        if keys_pressed[pygame.K_a]:
            self._rect.x -= 5

        if keys_pressed[pygame.K_d]:
            self._rect.x += 5

    def get_Width(self):
        return self._WIDTH

    def get_Height(self):
        return self._HEIGHT
