import pygame
from pygame.locals import *
import sys

SCREEN_SIZE = (640, 480)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Draw images")

    backImg = pygame.image.load("moriyama.jpg").convert()
    pythonImg = pygame.image.load("python.png").convert_alpha()

    while True:
        screen.blit(backImg, (0, 0))
        screen.blit(pythonImg, (320, 400))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
