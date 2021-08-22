import pygame
from pygame import sprite
from pygame import transform

import globs
from globs import TILE_SIZE

from models import EnemyModel, SwordModel

class Entity(sprite.Sprite):

    def __init__(self, image='', pos=(0, 0), size=(1,1), clickable=False, animate=False, **kwargs):

        super(Entity, self).__init__(**kwargs)

        self.clickable = clickable
        self.pos = pos
        self.size = size
        self.animate = animate

        if self.animate:
            self.image = image[0]

        else:
            self.image = image

        self.image = transform.scale(self.image, (TILE_SIZE*size[0], TILE_SIZE*size[1]))
        self.rect = self.image.get_rect()
        self.rect.move_ip(self.pos[0]*TILE_SIZE, self.pos[1]*TILE_SIZE)

        self.current_sprite = 0
        self.animation_speed = 0.25



    def update(self):

        self.current_sprite += self.animation_speed
        self.current_sprite = self.current_sprite % (len(globs.IMAGES["enemy"]))
        self.image = globs.IMAGES["enemy"][int(self.current_sprite)]
        self.image = transform.scale(self.image, (TILE_SIZE*self.size[0], TILE_SIZE*self.size[1]))


    def on_click(self):

        if self.clickable:
            raise NotImplemented

        return

class Enemy(Entity):

    def __init__(self, model: EnemyModel, **kwargs):
        super(Enemy, self).__init__(**kwargs)

        self.model = model

    def update(self):

        super(Enemy, self).update()






class CentralWeaponField(Entity):

    def __init__(self, enemy_model: EnemyModel,
                       weapon_model: SwordModel, **kwargs):

        super(CentralWeaponField, self).__init__(**kwargs)

        self.enemy_model = enemy_model
        self.sword_model = weapon_model


    def update(self):

        self.on_click()


    def on_click(self):

        self.enemy_model.hit(self.sword_model.damage)





