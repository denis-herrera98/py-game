#!/usr/bin/python3.9
import os
import pygame
from character import Character
from platform import Platform 
from settings import *


class App:

    def __init__(self):
        self._running = True
        self._WIDTH =  WINDOW_WIDTH 
        self._HEIGHT = WINDOW_HEIGHT 
        self._FPS = FPS 
        self._all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()

    def start_over(self):
        pass

    def on_init(self):
        pygame.init()
        pygame.mixer.init()
        self._running = True
        self._FramePerSec = pygame.time.Clock()
        pygame.display.set_caption("FIRST AND LAST LEVEL")

        self._background = pygame.transform.scale(pygame.image.load(os.path.join(
            'Assets', 'day.png')), (self._WIDTH, self._HEIGHT))
        self._display_surf = pygame.display.set_mode(
                (self._WIDTH, self._HEIGHT))
        self._display_surf.blit(self._background, (0, 0))


        self.player = Character(PLAYER_WIDTH, PLAYER_HEIGHT)
        self._all_sprites.add(self.player)

        p1 = Platform(0, WINDOW_HEIGHT - 200, WINDOW_WIDTH, 200) 
        p2 = Platform(WINDOW_WIDTH / 2, WINDOW_HEIGHT /2 - 200 , WINDOW_WIDTH / 2, 100) 
        self.platforms.add(p1)
        self.platforms.add(p2)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False


    def update(self):
        self._all_sprites.update()

        hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
        if hits:
            self.player.pos.y = hits[0].rect.top
            self.player.vel.y = 0

        pass

    def draw(self):
        self._display_surf.blit(self._background, (0, 0))
        self.platforms.draw(self._display_surf)
        self._all_sprites.draw(self._display_surf)

        pygame.display.flip()
        # *after* drawing everything, flip the display
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):

        self._running = True
        self.on_init()


        while(self._running):

            self._FramePerSec.tick(self._FPS)

            for event in pygame.event.get():
                self.on_event(event)

            self.update()
            self.draw()

        self.on_cleanup()


if __name__ == "__main__":
    app = App()
    app.on_execute()
