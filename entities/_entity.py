import pygame
from pygame import sprite
from pygame import transform

from globs import TILE_SIZE

from models import EnemyModel, SwordModel

CLICKABLE_GROUP = pygame.sprite.Group()
ENEMY_GROUP = pygame.sprite.Group()

class Entity(sprite.Sprite):

    def __init__(self, image='', pos=(0, 0), size=(1,1), clickable=False, **kwargs):

        super(Entity, self).__init__(**kwargs)

        self.clickable = clickable
        self.pos = pos
        self.size = size
        self.image = pygame.image.load(image).convert()
        self.image = transform.scale(self.image, (TILE_SIZE*size[0], TILE_SIZE*size[1]))
        self.rect = self.image.get_rect()
        self.rect.move_ip(self.pos[0]*TILE_SIZE, self.pos[1]*TILE_SIZE)

        if self.clickable:
            CLICKABLE_GROUP.add(self)


    def update(self):
        pass

    def on_click(self):

        if self.clickable:
            raise NotImplemented

        return

class Enemy(Entity):

    def __init__(self, model: EnemyModel, **kwargs):
        super(Enemy, self).__init__(**kwargs)

        self.model = model
        ENEMY_GROUP.add(self)


    def update(self):


        if not self.model.is_alive:
            ENEMY_GROUP.remove(self)



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





