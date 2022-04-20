# !/usr/bin/python3.9
import os
import pygame
from settings import *
vec = pygame.math.Vector2


class Character(pygame.sprite.Sprite):

    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        self._WIDTH = width
        self._HEIGHT = height
        loadImagine = pygame.image.load(os.path.join(
            'Assets', 'cuca.png')).convert()
        self.image = pygame.transform.scale(loadImagine, (self._WIDTH, self._HEIGHT))
        self.rect = self.image.get_rect()
        self.pos = vec(200,200)
        self.acc = vec(0,0)
        self.vel = vec(0,0)

    def update (self):
        self.handle_movement()
        self.handle_gravity()

    def handle_movement(self):
        self.acc = vec(0, 0.5)
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_a]:
            self.acc.x = -PLAYER_ACC

        if keys_pressed[pygame.K_d]:
            self.acc.x = PLAYER_ACC

        if keys_pressed[pygame.K_s]:
            self.acc.y = PLAYER_ACC

        if keys_pressed[pygame.K_w]:
            self.acc.y = -PLAYER_ACC

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

    def handle_gravity(self):
        self.pos.y += PLAYER_ACC

        if self.pos.y > WINDOW_HEIGHT:
            self.pos.y = 0
            self.rect.midbottom = self.pos

