import pygame
import sys

import globs
from background.map import Map

from entities._text_entity import RenderText
from entities._text_entity import TEXT_GROUP
from entities._entity import CLICKABLE_GROUP, ENEMY_GROUP
from entities._entity import Enemy, CentralWeaponField

from models import EnemyModel, SwordModel

import logging

from ._base_loop import BaseLoop

enemy_image = r'D:\Projekte\Python\CIAD-Idle\resources\Sprites\Entitys\PNG\alien.png'
central_weapon_image = r'D:\Projekte\Python\CIAD-Idle\resources\Sprites\Entitys\Export_64\Sword.png'

class MainGame(BaseLoop):

    def __init__(self, screen, clock):

        super(MainGame, self).__init__(screen, clock)

        self.map = Map()
        self.map.random_map()

        self.status_text = RenderText(self.screen, 'FPS',
                                      size=42,
                                      pos=[50, 50],
                                      pos_rel=(1, 3))

        self.enemy_model = EnemyModel(max_hp=10, defense=0)
        self.sword_model = SwordModel(damage=1)

        self.current_enemy = Enemy(model=self.enemy_model,
                                   image=enemy_image,
                                   pos=globs.ENEMY_POS,
                                   size=(2,2),
                                   clickable=False)

        self.weapon_field = CentralWeaponField(enemy_model=self.enemy_model,
                                               weapon_model=self.sword_model,
                                               image=central_weapon_image,
                                               pos=globs.CENTRAL_WEAPON_POS,
                                               size = (3,2),
                                               clickable=True)

        self._logger = logging.getLogger(self.__class__.__name__)


    def _handle_input(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # First handle clickable Groups
                for clickable in CLICKABLE_GROUP:
                    if clickable.rect.collidepoint(x, y):
                        clickable.update()

    def _update_model(self):

        ENEMY_GROUP.update()


    def _update_screen(self):

        self.map.tile_group.draw(self.screen)

        TEXT_GROUP.draw(self.screen)
        CLICKABLE_GROUP.draw(self.screen)
        ENEMY_GROUP.draw(self.screen)

        self.status_text.print_text('FPS: %d' % self.clock.get_fps())

