#!/usr/bin/python3.9
import os
import pygame
from character import Character


class App:

    def __init__(self):
        self._running = True
        self._player = Character()
        self._display_surf = None
        self._WIDTH = 900
        self._HEIGHT = 500
        self.FPS = 60
        self._background = pygame.transform.scale(pygame.image.load(os.path.join(
            'Assets', 'day.png')), (self._WIDTH, self._HEIGHT))
        self._display_surf = pygame.display.set_mode(
                (self._WIDTH, self._HEIGHT))
        self._display_surf.blit(self._background, (0, 0))

    def on_init(self):
        pygame.init()
        self._running = True
        self._FramePerSec = pygame.time.Clock()
        self._FramePerSec.tick(self.FPS)
        self._player.draw(self._display_surf)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        keys_pressed = pygame.key.get_pressed()
        self._player.handle_movement(keys_pressed)

    def on_loop(self):
        self._display_surf.blit(self._background, (0, 0))
        pass

    def on_render(self):
        self._player.draw(self._display_surf)
        pygame.display.update()
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):

        self._running = True
        self.on_init()

        while(self._running):

            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()

        self.on_cleanup()


if __name__ == "__main__":
    app = App()
    app.on_execute()
