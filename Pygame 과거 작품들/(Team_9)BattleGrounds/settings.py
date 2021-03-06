import pygame as pg
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
YELLOW2 = (200,150,0)
DESERT = (204, 153, 0)
FOREST = (0, 204, 0)
CITY = (153,153,153)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 480  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = DARKGREY

TILESIZE = 16
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE
FONT_NAME = 'Impact'

# Player settings
PLAYER_SPEED = 180
PLAYER_HEALTH = 100
CHALLENGER_HEALTH = 100
