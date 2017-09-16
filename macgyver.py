"""
MacGyver Maze
WIN : Reach the 3 artifacts to send to sleep the guard and exit
"""


from classy import *
from pygame.locals import *


# Init
pygame.init()
window = pygame.display.set_mode((680, 680))
icone = pygame.image.load("img/mac.png").convert_alpha()
pygame.display.set_icon(icone)
pygame.display.set_caption("MacGyver")

# Init Generate Display of the level
Level = Maping()
Level.generate()
Level.display(window)

# Creation of MacGyver
Mac = Characters(1, 1, "img/mac.png", Level)

# Creation of the Guard
Keeper = Characters(15, 14, "img/keeper.png", Level)

# Creation of items / Edition of Level.map
Needle = Items("N", "img/needle.png", Level)
Needle.display(window)
Level.map[Needle.case_y][Needle.case_x] = Needle.id
Ether = Items("E", "img/ether.png", Level)
Ether.display(window)
Level.map[Ether.case_y][Ether.case_x] = Ether.id
Tube = Items("T", "img/tube.png", Level)
Tube.display(window)
Level.map[Tube.case_y][Tube.case_x] = Tube.id

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
    Needle.display(window)
    Ether.display(window)
    Tube.display(window)

    if Keeper.health > 0:
        window.blit(Keeper.sprite, (Keeper.x, Keeper.y))
    else:
        Keeper.chgsprite("img/rip.png")
        window.blit(Keeper.sprite, (Keeper.x, Keeper.y))
    if Mac.health > 0:
        window.blit(Mac.sprite, (Mac.x, Mac.y))
    else:
        Mac.chgsprite("img/rip.png")
        window.blit(Mac.sprite, (Mac.x, Mac.y))

    # Items gestion
    if Level.map[Mac.case_y][Mac.case_x] == 'N':
        Needle.damage()
        Level.map[Mac.case_y][Mac.case_x] = '0'
        Mac.getitem()
    if Level.map[Mac.case_y][Mac.case_x] == 'E':
        Ether.damage()
        Level.map[Mac.case_y][Mac.case_x] = '0'
        Mac.getitem()
    if Level.map[Mac.case_y][Mac.case_x] == 'T':
        Tube.damage()
        Level.map[Mac.case_y][Mac.case_x] = '0'
        Mac.getitem()

    # Fight
    if Level.map[Mac.case_y][Mac.case_x] == 'K':
        if Mac.items >= 3:
            Keeper.damage()
            Level.map[Mac.case_y][Mac.case_x] = '0'

        else:
            continue_game = 0
            print("GAME OVER")

    # WIN
    if Level.map[Mac.case_y][Mac.case_x] == 'A':
        if Mac.items >= 3:
            continue_game = 0
            print("WIN")

    # Refresh
    pygame.display.flip()

