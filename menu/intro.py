import pygame
import sys

import globs
import logging

from ._base_loop import BaseLoop
from entities import RenderText



class Intro(BaseLoop):

    TEXT_GROUP = pygame.sprite.RenderUpdates()


    def __init__(self, screen, clock):

        super(Intro, self).__init__(screen, clock)

        self.image = pygame.image.load(r'D:\Projekte\Python\CIAD-Idle\resources\background\Suelo nieve.jpg')
        self.surface = pygame.transform.scale(self.image, (globs.WIDTH, globs.HEIGHT))
        self.font_path = r'D:\Projekte\Python\CIAD-Idle\resources\Sprites\Font\kenvector_future.ttf'

        self.welcome_text = RenderText(self.surface,
                                      text="Welcome to Call It a Day - Idle",
                                      pos=(int(globs.WIDTH/2), int(globs.HEIGHT/4)),
                                      pos_rel=(1, 0),
                                      font=self.font_path,
                                      size=36,
                                      color=globs.BLACK,
                                      antialias=True)

        self.start_text = RenderText(self.surface,
                                     text="BEGIN",
                                     pos=(int(globs.WIDTH/2), int(globs.HEIGHT/2)),
                                     pos_rel=(1, 0),
                                     font=self.font_path,
                                     size=24,
                                     color=globs.BLACK,
                                     antialias=True,
                                     selcetable=True)

        self.settings_text = RenderText(self.surface,
                                        text="Settings",
                                        pos=(int(globs.WIDTH/2), int(globs.HEIGHT/2)),
                                        pos_rel=(1, -4),
                                        font=self.font_path,
                                        size=24,
                                        color=globs.BLACK,
                                        antialias=True,
                                        selcetable=True)

        self.TEXT_GROUP.add(self.welcome_text)
        self.TEXT_GROUP.add(self.start_text)
        self.TEXT_GROUP.add(self.settings_text)


    def _handle_input(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.stop()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                x,y = event.pos

                try:
                    text_collision = next(sprite for sprite in self.TEXT_GROUP if sprite.rect.collidepoint(x,y))
                except StopIteration:
                    text_collision = None

                if text_collision == self.start_text:
                    self.running = False

            if event.type == pygame.MOUSEMOTION:

                x, y = event.pos
                for sprite in self.TEXT_GROUP:
                    if sprite.rect.collidepoint(x, y):
                        sprite.selected = True

                    else:
                        sprite.selected = False



    def _update_screen(self):

        self
        #first always draw background
        self.screen.blit(self.surface, (0,0))

        # Render Texts
        self.TEXT_GROUP.draw(self.surface)


    def _update_model(self):

        pass





