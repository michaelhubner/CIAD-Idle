import pygame
import sys

import globs
import logging

from ._base_loop import BaseLoop

class Intro(BaseLoop):


    def __init__(self, screen, clock):

        super(Intro, self).__init__(screen, clock)

        self.image = pygame.image.load(r'D:\Projekte\Python\CIAD-Idle\resources\background\Suelo nieve.jpg')
        self.surface = pygame.transform.scale(self.image, (globs.WIDTH, globs.HEIGHT))

    def _handle_input(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.stop()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.stop()

    def _update_screen(self):

        self.screen.blit(self.surface, (0,0))

    def _update_model(self):

        pass


