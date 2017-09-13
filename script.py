import pygame
from pygame.locals import *

def refresh():
    fenetre.blit(logo, (0, 0))
    fenetre.blit(fond, (0, 100))
    fenetre.blit(perso, (position_perso_x, position_perso_y))
    pygame.display.flip()


pygame.init()

fenetre = pygame.display.set_mode((600, 700))

fond = pygame.image.load("img/fond.jpg").convert()
logo = pygame.image.load("img/logo.png").convert_alpha()


perso = pygame.image.load("img/mac.png").convert_alpha()
position_perso_x = 0
position_perso_y = 100


refresh()


continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_w:
                position_perso_y = position_perso_y - 40
            if event.key == K_a:
                position_perso_x = position_perso_x - 40
            if event.key == K_s:
                position_perso_y = position_perso_y + 40
            if event.key == K_d:
                position_perso_x = position_perso_x + 40
    refresh()
