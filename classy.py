"""
Class for MacGyver Maze
"""


import pygame
from pygame.locals import *


class Maping:
    """Method to a"""
    def __init__(self):
        self.file = "maps/map1.txt"
        self.level = 0

    def generate(self):
        with open(self.file, 'r') as file:
            level_map = []
            for line in file:
                line_level = []
                for sprite in line:
                    if sprite != '\n':
                        line_level.append(sprite)
                level_map.append(line_level)
            self.level = level_map

    def display(self, window):
        wall = pygame.image.load("img/wall.png").convert_alpha()
        flor = pygame.image.load("img/flor40.jpg").convert()
        num_line = 0
        for line in self.level:
            num_case = 0
            for sprite in line:
                x = num_case * 40
                y = num_line * 40
                if sprite == '1':
                    window.blit(wall, (x, y))
                elif sprite == '0' :
                    window.blit(flor, (x, y))
                num_case +=1
            num_line +=1


class Characters:
    """Class to create a character"""
    def __init__(self, cx, cy, path, level):
        self.items = 0
        self.health = 1
        self.case_x = cx
        self.case_y = cy
        self.x = self.case_x * 40
        self.y = self.case_x * 40
        self.level = level
        self.sprite = pygame.image.load(path).convert_alpha()

    def alive(self):
        return self.health > 0

    def move(self, direction):
        if direction == 'right':
            if self.case_x < 16:
                if self.level.level[self.case_y][self.case_x+1] != '1':
                    self.case_x += 1
                    self.x = self.case_x * 40
        if direction == 'left':
            if self.case_x > 0:
                if self.level.level[self.case_y][self.case_x-1] != '1':
                    self.case_x -= 1
                    self.x = self.case_x * 40
        if direction == 'up':
            if self.case_y > 0:
                if self.level.level[self.case_y-1][self.case_x] != '1':
                    self.case_y -= 1
                    self.y = self.case_y * 40
        if direction == 'down':
            if self.case_y < 16:
                if self.level.level[self.case_y+1][self.case_x] != '1':
                    self.case_y += 1
                    self.y = self.case_y * 40

    def getpos(self):
        return self.position
