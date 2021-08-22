import pygame

FPS = 60
SIZE = WIDTH, HEIGHT = 960, 960
N_TILES = 10
TILE_SIZE = int(WIDTH/N_TILES)

ENEMY_POS = [int(N_TILES/2)-1, int(N_TILES/4)]

CENTRAL_WEAPON_POS = [int(N_TILES/2)-1, int(3*N_TILES/4)]

#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

IMAGES ={"sword_0": pygame.image.load(r'D:\Projekte\Python\CIAD-Idle\resources\fantasy\64\swordWood.png'),
         "wand_0":  pygame.image.load(r'D:\Projekte\Python\CIAD-Idle\resources\fantasy\64\wand.png'),

         "enemy": [pygame.image.load(r'D:\Projekte\Python\CIAD-Idle\resources\enemies\Transparent PNG\frame-1.png'),
                   pygame.image.load(r'D:\Projekte\Python\CIAD-Idle\resources\enemies\Transparent PNG\frame-2.png'),
                   pygame.image.load(r'D:\Projekte\Python\CIAD-Idle\resources\enemies\Transparent PNG\frame-3.png'),
                   pygame.image.load(r'D:\Projekte\Python\CIAD-Idle\resources\enemies\Transparent PNG\frame-4.png'),
                   pygame.image.load(r'D:\Projekte\Python\CIAD-Idle\resources\enemies\Transparent PNG\frame-5.png'),
                   pygame.image.load(r'D:\Projekte\Python\CIAD-Idle\resources\enemies\Transparent PNG\frame-6.png'),
                   pygame.image.load(r'D:\Projekte\Python\CIAD-Idle\resources\enemies\Transparent PNG\frame-7.png'),
                   pygame.image.load(r'D:\Projekte\Python\CIAD-Idle\resources\enemies\Transparent PNG\frame-8.png')]}