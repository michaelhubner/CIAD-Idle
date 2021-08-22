import pygame
import sys

import globs
import logging

class BaseLoop():


    def __init__(self, screen, clock):



        self.screen = screen
        self.clock = clock

        self.running = False
        self.config = None
        self._logger = logging.getLogger(self.__class__.__name__)


    def run(self):

        self._logger.debug("Started")

        while self.running:

            self.clock.tick(globs.FPS)

            self._handle_input()
            self._update_model()
            self._update_screen()

            pygame.display.flip()


    def start(self, config=None):
        self.running = True
        self.config = self._load_config(config)


    def stop(self, **kwargs):

        self.running = False
        self.config = self._generate_config()
        self.screen.fill((0,0,0))
        pygame.display.flip()
        self._logger.debug("Stopped")


    def _handle_input(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.stop()


    def _update_screen(self):
        raise NotImplementedError

    def _update_model(self):
        raise NotImplementedError

    def _load_config(self, config):
        self.config = config

    def _generate_config(self):
        return {}

