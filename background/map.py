import globs

import pygame

from numpy import random
import os

grass = 'grass_tile_'

class Tile(pygame.sprite.Sprite):

    def __init__(self, image, pos, access):

        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.access = access
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]



class Map():

    tile_group = pygame.sprite.Group()

    def __init__(self):

        self.n_width = int(globs.WIDTH/globs.TILE_SIZE)
        self.n_height = int(globs.HEIGHT/globs.TILE_SIZE)


    def _load_random_image(self):

        tile = random.choice(["1", "2", "3"])
        grass_path = os.path.join(os.path.dirname(__file__),
                                  "../resources", "Sprites", "background", grass + tile + ".png")
        surf = pygame.image.load(grass_path)
        return surf


    def random_map(self):

      for i in range(self.n_width):
          for j in range (self.n_height):

              surf = self._load_random_image()
              image = pygame.transform.scale(surf, (globs.TILE_SIZE, globs.TILE_SIZE))

              pos = (i*globs.TILE_SIZE, j*globs.TILE_SIZE)
              new_tile = Tile(image, pos, True)
              self.tile_group.add(new_tile)



















