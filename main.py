import pygame, random, sys

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
TITLE = 'THIS IS A TITLE'
TEXT_FONT = 'ARIAL.TTF'
FAVICON = 'favicon-32x32.png'
SOUND_1 = 'sound1.ogg'
SOUND_2 = 'sound2.ogg'
SOUND_3 = 'sound3.ogg'
BGMUSIC = 'Separate Ways (Worlds Apart) (2023 Remaster).mp3'

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
FIRESKY = (230, 69, 29)
GOLDBRICK = (181, 101, 29)
SAPPHIRE = (15, 82, 186)

sound1 = pygame.mixer.Sound(SOUND_1)
sound2 = pygame.mixer.Sound(SOUND_2)
sound3 = pygame.mixer.Sound(SOUND_3)
bgmusic = pygame.mixer.Sound(BGMUSIC)

def init_game ():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(TITLE)
    return screen

def handle_events ():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False