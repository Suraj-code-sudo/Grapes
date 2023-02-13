import pygame
import math
from time import *

pygame.init()
screen = pygame.display.set_mode((700, 700))

black = (0, 0, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)

ex = 50
ey = 350
oe = 0
om = 0
a = 1

while a == 1:
    screen.fill(black)

    ex = math.cos(oe) * 300 + 350
    ey = -math.sin(oe) * 300 + 350

    oe += .002
    om += 0.01

    pygame.draw.circle(screen, yellow, (350, 350), 50)
    pygame.draw.circle(screen, blue, (int(ex), int(ey)), 15)

    pygame.display.flip()
    sleep(.010)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = 0

pygame.quit()
