import pygame
import sys

import globs
import logging

from menu import Intro, MainGame, EndOfDay

formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, format=formatter)


"""
enemy_1 = r'D:\Projekte\Python\BGTTD\Sprites\Entitys\PNG\alien.png'
projectile = r'D:\Projekte\Python\BGTTD\Sprites\Entitys\PNG\projectile.png'
hero_1 = r'D:\Projekte\Python\BGTTD\Sprites\Entitys\PNG\little_hero.png'

enemy_1_image = pygame.image.load(enemy_1).convert()
projectile_iage = pygame.image.load(projectile).convert()
hero_1_image = pygame.image.load(hero_1).convert()
"""



class GameStateMaschine():

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(globs.SIZE)

    def __init__(self):

        self.running = True

        self._states = {"Intro": Intro(self.screen, self.clock),
                        "EOD": EndOfDay(self.screen, self.clock),
                        "Main": MainGame(self.screen, self.clock)}


        self.state = self._states["Intro"]
        self.state.start()

        self._logger = logging.getLogger(self.__class__.__name__)

    def run(self):

        self._logger.debug("Started")

        while self.running:

            self._handle_input()
            self.state.run()
            self._change_state(self.state)

            self.clock.tick(globs.FPS)



    def _handle_input(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False
                sys.exit()




    def _change_state(self, last_state):

        if last_state == self._states["Intro"]:
            self.state = self._states["EOD"]

        elif last_state == self._states["EOD"]:
            self.state = self._states["Main"]

        self.state.start(config=last_state.config)







