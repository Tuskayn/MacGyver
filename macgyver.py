"""
MacGyver Maze
WIN : Reach the 3 artifacts to send to sleep the guard and exit
"""

import pygame
from classy import *
from pygame.locals import *


pygame.init()
window = pygame.display.set_mode((680, 680))
icone = pygame.image.load("img/mac.png").convert_alpha()
pygame.display.set_icon(icone)
pygame.display.set_caption("MacGyver")


#Init Generate Display of the level


Level = Maping()
Level.generate()
Level.display(window)


#Creation of MacGyver


Mac = Characters(2, 2, "img/mac.png", Level)


continue_game = 1
while continue_game:
    pygame.time.Clock().tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            continue_game = 0
        if event.type == KEYDOWN:
            if event.key == K_UP:
                Mac.move('up')
            if event.key == K_LEFT:
                Mac.move('left')
            if event.key == K_DOWN:
                Mac.move('down')
            if event.key == K_RIGHT:
                Mac.move('right')
    Level.display(window)
    window.blit(Mac.sprite, (Mac.x, Mac.y))
    pygame.display.flip()
    if Level.level[Mac.case_y][Mac.case_x] == 'A':
        continue_game = 0
