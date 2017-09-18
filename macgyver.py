# -*- coding: Utf-8 -*

"""
MacGyver Maze
WIN : Reach the 3 artifacts to send to sleep the guard and exit
"""

from classy import *
from constant import *
from pygame.locals import *
import pygame

# Pygame Init
pygame.init()
window = pygame.display.set_mode(c_window)
icon = pygame.image.load(c_icon).convert_alpha()
pygame.display.set_icon(icon)
pygame.display.set_caption(c_title)
myfont = pygame.font.SysFont('Monospace', 20, True)

# Pygame objects
stone = pygame.image.load(c_stone).convert_alpha()
logo = pygame.image.load(c_logo).convert_alpha()
start = pygame.image.load(c_start).convert_alpha()
loses = pygame.image.load(c_died).convert_alpha()
wins = pygame.image.load(c_win).convert_alpha()

# Sounds
m_mac = pygame.mixer.Sound(c_m_mac)
m_mac.set_volume(0.05)
m_zelda = pygame.mixer.Sound(c_m_zelda)
m_zelda.set_volume(0.03)
m_lose = pygame.mixer.Sound(c_m_lose)
m_lose.set_volume(0.5)
m_win = pygame.mixer.Sound(c_m_win)
m_win.set_volume(0.05)
m_music = pygame.mixer.Sound(c_m_music)
m_music.set_volume(0.05)


# Main loop
gamestatu = 1
while gamestatu:
    useready = 1
    continue_game = 1
    m_mac.play()
    # 'Press Start' loop
    while useready:
        window.blit(stone, c_pstone)
        window.blit(start, c_pstart)
        pygame.display.flip()
        pygame.time.Clock().tick(30)
        # Event check of userready loop
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                gamestatu = 0
                useready = 0
                continue_game = 0
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    continue_game = 1
                    useready = 0
                    m_mac.stop()

        if useready == 0:
            # Creation of the map and display it
            Level = Maping()
            Level.display(window)
            # Creation of MacGyver
            Mac = Characters(c_xmac, c_ymac, c_mac, Level)

            # Creation of the Guard
            Keeper = Characters(c_xkeep, c_ykeep, c_keeper, Level)

            # Creation of items and display it
            Needle = Items("N", c_needle, Level)
            Needle.display(window)
            Ether = Items("E", c_ether, Level)
            Ether.display(window)
            Tube = Items("T", c_tube, Level)
            Tube.display(window)

    # Game loop
    while continue_game:
        m_music.play()
        inventory = myfont.render(Mac.inventory(), False, (255, 255, 255))
        pygame.time.Clock().tick(30)
        # Event check of Game loop
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                m_music.stop()
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

        # Items gestion
        if Level.map[Mac.case_y][Mac.case_x] == Needle.id:
            Needle.damage()
            Mac.getitem()
            if Mac.items >= 3:
                m_music.stop()
                m_zelda.play()
        if Level.map[Mac.case_y][Mac.case_x] == Ether.id:
            Ether.damage()
            Mac.getitem()
            if Mac.items >= 3:
                m_music.stop()
                m_zelda.play()
        if Level.map[Mac.case_y][Mac.case_x] == Tube.id:
            Tube.damage()
            Mac.getitem()
            if Mac.items >= 3:
                m_zelda.play()

        # Meet the guard
        if Level.map[Mac.case_y][Mac.case_x] == 'K':
            if Mac.items >= 3:
                Keeper.damage()
                Level.map[Mac.case_y][Mac.case_x] = '0'

            # LOSE
            else:
                lose = 1
                m_music.stop()
                m_lose.play()
                while lose:
                    pygame.time.Clock().tick(30)
                    window.blit(loses, c_pdied)
                    for event in pygame.event.get():
                        if event.type == KEYDOWN and event.key == K_ESCAPE:
                            lose = 0
                            continue_game = 0
                            m_lose.stop()
                            m_mac.play()
                    pygame.display.flip()
        # WIN
        if Level.map[Mac.case_y][Mac.case_x] == 'A' and Mac.items >= 3:
            win = 1
            m_music.stop()
            m_win.play()
            while win:
                pygame.time.Clock().tick(30)
                window.blit(wins, c_pwin)
                for event in pygame.event.get():
                    if event.type == KEYDOWN and event.key == K_ESCAPE:
                        win = 0
                        continue_game = 0
                        m_win.stop()
                        m_mac.play()
                pygame.display.flip()

        # Rebuild
        if continue_game:
            window.blit(stone, c_pstone)
            window.blit(logo, c_plogo)
            window.blit(inventory, c_pinv)
            Level.display(window)
            Needle.display(window)
            Ether.display(window)
            Tube.display(window)
            # Rebuild of the Characters
            if Keeper.health > 0:
                window.blit(Keeper.sprite, (Keeper.x, Keeper.y))
            else:
                Keeper.chgsprite(c_rip)
                window.blit(Keeper.sprite, (Keeper.x, Keeper.y))
            window.blit(Mac.sprite, (Mac.x, Mac.y))

        # Refresh
        pygame.display.flip()
