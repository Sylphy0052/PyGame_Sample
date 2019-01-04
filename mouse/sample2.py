import pygame
from pygame.locals import *
import sys

SCREEN_SIZE = (640, 480)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Mouse event")

    backImg = pygame.image.load("moriyama.jpg").convert()
    pythonImg = pygame.image.load("python.png").convert_alpha()

    cur_pos = (0, 0)
    pythons_pos = []

    while True:
        screen.blit(backImg, (0, 0))

        mouse_pressed = pygame.mouse.get_pressed()

        if mouse_pressed[0]:
            x, y = pygame.mouse.get_pos()
            x -= pythonImg.get_width() / 2
            y -= pythonImg.get_height() / 2
            pythons_pos.append((x, y))

        x, y = pygame.mouse.get_pos()
        x -= pythonImg.get_width() / 2
        y -= pythonImg.get_height() / 2
        cur_pos = (x, y)

        screen.blit(pythonImg, cur_pos)
        for i, j in pythons_pos:
            screen.blit(pythonImg, (i, j))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
