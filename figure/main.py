import pygame
from pygame.locals import *
import sys

SCREEN_SIZE = (640, 480)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Draw figures")
    while True:
        screen.fill((0, 0, 255))

        # 矩形 rect(Surface, 色, Rect(左上の座標, 幅, 高さ))
        pygame.draw.rect(screen, (255, 255, 0), Rect(10, 10, 300, 200))
        # 円 circle(Surface, 色, 中心座標, 半径)
        pygame.draw.circle(screen, (255, 0, 0), (320, 240), 100)
        # 楕円 ellipse(Surface, 色, (左上の座標, 幅, 高さ))
        pygame.draw.ellipse(screen, (255, 0, 255), (400, 300, 200, 100))
        # 直線 line(Surface, 色, 始点, 終点)
        pygame.draw.line(screen, (255, 255, 255), (0, 0), (640, 480))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
