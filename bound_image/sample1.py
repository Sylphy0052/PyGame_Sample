import pygame
from pygame.locals import *
import sys

SCR_WIDTH, SCR_HEIGHT = 640, 480

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
    pygame.display.set_caption("Moving Images and bound")

    img = pygame.image.load("python.png").convert_alpha()
    img_rect = img.get_rect()

    vx = vy = 6
    clock = pygame.time.Clock()

    while True:
        # fps=60
        clock.tick(60)
        img_rect.move_ip(vx, vy)
        if img_rect.left < 0 or img_rect.right > SCR_WIDTH:
            vx = -vx
        if img_rect.top < 0 or img_rect.bottom > SCR_HEIGHT:
            vy = -vy

        screen.fill((0, 0, 255))
        screen.blit(img, img_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit()
