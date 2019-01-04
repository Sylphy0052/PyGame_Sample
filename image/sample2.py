import pygame
from pygame.locals import *
import sys

SCREEN_SIZE = (640, 480)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(u"Draw images 透明色")

    planeImg = pygame.image.load("plane.png").convert()

    planeImg2 = pygame.image.load("plane.png").convert()
    colorkey = planeImg2.get_at((0,0))
    planeImg2.set_colorkey(colorkey, RLEACCEL)

    while True:
        screen.fill((0,0,0))
        screen.blit(planeImg, (100,100))
        screen.blit(planeImg2, (200,100))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
