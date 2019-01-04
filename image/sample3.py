import pygame
from pygame.locals import *
import sys

SCREEN_SIZE = (640, 480)

def load_image(filename, colorkey=None):
    try:
        image = pygame.image.load(filename)
    except (pygame.error, message):
        print("Cannot load image: {}".format(filename))
        raise (SystemExit, message)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Function of Image Load")

    planeImg, planeRect = load_image("plane.png", colorkey=-1)

    while True:
        screen.fill((0,0,0))
        screen.blit(planeImg, (200,100))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
