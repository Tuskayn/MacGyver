"""
Class for MacGyver Maze
"""


import pygame
import random


class Maping:
    """Class to create the map"""
    def __init__(self):
        """Initial settings for the class"""
        self.file = "maps/map1.txt"
        self.map = ''

    def generate(self):
        """Generate a map from a file thru list"""
        with open(self.file, 'r') as file:
            level_map = []
            for line in file:
                line_level = []
                for sprite in line:
                    if sprite != '\n':
                        line_level.append(sprite)
                level_map.append(line_level)
            self.map = level_map

    def display(self, window):
        """Display the map from the generation"""
        wall = pygame.image.load("img/wall.png").convert_alpha()
        flor = pygame.image.load("img/flor40.jpg").convert()
        num_line = 0
        for line in self.map:
            num_case = 0
            for sprite in line:
                x = num_case * 40
                y = num_line * 40
                if sprite == '1':
                    window.blit(wall, (x, y))
                else:
                    window.blit(flor, (x, y))
                num_case += 1
            num_line += 1


class Characters:
    """Class to create a character"""
    def __init__(self, cx, cy, path, level):
        """Initial settings for the class"""
        self.items = 0
        self.health = 1
        self.case_x = cx
        self.case_y = cy
        self.x = self.case_x * 40
        self.y = self.case_y * 40
        self.level = level
        self.sprite = pygame.image.load(path).convert_alpha()

    def chgsprite(self, path):
        self.sprite = pygame.image.load(path).convert_alpha()

    def move(self, direction):
        """Methode to move the hero"""
        if direction == 'right':
            if self.case_x < 16:
                if self.level.map[self.case_y][self.case_x+1] != '1':
                    self.case_x += 1
                    self.x = self.case_x * 40
        if direction == 'left':
            if self.case_x > 0:
                if self.level.map[self.case_y][self.case_x-1] != '1':
                    self.case_x -= 1
                    self.x = self.case_x * 40
        if direction == 'up':
            if self.case_y > 0:
                if self.level.map[self.case_y-1][self.case_x] != '1':
                    self.case_y -= 1
                    self.y = self.case_y * 40
        if direction == 'down':
            if self.case_y < 16:
                if self.level.map[self.case_y+1][self.case_x] != '1':
                    self.case_y += 1
                    self.y = self.case_y * 40

    def getitem(self):
        self.items += 1

    def damage(self):
        self.health -= 1


class Items:
    """Class to create an item"""
    def __init__(self, name,  path, level):
        """Initial settings for the item"""
        self.id = name
        self.health = 1
        self.level = level
        self.case_x, self.case_y = self.randpos()
        self.x = self.case_x * 40
        self.y = self.case_y * 40
        self.sprite = pygame.image.load(path).convert_alpha()


    def randpos(self):
        while True:
            self.case_x = random.randrange(1, 16)
            self.case_y = random.randrange(1, 16)
            if self.level.map[self.case_y][self.case_x] == '0':
                self.level.map[self.case_y][self.case_x] = self.id
                break
        return self.case_x, self.case_y

    def damage(self):
        self.health -= 1

    def display(self, window):
        """Display the item on screen"""
        if self.health > 0:
            window.blit(self.sprite, (self.x, self.y))
