import pygame
from pygame.locals import *
import sys

SCREEN_SIZE = (640, 480)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(u"ウィンドウの作成")
    while True:
        screen.fill((0, 0, 255))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
