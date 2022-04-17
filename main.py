#!/usr/bin/python3.9
import os
import pygame
from character import Character
from platform import Platform 


class App:

    def __init__(self):
        self._running = True
        self._player = Character(200, 200)
        self._WIDTH = 900
        self._HEIGHT = 500
        self._FPS = 60
        self._all_sprites = pygame.sprite.Group()
        self._platforms = pygame.sprite.Group()

        p1 = Platform(0, 50, 40, 50) 
        self._platforms.add(p1)

    def on_init(self):
        pygame.init()
        pygame.mixer.init()
        self._running = True
        self._FramePerSec = pygame.time.Clock()
        self._FramePerSec.tick(self._FPS)
        pygame.display.set_caption("FIRST AND LAST LEVEL")
        self._background = pygame.transform.scale(pygame.image.load(os.path.join(
            'Assets', 'day.png')), (self._WIDTH, self._HEIGHT))
        self._display_surf = pygame.display.set_mode(
                (self._WIDTH, self._HEIGHT))
        self._display_surf.blit(self._background, (0, 0))
        self._all_sprites.add(self._player)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False


    def update(self):
        self._all_sprites.update()

        pass

    def draw(self):
        self._all_sprites.draw(self._display_surf)
        #hits = pygame.sprite.spritecollide(self._player, self._platforms, False)
        #if hits:
            #self._player.pos.y = hits[0].rect.top
            #self._player.vel.y = 0
        self._display_surf.blit(self._background, (0, 0))
        self._all_sprites.draw(self._display_surf)
        # *after* drawing everything, flip the display
        pygame.display.flip()
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):

        self._running = True
        self.on_init()

        while(self._running):

            for event in pygame.event.get():
                self.on_event(event)

            self.draw()
            self.update()

        self.on_cleanup()


if __name__ == "__main__":
    app = App()
    app.on_execute()
