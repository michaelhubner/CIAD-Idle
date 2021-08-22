import pygame
import sys

import globs

from ._base_loop import BaseLoop

from entities import RenderText

from entities import Entity


import logging



class EndOfDay(BaseLoop):

    TEXT_GROUP = pygame.sprite.RenderUpdates()
    WEAPONS_GROUP = pygame.sprite.Group()

    def __init__(self, screen, clock):

        super(EndOfDay, self).__init__(screen, clock)

        self.image = pygame.image.load(r'D:\Projekte\Python\CIAD-Idle\resources\background\Suelo nieve.jpg')
        self.surface = pygame.transform.scale(self.image, (globs.WIDTH, globs.HEIGHT))
        self.font_path = r'D:\Projekte\Python\CIAD-Idle\resources\Sprites\Font\kenvector_future.ttf'

        self.sword_text = RenderText(self.surface,
                                     text="Sword-Mastery",
                                     pos=(int(globs.WIDTH/4), int(globs.HEIGHT/4)),
                                     pos_rel=(0, 0),
                                     font=self.font_path,
                                     size=16,
                                     color=globs.BLACK,
                                     antialias=True,
                                     unlocked=True)

        self.skill_text = RenderText(self.surface,
                                     text="Skill-Mastery",
                                     pos=(int(globs.WIDTH/4), int(globs.HEIGHT/4)),
                                     pos_rel=(2, 0),
                                     font=self.font_path,
                                     size=16,
                                     color=globs.BLACK,
                                     antialias=True,
                                     unlocked=True)

        self.TEXT_GROUP.add(self.sword_text)
        self.TEXT_GROUP.add(self.skill_text)

        self.sword = Entity(image=globs.IMAGES["sword_0"],
                            pos=(3, 3),
                            size=(1,1),
                            clickable=True)

        self.wand = Entity(image=globs.IMAGES["wand_0"],
                           pos=(6, 3),
                           size=(1, 1),
                           clickable=True)

        self.WEAPONS_GROUP.add(self.sword)
        self.WEAPONS_GROUP.add(self.wand)

        self.selected_weapon = None
        self.config = None


    def _handle_input(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.stop()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                x,y = event.pos

                for sprite in self.WEAPONS_GROUP:
                    if sprite.rect.collidepoint(x,y):
                        if sprite == self.sword:
                            self.selected_weapon = "sword"
                            self.stop()

                        elif sprite == self.wand:
                            self.selected_weapon = "wand"
                            self.stop()



    def _update_screen(self):

        #first always draw background
        self.screen.blit(self.surface, (0,0))

        # Render Texts
        self.TEXT_GROUP.draw(self.surface)
        self.WEAPONS_GROUP.draw(self.surface)


    def _update_model(self):

        pass

    def _generate_config(self):

        return dict(weapon=self.selected_weapon)








